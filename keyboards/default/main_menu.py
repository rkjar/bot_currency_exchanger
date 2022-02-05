from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


button_1 = "DOLLAR to RUB"
button_2 = "DOLLAR to BTC"
button_3 = "DOLLAR to ETH"
button_4 = "DOLLAR to EURO"
main_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(button_1),
            KeyboardButton(button_2)
        ],
        [
            KeyboardButton(button_3),
            KeyboardButton(button_4)
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)