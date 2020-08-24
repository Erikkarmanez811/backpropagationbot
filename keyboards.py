from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
import numpy as np
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='close')
        ],
        [
            KeyboardButton(text='Digit Recognizer'),
            #KeyboardButton(text='')
        ]

],resize_keyboard=True
)
random_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/backpropagation')
        ]
],resize_keyboard=True
)