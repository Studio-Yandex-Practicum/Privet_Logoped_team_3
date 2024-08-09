from dataclasses import dataclass


@dataclass
class Buttons:
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


@dataclass
class Placeholders:
    role: str = 'Выберите роль'
    action: str = 'Выберите действие из меню'


@dataclass
class Messages:
    start: str = (
        'Добро пожаловать в бота "Привет, Логопед!".\n'
        'Давайте познакомимся, выберите свою роль:'
    )
    menu: str = 'Вот с чем я могу Вам помочь:'
    role_logoped: str = (
            'Вы вошли как логопед.\n'
            'Вот с чем я могу Вам помочь:'
    )
    role_parent: str = (
            'Вы вошли как родитель.\n'
            'Вот с чем я могу Вам помочь:'
    )
    confirmation_contact: str = 'Связаться с логопедом?'


@dataclass
class Lexicon:
    buttons: Buttons = Buttons()
    placeholders: Placeholders = Placeholders()
    messages: Messages = Messages()


lexicon = Lexicon()
