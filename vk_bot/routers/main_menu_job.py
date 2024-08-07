import json
import logging
from http import HTTPStatus

from api.schemas import ContentOne, ContentMany
from api.utils import async_http_get
from config import bot_env

log = logging.getLogger(__name__)


class MainMenu:

    @staticmethod
    async def response(message):
        if message == 'Полезное видео':
            return await MainMenu.get_video()
        elif message == 'Отследить результаты':
            return await MainMenu.get_result()
        elif message == 'Оплата':
            return await MainMenu.get_payment()
        elif message == 'Помощь с приложением':
            return await MainMenu.get_app_help()

    @staticmethod
    async def get_video():
        value = await MainMenu._get_content()
        return value.url_gift

    @staticmethod
    async def get_payment():
        return 'get_result в процессе реализации'

    @staticmethod
    async def get_result():
        return 'get_result в процессе реализации'

    @staticmethod
    async def get_app_help():
        return 'get_app_help в процессе реализации'

    @staticmethod
    async def _get_content():
        response = await async_http_get(
            bot_env.url_api + 'content/'
        )
        if response['status'] == HTTPStatus.OK:
            contents = json.loads(response['text'])
            content = ContentOne.parse_obj(contents[0])
            # content = ContentMany.parse_raw(response['text'])
            # content = [ContentMany(**item) for item in json.loads(response['text'])]
        return content
