from typing import NamedTuple


class Buttons(NamedTuple):
    # Main menu
    usefull_video: str = 'Полезное видео'
    track_results: str = 'Отследить результаты'
    payment: str = 'Оплата'
    notifications: str = 'Уведомления'
    gift: str = 'Подарок'
    help: str = 'Помощь с приложением'
    contact_logoped: str = 'Связаться с логопедом'
    # Role menu
    parent: str = 'Родитель'
    logoped: str = 'Логопед'
    # Confirmation contact menu
    yes: str = 'Да'
    no: str = 'Нет'
    # Back to main menu
    back: str = 'Назад'


class Placeholders(NamedTuple):
    role: str = 'Выберите роль'
    action: str = 'Выберите действие из меню'


class Messages(NamedTuple):
    start: str = (
        'Добро пожаловать в бота "Привет, Логопед!".\n'
        'Давайте познакомимся, выберите свою роль:'
    )
    menu: str = 'Вот с чем я могу Вам помочь:'
    role_logoped: str = 'Вы вошли как логопед.\nВот с чем я могу Вам помочь:'
    role_parent: str = 'Вы вошли как родитель.\nВот с чем я могу Вам помочь:'
    confirmation_contact: str = 'Связаться с логопедом?'
    # Promocode menu
    input_promocode: str = 'Вы можете ввести промокод:'


class Lexicon(NamedTuple):
    buttons: Buttons = Buttons()
    placeholders: Placeholders = Placeholders()
    messages: Messages = Messages()


lexicon = Lexicon()
