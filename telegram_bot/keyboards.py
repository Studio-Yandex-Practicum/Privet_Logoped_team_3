from aiogram.types import KeyboardButton  # Кнопки для Reply клавиатуры
from aiogram.types import ReplyKeyboardMarkup  # Клавиатура под полем ввода
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lexicon import lexicon

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=lexicon.buttons.usefull_video),
            KeyboardButton(text=lexicon.buttons.track_results),
        ],
        [
            KeyboardButton(text=lexicon.buttons.payment),
            KeyboardButton(text=lexicon.buttons.notifications),
        ],
        [
            KeyboardButton(text=lexicon.buttons.gift),
            KeyboardButton(text=lexicon.buttons.help),
        ],
        [KeyboardButton(text=lexicon.buttons.contact_logoped)],
    ],
    # Подстраивает размер кнопок под телефон
    resize_keyboard=True,
    # Скрывает клавиатуру после нажатия кнопки
    one_time_keyboard=True,
    # выводит сообщение в поле ввода во время работы с меню
    input_field_placeholder=lexicon.placeholders.action,
)


role_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=lexicon.buttons.parent),
            KeyboardButton(text=lexicon.buttons.logoped),
        ]
    ],
    # Подстраивает размер кнопок под телефон
    resize_keyboard=True,
    # Скрывает клавиатуру после нажатия кнопки
    one_time_keyboard=True,
    # выводит сообщение в поле ввода во время работы с меню
    input_field_placeholder=lexicon.placeholders.role,
)


confirmation_contact_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=lexicon.buttons.yes, url='https://t.me/BotFather'
            ),
            InlineKeyboardButton(
                text=lexicon.buttons.no, callback_data='main_menu'
            ),
        ]
    ]
)
