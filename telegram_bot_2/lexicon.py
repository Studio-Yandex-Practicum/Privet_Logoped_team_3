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
    # Payment menu
    pay_full_version: str = 'Оплатить полную версию'
    pay_ios_version: str = 'Как купить на iOS'
    # Help menu
    install_help: str = 'Помощь в установке'
    output_pc: str = 'Вывод на ПК'
    # Confirmation contact menu
    yes: str = 'Да'
    no: str = 'Нет'
    # Back to main menu
    back: str = 'Назад'
    # Notification menu
    delete_notification: str = 'Отключить'
    edit_notification: str = 'Изменить'
    add_notification: str = 'Установить'


class Placeholders(NamedTuple):
    role: str = 'Выберите роль'
    action: str = 'Выберите действие из меню'


class Messages(NamedTuple):
    start: str = (
        'Добро пожаловать в бота "Привет, Логопед!".\n'
        'Давайте познакомимся, выберите свою роль:'
    )
    menu: str = 'Вот чем я могу Вам помочь:'
    role_logoped: str = 'Вы вошли как логопед.\nВот чем я могу Вам помочь:'
    role_parent: str = 'Вы вошли как родитель.\nВот чем я могу Вам помочь:'
    confirmation_contact: str = 'Связаться с логопедом?'
    help_menu: str = 'Меню оплаты:'
    payment_menu: str = 'Вот чем я могу Вам помочь:'
    # Promocode menu
    input_promocode: str = 'Вы можете ввести промокод:'
    # Notification
    notification: str = 'Уведомление:\nТекст уведомления'
    input_time: str = 'Введите время уведомления в формате ЧЧ:ММ'


class Lexicon(NamedTuple):
    buttons: Buttons = Buttons()
    placeholders: Placeholders = Placeholders()
    messages: Messages = Messages()


lexicon = Lexicon()
