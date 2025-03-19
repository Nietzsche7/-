import traceback
import asyncio
from settings import symbols,stop_limit
import binance_api
from config import api_key,api_secret
from data.sender import trading_pairs
from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from config import tg_token_main,admin_id
import asyncio

bot = Bot(tg_token_main, default=DefaultBotProperties(parse_mode='HTML'))


async def account_updates(ws,message):
    client = binance_api.Futures(api_key=api_key, secret_key=api_secret,asynced=True)

    try:
        if message['e'] == "ORDER_TRADE_UPDATE":
            print(message)

            if 'o' in message and 's' not in message:
                symbol = message['o']['s']

                if symbol not in symbols:
                    return

                order_type = message['o']['o']
                execution_type = message['o']['x']
                order_id = message['o']['i']
                order_status = message['o']['X']
                order_side = message['o']['S']
                order_filled_price = float(message['o']['L'])
                last_filled_qty = float(message['o']['l'])
                order_qty = float(message['o']['q'])

                print(order_filled_price)

                price = float(message['o']['p'])
                print(symbol,order_side,order_type,order_status)

                # trading_pairs.trading_symbols[symbol]['side'] = "BUY"
                # trading_pairs.trading_symbols[symbol]['enter'] = 0.5571
                # trading_pairs.trading_symbols[symbol]['take'] = 0.5599
                # trading_pairs.trading_symbols[symbol]['stop'] = 0.5554
                # trading_pairs.trading_symbols[symbol]['in_pos'] = True

                if order_status == "NEW" and\
                        order_type == "MARKET" and\
                        trading_pairs.trading_symbols[symbol]['in_pos'] is False and\
                        trading_pairs.trading_symbols[symbol]['side'] is None:

                    print("New pos")

                elif order_status == "FILLED" and\
                        order_type == "MARKET" and\
                        trading_pairs.trading_symbols[symbol]['in_pos'] is True and\
                        order_side != trading_pairs.trading_symbols[symbol]['side']:

                    print("Pos closed")

                    entry_price = trading_pairs.trading_symbols[symbol]['enter']
                    take_profit = trading_pairs.trading_symbols[symbol]['take']
                    stop_loss = trading_pairs.trading_symbols[symbol]['stop']
                    side = trading_pairs.trading_symbols[symbol]['side']

                    if side == "BUY":
                        if order_filled_price > entry_price:
                            profit_percent = calculate_profit_loss(side, entry_price, take_profit)
                            result = f"Take Profit (+{profit_percent}%)"
                        elif order_filled_price < entry_price:
                            loss_percent = calculate_profit_loss(side, entry_price, stop_loss)
                            result = f"Stop Loss ({loss_percent}%)"
                    elif side == "SELL":
                        if order_filled_price < entry_price:
                            profit_percent = calculate_profit_loss(side, entry_price, take_profit)
                            result = f"Take Profit (+{profit_percent}%)"
                        elif order_filled_price > entry_price:
                            loss_percent = calculate_profit_loss(side, entry_price, stop_loss)
                            result = f"Stop Loss ({loss_percent}%)"


                    exit_message = format_exit_signal(symbol, side, entry_price, take_profit, stop_loss, result)


                    await trading_pairs.trading_symbols[symbol]['signals'].reply(text=exit_message)

                    trading_pairs.trading_symbols[symbol]['signals'] = None
                    trading_pairs.trading_symbols[symbol]['in_pos'] = False
                    trading_pairs.trading_symbols[symbol]['side'] = None
                    trading_pairs.trading_symbols[symbol]['take'] = None
                    trading_pairs.trading_symbols[symbol]['stop'] = None
                    trading_pairs.trading_symbols['pairs_in_pos'] -= 1

                    if "Stop Loss" in result:
                        trading_pairs.trading_symbols['stop_count'] += 1
                        if trading_pairs.trading_symbols['stop_count'] >= stop_limit:
                            trading_pairs.trading_status = "off"

                    await client.cancel_open_orders(symbol)

                elif order_status == "NEW" and order_type == "TAKE_PROFIT_MARKET" and trading_pairs.trading_symbols[symbol]['take'] is None:
                    print("Тейк есть, цена",float(message['o']['sp']))
                    take_price = float(message['o']['sp'])
                    trading_pairs.trading_symbols[symbol]['take'] = take_price

                elif order_status == "NEW" and order_type == "STOP_MARKET" and trading_pairs.trading_symbols[symbol]['stop'] is None:
                    print("Стоп исполнен, цена",float(message['o']['sp']))
                    stop_price = float(message['o']['sp'])
                    trading_pairs.trading_symbols[symbol]['stop'] = stop_price
        await client.close()



    except:
        traceback.print_exc()

async def on_open(ws):
    print("Поток пользователя запущен")

async def connect_user_stream():
    client_binance = binance_api.Futures(api_key=api_key, secret_key=api_secret, testnet=False, asynced=True)

    ws = await client_binance.websocket_userdata(on_message=account_updates,on_open=on_open)
    while True:
        await asyncio.sleep(60)

def format_trade_signal(symbol, order_side, entry_price, take_profit, stop_loss,exchange):
    emoji_side = "🔴" if order_side == "SELL" else "🟢"
    return (
        f"🚀 <b>Монета</b>: {symbol} - {exchange}\n"
        f"{emoji_side} <b>Тип сделки</b>: {order_side.capitalize()}\n"
        f"🔹 <b>Цена входа</b>: {entry_price} USDT\n"
        f"🔸 <b>Take Profit</b>: {take_profit} USDT\n"
        f"🔻 <b>Stop Loss</b>: {stop_loss} USDT\n"
    )

# Формирование сообщения о выходе из сделки
def format_exit_signal(symbol, order_side, entry_price, take_profit, stop_loss, result):
    emoji_side = "🔴" if order_side == "SELL" else "🟢"
    if "Take Profit" in result:
        emoji = "✅"
    else:
        emoji = "❌"

    return (
        f"🚀 <b>Монета</b>: {symbol}\n"
        f"{emoji_side} <b>Тип сделки</b>: {order_side.capitalize()}\n"
        f"🔹 <b>Цена входа</b>: {entry_price} USDT\n"
        f"🔸 <b>Take Profit</b>: {take_profit} USDT\n"
        f"🔻 <b>Stop Loss</b>: {stop_loss} USDT\n\n"
        f"{emoji} <b>Результат</b>: {result}\n"
    )

def calculate_profit_loss(order_side, entry_price, exit_price):
    if order_side == "BUY":
        return round(((exit_price - entry_price) / entry_price) * 100, 2)
    elif order_side == "SELL":
        return round(((entry_price - exit_price) / entry_price) * 100, 2)

if __name__ == '__main__':
    message = {'e': 'ORDER_TRADE_UPDATE', 'T': 1729161129702, 'E': 1729161129703, 'o': {'s': 'XRPUSDT', 'c': 'dN3iz4QQjUOC5XVqeEuYsQ', 'S': 'SELL', 'o': 'MARKET', 'f': 'GTC', 'q': '39.4', 'p': '0', 'ap': '0.55560', 'sp': '0.5556', 'x': 'TRADE', 'X': 'FILLED', 'i': 68073466639, 'l': '39.4', 'z': '39.4', 'L': '0.5556', 'n': '0.01094532', 'N': 'BNFCR', 'T': 1729161129702, 't': 1623642341, 'b': '0', 'a': '0', 'm': False, 'R': True, 'wt': 'CONTRACT_PRICE', 'ot': 'STOP_MARKET', 'ps': 'BOTH', 'cp': True, 'rp': '-0.06304000', 'pP': False, 'si': 0, 'ss': 0, 'V': 'NONE', 'pm': 'NONE', 'gtd': 0}}
    asyncio.run(account_updates(0,message))