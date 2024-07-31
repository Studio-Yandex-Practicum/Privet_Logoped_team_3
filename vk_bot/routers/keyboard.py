from vkbottle import Keyboard, Text

BUTTONS_PER_LINE = 2

ROLE_MENU = (
    'Родитель',
    'Логопед'
)

MAIN_MENU = (
    'Полезное видео',
    'Отследить результаты',
    'Оплата',
    'Уведомления',
    'Подарок',
    'Помощь с приложением'
)


def main_keyboard():
    buttons = [
        Text(item) for item in MAIN_MENU
    ]

    return make_keyboard(
        buttons,
        buttons_per_line=BUTTONS_PER_LINE,
        inline=True
    )


def start_keyboard():
    buttons = [
        Text(item) for item in ROLE_MENU
    ]
    return make_keyboard(
        buttons,
        buttons_per_line=BUTTONS_PER_LINE,
        inline=True
    )


def make_keyboard(keyboard_buttons, buttons_per_line=1, inline=False):
    # keyboard = Keyboard(inline=inline)
    keyboard = Keyboard()
    buttons = 0
    len_buttons = len(keyboard_buttons) - 1
    for pos, button in enumerate(keyboard_buttons):
        keyboard.add(button)
        buttons += 1
        if buttons == buttons_per_line and pos != len_buttons:
            buttons = 0
            keyboard.row()
    return keyboard
