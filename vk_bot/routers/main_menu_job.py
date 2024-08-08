import json
import logging
from http import HTTPStatus

from api.schemas import ContentOne
from api.utils import async_http_get
import bot_cfg
from config import bot_env
from routers.keyboard import HELP_MENU, MAIN_MENU, make_keyboard_menu
from routers.states import States

log = logging.getLogger(__name__)


class MainMenu:

    @staticmethod
    async def response(message, message_base):
        if message == MAIN_MENU[0]:
            return await MainMenu.get_video()
        elif message == MAIN_MENU[1]:
            return await MainMenu.get_result()
        elif message == MAIN_MENU[2]:
            return await MainMenu.get_payment()
        elif message == MAIN_MENU[3]:
            return await MainMenu.get_notification()
        elif message == MAIN_MENU[4]:
            return await MainMenu.get_present(message_base)
        elif message == MAIN_MENU[5]:
            return await MainMenu.get_app_help()

    @staticmethod
    async def get_video():
        content = await MainMenu._get_content()
        return {
            'text': f'Рекомендуем посмотреть это видео: ' + content.url_gift
        }

    @staticmethod
    async def get_payment():
        return {
            'text': 'get_result в процессе реализации'
        }

    @staticmethod
    async def get_notification():
        return {
            'text': 'get_notification в процессе реализации'
        }

    @staticmethod
    async def get_present(message_base):
        await bot_cfg.bot.state_dispenser.set(
            message_base.peer_id,
            States.waiting_for_code
        )
        # await message_base.set_state(States.waiting_for_code)
        return {
            'text': 'Введите секретное слово:'
        }

    @staticmethod
    async def get_result():
        content = await MainMenu._get_content()
        return {
            'text': ('У меня для Вас есть специальный файлик, который '
                     'поможет вам '
                     f'следить за прогрессом ребенка:' + content.track_file)
        }

    @staticmethod
    async def get_app_help():
        return {
            'text': 'Вот чем я могу Вам помочь:',
            'keyboard': make_keyboard_menu(HELP_MENU)
        }

    @staticmethod
    async def _get_content():
        response = await async_http_get(
            bot_env.url_api + 'content/'
        )
        if response['status'] == HTTPStatus.OK:
            contents = json.loads(response['text'])
            content = ContentOne.parse_obj(contents[0])
        return content
