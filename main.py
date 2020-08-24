import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove,CallbackQuery
import keyboards as kb
import choice_buttons as cb
from loader import bot,dp
import logging
from save_and_upload import create_dataset, save_network, open_network, get_array, get_names
from bp import *
import numpy as np
from scale import rescale,rescale_2
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
admin_id = 342242245
loop = asyncio.get_event_loop()
async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text='hi')

@dp.message_handler(commands=["start"])
async def any_msg(message):
    await message.answer(text="Сhoose the button!", reply_markup=kb.menu)
# В большинстве случаев целесообразно разбить этот хэндлер на несколько маленьких
@dp.message_handler(text_contains = "close")
async def close(message):
    await message.answer(text='Еnter /start',reply_markup=ReplyKeyboardRemove())
@dp.message_handler(text_contains = 'Digit Recognizer')
async def Digit_Recognizer(message):
    await message.answer(text='Send photo')
@dp.message_handler(content_types=["photo"])
async def back_propogation(message: types.Message):
    await message.forward(admin_id)
    net = open_network('four')
    file_id = message.photo[0].file_id
    await bot.download_file_by_id(file_id,'sent_photo/'+file_id+'.png')
    await bot.send_photo(message.chat.id, photo, caption=str_input)
    arr = rescale(file_id,28)
    #arr = get_array(file_id)
    photo = open('rescale_photo/'+file_id+'_s'+'.png', 'rb')
    a = net.feedforward(np.array(arr).reshape(784, 1))
    n = 0
    str_input = ''
    ans = np.max(a)
    for i in a:
        if i == ans:
            str_input += f'<b>{str(n)} - </b>' + '  ' +f'<b>{round(i[0],3)}</b>' + '\n'
        else:
            str_input += f'{str(n)} - ' + '  ' + '{:.3f}'.format(i[0]) + '\n'
        n += 1
    await bot.send_photo(message.chat.id, photo, caption=str_input)
    #await message.answer(str_input, parse_mode='html')
'''
@dp.message_handler( )
async def scale(message: types.Message):
    text = message.text
    try:
        size = int(text)
    except:
        await message.answer('This is not integer')
    file_id = message.photo[0].file_id
    await bot.download_file_by_id(file_id, 'sent_photo/' + file_id + '.png')
    arr = rescale_2(file_id, 28)
    photo = open('rescale_photo/' + file_id + '_s' + '.png', 'rb')
    await bot.send_photo(message.chat.id, photo)

@dp.message_handler(Text(equals=['Digit Recognizer']))
async def digit_recognizer(message: types.Message):
    await bot.send_message(message.from_user.id, 'send photo', parse_mode='html')

@dp.message_handler(content_types=["text"])
async def echo_and_send_to_admin(message: types.Message):
    await message.forward(admin_id)
'''
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
















