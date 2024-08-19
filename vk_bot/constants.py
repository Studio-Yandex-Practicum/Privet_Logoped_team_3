DB_PATH = 'sqlite:///sqlite.db'

NOTIFICATION_PATH = 'notification/vk/?time='
CONTENT_PATH = 'content/'

LOOPWRAPPER_INTERVAL = 10

USER_TOKEN_MAX_LEN = 15

COMMAND_PREFIXES = ['', '/']
MAIN_MENU_CMD = 'меню'
START_MENU_CMD = 'старт'
GREETING_MESSAGE = ('Добро пожаловать в бота “Привет, Логопед!”. '
                    'команды бота: старт - выбор роли Родитель/Логопед '
                    'меню - Главное меню '
                    'Пожалуйста выберите действия:”')
ROLE_MESSAGE = ('Укажите вашу роль:')
INVITE_MESSAGE = f'Комманды бота {START_MENU_CMD} {MAIN_MENU_CMD}'
ERROR_MESSAGE = 'Данные не загружены, попробуйте позже'

EVENT_MESSAGE = 'Будильник! Будильник! Будильник! '
