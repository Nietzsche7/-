from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    KeyboardButtonPollType
)


start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Выключить"),
            KeyboardButton(text="Включить"),
        ],
        [
            KeyboardButton(text="Шорт"),
            KeyboardButton(text="Лонг"),
        ],
        [
            KeyboardButton(text="Баланс"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder="Выберите действие из меню",
    selective=True
)



