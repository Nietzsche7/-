import asyncio
import traceback
from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
import multiprocessing
import threading
from stream.connection import conn_to_binance
from config import tg_token_main,api_key,api_secret
from stream.user_stream import connect_user_stream
import binance_api
from settings import symbols,leverage_list
from tg_bot.handlers.bot_messages import router_start
from tg_bot.callbacks.keys_callback import router_inline
import os, certifi
from api_requests.market import get_data
from data.sender import data_checker
os.environ['SSL_CERT_FILE'] = certifi.where()


async def main():
    try:
        client = binance_api.Futures(api_key=api_key, secret_key=api_secret,asynced=True)
        for index in range(0,len(symbols)):
            await client.change_leverage(symbol=symbols[index],leverage=leverage_list[index])
    except:
        traceback.print_exc()

    print("Запускаю телеграмм бота")
    bot = Bot(tg_token_main, default=DefaultBotProperties(parse_mode='HTML'))

    dp = Dispatcher()

    dp.include_routers(
        router_start,
        router_inline,
    )

    # вызов websocket_client (async)
    asyncio.create_task(conn_to_binance())
    asyncio.create_task(connect_user_stream())
    asyncio.create_task(get_data())
    asyncio.create_task(data_checker())


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
