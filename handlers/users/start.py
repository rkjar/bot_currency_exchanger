from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default import main_menu_keyboard
from loader import dp


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer(\
        f"Это конвертер курса валют.\n"
        f"Ответным сообщением можно указать <b>сумму</b> (по умолчанию 1$)\n"
        f"В появившейся клавиатуре выбрать нужную валюту.", reply_markup=main_menu_keyboard
    )