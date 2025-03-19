import binance_api
import json
import traceback
from stream.sorting import ws_sorting
import asyncio
from settings import timeframe, symbols



async def on_close(ws, **kwargs):
    print("Вебсокет Binance отключен")


async def on_open(ws):
    print("Вебсокет Binance запущен")

async def on_error(ws,e):
    print(e)
    traceback.print_exc()


# Глобальная переменная для хранения вебсокетов
websockets = []

async def conn_to_binance():
    global websockets
    clients = [
        binance_api.Futures(asynced=True, api_key="", secret_key=""),
        binance_api.Futures(asynced=True, api_key="", secret_key=""),
        binance_api.Futures(asynced=True, api_key="", secret_key="")
    ]
    tasks = []
    streams = [f"{symbol.lower()}@kline_{timeframe}" for symbol in symbols]

    #chunk_size = 200
    #chunks = [streams[i:i + chunk_size] for i in range(0, len(streams), chunk_size)]
    print(streams)
    ws = await clients[0].websocket(
        stream=streams,
        on_close=on_close,
        on_open=on_open,
        on_message=ws_sorting,
        on_error=on_error
    )
    await asyncio.sleep(3)

    #await ws.run()

    #await asyncio.gather(*tasks)
    while True:
        await asyncio.sleep(60)

