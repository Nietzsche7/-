import traceback

import binance_api
from settings import symbols,analyzeCounterKlines, timeframe
import asyncio
from datetime import datetime

historical_data = {}
historical_oi = {}

async def get_klines(client_binance):
    #client_binance = binance_api.Futures(api_key="", secret_key="", testnet=False, asynced=True)

    for symbol in symbols:
        klines = await client_binance.klines(limit=5, interval=timeframe, symbol=symbol)

        # Очистка предыдущих данных для символа
        historical_data[symbol] = []

        # Пробегаемся по всем свечам, кроме последней
        for kline in klines[:-1]:
            open_time = kline[0]
            open_price = float(kline[1])
            close_price = float(kline[4])
            volume = float(kline[7])
            close_time = float(kline[6])


            # Добавляем данные в список
            historical_data[symbol].append({
                'volume': volume,
                'open_price': open_price,
                'close_price': close_price,
                'interest': None,  # Эти данные добавишь позже, если они будут
                'close_time': close_time  # Здесь уже формат datetime
            })

        print(f"Symbol: {symbol}, Data length: {len(historical_data[symbol])}")
    #await client_binance.close()



async def fetch_open_interest(symbol):
    """Функция для получения данных об открытом интересе через API"""
    try:
        client = binance_api.Futures(asynced=True, api_key="", secret_key="")
        liveInterest = await client.open_interest(symbol=symbol)
        await client.close()
        return float(liveInterest['openInterest'])  # Возвращаем открытый интерес как float
    except Exception:
        traceback.print_exc()

async def history_open_interest(client):
    if timeframe != "1m":
        #client = binance_api.Futures(asynced=True, api_key="", secret_key="")

        for symbol in symbols:
            historical_oi[symbol] = []
            history_data = await client.open_interest_hist(symbol=symbol,period=timeframe,limit=5)
            for oi in history_data:
                historical_oi[symbol].append(float(oi['sumOpenInterest']))
            for index in range(0,len(historical_data[symbol])):
                historical_data[symbol][index]['interest'] = historical_oi[symbol][index]

        #await client.close()
    else:
        for symbol in symbols:
            for index in range(0,len(historical_data[symbol])):
                historical_data[symbol][index]['interest'] = None

async def get_data():
    client_binance = binance_api.Futures(api_key="", secret_key="", testnet=False, asynced=True)

    await get_klines(client_binance)
    await history_open_interest(client_binance)

    await client_binance.close()


# Теперь один вызов asyncio.run для всех асинхронных задач
#asyncio.run(main())