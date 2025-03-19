from aiogram.types import Message
from aiogram import Bot, Dispatcher, Router, types
from tg_bot.keyboards import reply, inline, builders, fabrics
from aiogram.filters import CommandStart
from tg_bot.keyboards.inline import start_menu

router_start = Router()
#state_trading = StateTrading()


@router_start.message(CommandStart())
async def greetings(message: Message):
    msg_state = await message.reply(text="Панель управления ботом.",reply_markup=inline.start_menu)





