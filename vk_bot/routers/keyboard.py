from vkbottle import Keyboard, Text


def main_keyboard():
    buttons = [
        Text('Полезное видео'),
        Text('Отследить результаты'),
        Text('Оплата'),
        Text('Уведомления'),
        Text('Подарок'),
        Text('Помощь с приложением')
    ]
    return make_keyboard(buttons, buttons_per_line=2, inline=True)


def make_keyboard(keyboard_buttons, buttons_per_line=1, inline=True):
    keyboard = Keyboard(inline=inline)
    buttons = 0
    len_buttons = len(keyboard_buttons) - 1
    for pos, button in enumerate(keyboard_buttons):
        keyboard.add(button)
        buttons += 1
        if buttons == buttons_per_line and pos != len_buttons:
            buttons = 0
            keyboard.row()
    return keyboard
