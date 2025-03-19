from contextlib import suppress
from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message,CallbackQuery
import tg_bot.keyboards.inline
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from tg_bot.keyboards import inline
from pybit.unified_trading import HTTP
import datetime
from tg_bot.keyboards import fabrics
from aiogram import Bot, Dispatcher, Router, types
from aiogram.client.bot import DefaultBotProperties
from config import tg_token_main
from data.sender import trading_pairs
from config import api_key,api_secret
import binance_api
import asyncio

router_inline = Router()
#state_trading = StateTrading()


class Form(StatesGroup):
    api_key = State()
    api_secret = State()
    depo = State()
    lvg = State()

bot = Bot(tg_token_main, default=DefaultBotProperties(parse_mode='HTML'))


@router_inline.message(F.text == "Включить")
async def trading_on(message: Message, state: FSMContext):
    msg = await message.reply(text="✅Торговля активна✅",reply_markup=inline.start_menu)
    trading_pairs.trading_status = "on"
    trading_pairs.trading_symbols['stop_count'] = 0

@router_inline.message(F.text == "Выключить")
async def trading_on(message: Message, state: FSMContext):
    msg = await message.reply(text="🚫Торговля неактивна🚫", reply_markup=inline.start_menu)
    trading_pairs.trading_status = "off"


@router_inline.message(F.text == "Шорт")
async def trading_on(message: Message, state: FSMContext):
    if trading_pairs.trading_symbols['short_only'] is False:
        msg = await message.reply(text="Теперь торговля будет только в Шорт.", reply_markup=inline.start_menu)
        trading_pairs.trading_symbols['short_only'] = True
    elif trading_pairs.trading_symbols['short_only'] is True:
        msg = await message.reply(text="Режим 'только Шорт' выключен. Теперь торгвля будет в двух направлениях.",
                                  reply_markup=inline.start_menu)
        trading_pairs.trading_symbols['short_only'] = False


@router_inline.message(F.text == "Лонг")
async def trading_on(message: Message, state: FSMContext):
    if trading_pairs.trading_symbols['long_only'] is False:
        msg = await message.reply(text="Теперь торговля будет только в Лонг.", reply_markup=inline.start_menu)
        trading_pairs.trading_symbols['long_only'] = True
    elif trading_pairs.trading_symbols['long_only'] is True:
        msg = await message.reply(text="Режим 'только Лонг' выключен. Теперь торгвля будет в двух направлениях.", reply_markup=inline.start_menu)
        trading_pairs.trading_symbols['long_only'] = False

@router_inline.message(F.text == "Баланс")
async def balance(message: Message):
    client = binance_api.Futures(api_key=api_key, secret_key=api_secret, asynced=True)
    balance = await client.balance()
    total = ""

    for coin in balance:
        if float(coin['availableBalance']) != 0:
            total += coin['availableBalance'] + " " + coin['asset'] + "\n"

    # print(total)
    await message.reply(total)
    await client.close()


