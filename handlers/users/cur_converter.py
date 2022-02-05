from aiogram import types
from loader import dp
from utils import exchanger, output_text

user_input = {}


@dp.message_handler()
async def cur_converter(message: types.Message):
    if message.text.isdigit():
        user_input[message.from_user.id] = float(message.text)
    elif message.text in exchanger.info:
        await message.answer(output_text(message.text, user_input.get(message.from_user.id, 1)))