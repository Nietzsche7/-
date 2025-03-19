import asyncio
import traceback
from datetime import datetime, timedelta
from api_requests.market import fetch_open_interest, historical_data
from settings import analyzeCounterKlines, longRange,shortRange,symbols
import time
import copy
from api_requests.user import place_market_order
import binance_api
from data.sender import trading_pairs
from stream.user_stream import calculate_profit_loss,format_exit_signal

# Словарь для хранения информации по каждой торговой паре (текущее состояние)
open_interest_data = {}


async def calculate_signal(symbol, analyzeCounterKlines):
    # Проверяем, достаточно ли данных по символу
    if len(historical_data[symbol][-analyzeCounterKlines:]) < analyzeCounterKlines:
        return None  # Недостаточно данных для анализа

    # Получаем последние analyzeCounterKlines свечей для анализа
    latest_klines = historical_data[symbol][-analyzeCounterKlines:]


    # Инициализируем переменные для накопления значений
    total_close_prices = 0
    total_volumes = 0
    total_interests = 0
    valid_interest_count = 0


    # Перебираем свечи, кроме последней (она будет текущей для сравнения)
    for i in range(0, analyzeCounterKlines):
        kline = latest_klines[i]

        # Суммируем цены закрытия, объемы и открытый интерес
        total_close_prices += kline['close_price']
        total_volumes += kline['volume']

        if kline['interest'] is not None:
            total_interests += kline['interest']
            valid_interest_count += 1
        else:
            return {
                'avg_close_price': 0,
                'avg_volume': 0,
                'avg_interest': 0
            }

    # Вычисляем средние значения
    avg_close_price = total_close_prices / (analyzeCounterKlines)
    avg_volume = total_volumes / (analyzeCounterKlines)
    avg_interest = total_interests / valid_interest_count if valid_interest_count > 0 else None

    # Возвращаем результаты
    return {
        'avg_close_price': avg_close_price,
        'avg_volume': avg_volume,
        'avg_interest': avg_interest
    }


async def strategy_signal(symbol):
    try:
        signal_data = await calculate_signal(symbol, analyzeCounterKlines)
        print("Информация средних значений", signal_data)
        if any(value == 0 or value is None for value in signal_data.values()):
            print("Нулевые значения или отсутствующие данные, пропуск обработки")
            return

        # Получаем данные текущей (последней) свечи для сравнения
        last_kline = open_interest_data[symbol]['current_kline']

        # Рассчитываем процентное изменение цены, объема и открытого интереса
        price_change_last = (last_kline['close_price'] - signal_data['avg_close_price']) / signal_data['avg_close_price'] * 100
        volume_change_last = (last_kline['volume'] - signal_data['avg_volume']) / signal_data['avg_volume'] * 100
        interest_change_last = (last_kline['interest'] - signal_data['avg_interest']) / signal_data['avg_interest'] * 100

        print(price_change_last,volume_change_last,interest_change_last)
        # Суммируем изменения для оценки общего сигнала
        total_change = price_change_last + volume_change_last + interest_change_last

        # Проверяем условия входа в сделку
        print("Текущее изменение ", total_change)
        if trading_pairs.test_trading_symbol[symbol]['in_pos'] is False:
            if total_change > longRange and trading_pairs.trading_symbols[symbol]['in_pos'] is False:
                # Вход в лонг
                print(f"Open LONG position for {symbol}. Signal value: {total_change}")
                trading_pairs.trading_symbols[symbol]['enter'] = float(last_kline['close_price'])

                await place_market_order(symbol, "BUY", last_kline['close_price'])
                # trading_pairs.trading_symbols[symbol]['in_pos'] = True


            elif total_change < shortRange and trading_pairs.trading_symbols[symbol]['in_pos'] is False:
                # Вход в шорт
                print(f"Open SHORT position for {symbol}. Signal value: {total_change}")
                trading_pairs.trading_symbols[symbol]['enter'] = float(last_kline['close_price'])

                await place_market_order(symbol, "SELL", last_kline['close_price'])

                # trading_pairs.trading_symbols[symbol]['in_pos'] = True
            else:
                print(f"No trade signal for {symbol}. Signal value: {total_change}")
        print("\n")
    except:
        traceback.print_exc()

async def handle_kline_close(symbol, kline_data):
    """Функция, вызываемая при закрытии свечи."""
    try:
        kline_close_time = float(kline_data['T'])
        close_price = float(kline_data['c'])
        volume = float(kline_data['q'])
        open_price = float(kline_data['o'])

        # Получаем открытый интерес на момент закрытия свечи
        open_interest_at_close = await fetch_open_interest(symbol)

        # if open_interest_data[symbol]['current_kline']['start_interest'] is None:
        #     open_interest_data[symbol]['current_kline']['start_interest'] = open_interest_at_close


        open_interest_data[symbol]['current_kline']['volume'] = volume
        open_interest_data[symbol]['current_kline']['close_price'] = close_price
        open_interest_data[symbol]['current_kline']['interest'] = open_interest_at_close
        open_interest_data[symbol]['current_kline']['close_time'] = kline_close_time

        #print("Закрыта свеча:", open_interest_data[symbol]['current_kline'])


        # Ограничиваем размер истории
        if len(historical_data[symbol]) > 510:
            historical_data[symbol].pop(0)

        await strategy_signal(symbol)

        # Переносим свечу из временного хранилища в historical_data
        if open_interest_data[symbol]['current_kline']['interest'] is not None:
            historical_data[symbol].append(copy.deepcopy(open_interest_data[symbol]['current_kline']))

            # Очищаем данные текущей свечи для следующего использования
            open_interest_data[symbol]['current_kline'] = {
                'volume': None,
                'close_price': None,
                'interest': None,
                'close_time': None
            }


    except:
        traceback.print_exc()


async def ws_sorting(ws, message):

    """Основная функция для обработки сообщений по вебсокету."""
    try:
        kline_data = message["data"]['k']
        symbol = message["data"]['s']

        # Инициализация данных по символу, если его еще нет в словаре
        if symbol not in open_interest_data:
            open_interest_data[symbol] = {
                'current_kline':
                    {
                        'volume': None,
                        'close_price': None,
                        'interest': None,
                        'close_time': None
                    }
            }

        # Проверяем, закрыта ли свеча
        is_closed = kline_data['x']

        await check_testing_orders(symbol,float(kline_data['c']))

        if is_closed:
            # Если свеча закрыта, обрабатываем её и отмечаем флаг закрытия
            await handle_kline_close(symbol, kline_data)
            #open_interest_data[symbol]['is_last_kline_closed'] = True

    except:
        traceback.print_exc()

async def check_testing_orders(symbol,order_filled_price):
    if trading_pairs.test_trading_symbol[symbol]['in_pos'] is True:
        take_profit = trading_pairs.test_trading_symbol[symbol]['take']
        stop_loss = trading_pairs.test_trading_symbol[symbol]['stop']
        entry_price = trading_pairs.test_trading_symbol[symbol]['enter']
        order_side = trading_pairs.test_trading_symbol[symbol]['side']
        if order_side == "BUY":
            if order_filled_price >= take_profit:
                profit_percent = calculate_profit_loss(order_side, entry_price, take_profit)
                result = f"Take Profit (+{profit_percent}%)"
            elif order_filled_price <= stop_loss:
                loss_percent = calculate_profit_loss(order_side, entry_price, stop_loss)
                result = f"Stop Loss ({loss_percent}%)"
            else:
                return
        elif order_side == "SELL":
            if order_filled_price <= take_profit:
                profit_percent = calculate_profit_loss(order_side, entry_price, take_profit)
                result = f"Take Profit (+{profit_percent}%)"
            elif order_filled_price >= stop_loss:
                loss_percent = calculate_profit_loss(order_side, entry_price, stop_loss)
                result = f"Stop Loss ({loss_percent}%)"
            else:
                return

        msg = format_exit_signal(symbol,order_side,entry_price,take_profit,stop_loss,result)
        await trading_pairs.test_trading_symbol[symbol]['signals'].reply(msg)

        trading_pairs.test_trading_symbol[symbol]['signals'] = None
        trading_pairs.test_trading_symbol[symbol]['in_pos'] = False
        trading_pairs.test_trading_symbol[symbol]['side'] = None
        trading_pairs.test_trading_symbol[symbol]['take'] = None
        trading_pairs.test_trading_symbol[symbol]['stop'] = None
