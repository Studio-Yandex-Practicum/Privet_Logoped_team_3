from aiogram.types import (
    ReplyKeyboardMarkup,  # Клавиатура под полем ввода
    KeyboardButton,  # Кнопки для Reply клавиатуры
    InlineKeyboardMarkup,  # Клавиатура под сообщениями
    InlineKeyboardButton  # Кнопки для Inline клавиатуры
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
    resize_keyboard=True,  # Подстраивает размер кнопок под телефон
    one_time_keyboard=True,  # Скрывает клавиатуру после нажатия кнопки
    input_field_placeholder="Выберите действие из меню",  # выводит сообщение в поле ввода во время работы с меню

)
