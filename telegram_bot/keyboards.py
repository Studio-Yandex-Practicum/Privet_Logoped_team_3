from aiogram.types import KeyboardButton  # Кнопки для Reply клавиатуры
from aiogram.types import ReplyKeyboardMarkup  # Клавиатура под полем ввода
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import bot_env
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
                text=lexicon.buttons.yes, url=bot_env.owner_tg
            ),
            InlineKeyboardButton(
                text=lexicon.buttons.no, callback_data='main_menu'
            ),
        ]
    ]
)


back_to_main_menu_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=lexicon.buttons.back, callback_data='main_menu'
            )
        ]
    ]
)


help_menu_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=lexicon.buttons.install_help, callback_data='install_help'
            )
        ],
        [
            InlineKeyboardButton(
                text=lexicon.buttons.output_pc, callback_data='present_on_pc'
            )
        ],
    ]
)

payment_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=lexicon.buttons.pay_full_version,
                callback_data='pay_full_version',
            )
        ],
        [
            InlineKeyboardButton(
                text=lexicon.buttons.pay_ios_version,
                callback_data='pay_ios_version',
            )
        ],
    ]
)
