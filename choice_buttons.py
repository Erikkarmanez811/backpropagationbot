from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import URL_APPLES, URL_PEAR
from aiogram.utils.callback_data import CallbackData
buy_callback = CallbackData("buy", "item_name", "quantity")
choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='отмена',callback_data="cancel")
        ],
        [
            InlineKeyboardButton(text='выбор2',callback_data=buy_callback.new(item_name="pear",quantity = 1)),
            InlineKeyboardButton(text='выбор3',callback_data="buy:apple:5")
        ]

],resize_keyboard=True
)
pear_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='купи тут',callback_data=URL_PEAR)
        ]

]
)