from aiogram.types import (
    ReplyKeyboardMarkup,  # Клавиатура под полем ввода
    KeyboardButton,  # Кнопки для Reply клавиатуры
)

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Полезное видео"),
            KeyboardButton(text="Отследить результаты")
        ],
        [
            KeyboardButton(text="Оплата"),
            KeyboardButton(text="Уведомления")
        ],
        [
            KeyboardButton(text="Подарок"),
            KeyboardButton(text="Помощь с приложением")
        ],
        [
            KeyboardButton(text="Связаться с логопедом")
        ]
    ],
    # Подстраивает размер кнопок под телефон
    resize_keyboard=True,
    # Скрывает клавиатуру после нажатия кнопки
    one_time_keyboard=True,
    # выводит сообщение в поле ввода во время работы с меню
    input_field_placeholder="Выберите действие из меню",

)


role_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Родитель"),
            KeyboardButton(text="Логопед")
        ]
    ],
    # Подстраивает размер кнопок под телефон
    resize_keyboard=True,
    # Скрывает клавиатуру после нажатия кнопки
    one_time_keyboard=True,
    # выводит сообщение в поле ввода во время работы с меню
    input_field_placeholder="Выберите роль",
)
