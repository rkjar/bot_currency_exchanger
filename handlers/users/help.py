from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp


@dp.message_handler(CommandHelp(), state=None)
async def bot_help(message: types.Message):
    text = (f"<b>Команды:</b>\n"
            f"<b>/start</b> - Для запуска бота\n"
            f"<b>/help</b> - Справка")
    await message.answer(text)