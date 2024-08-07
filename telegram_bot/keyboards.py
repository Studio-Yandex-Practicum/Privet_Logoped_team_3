from aiogram.types import KeyboardButton  # Кнопки для Reply клавиатуры
from aiogram.types import ReplyKeyboardMarkup  # Клавиатура под полем ввода
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Полезное видео'),
            KeyboardButton(text='Отследить результаты'),
        ],
        [KeyboardButton(text='Оплата'), KeyboardButton(text='Уведомления')],
        [
            KeyboardButton(text='Подарок'),
            KeyboardButton(text='Помощь с приложением'),
        ],
        [KeyboardButton(text='Связаться с логопедом')],
    ],
    # Подстраивает размер кнопок под телефон
    resize_keyboard=True,
    # Скрывает клавиатуру после нажатия кнопки
    one_time_keyboard=True,
    # выводит сообщение в поле ввода во время работы с меню
    input_field_placeholder='Выберите действие из меню',
)


role_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Родитель'), KeyboardButton(text='Логопед')]
    ],
    # Подстраивает размер кнопок под телефон
    resize_keyboard=True,
    # Скрывает клавиатуру после нажатия кнопки
    one_time_keyboard=True,
    # выводит сообщение в поле ввода во время работы с меню
    input_field_placeholder='Выберите роль',
)


confirmation_contact_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Да', url='https://t.me/BotFather'),
            InlineKeyboardButton(text='Нет', callback_data='main_menu'),
        ]
    ]
)
