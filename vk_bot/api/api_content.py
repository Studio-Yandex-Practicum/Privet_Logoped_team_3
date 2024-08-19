import json
from http import HTTPStatus

from api.schemas import ContentOne
from api.utils import async_http_get
from config import bot_env
from constants import CONTENT_PATH


class ContentApi:
    @staticmethod
    async def get_pay_ios_version():
        """Купить версию для ios."""
        return await ContentApi._get_content()
        # return 'pay_for_ios в процессе реализации'

    @staticmethod
    async def get_pay_full_version():
        """Купить полную версию."""
        return await ContentApi._get_content()
        # return 'pay_full_version в процессе реализации'

    @staticmethod
    async def get_result():
        """Отследить результат."""
        return await ContentApi._get_content()

    @staticmethod
    async def get_help_with_install():
        """Вернуть ссылку на Помощь с установкой."""
        result = await ContentApi._get_content()
        return result

    @staticmethod
    async def get_help_with_pc():
        """Вернуть ссылку на Вывод на ПК."""
        result = await ContentApi._get_content()
        return result

    @staticmethod
    async def get_video():
        """Вернуть ссылку на полезное видео."""
        return await ContentApi._get_content()

    @staticmethod
    async def check_secret_word_ad_return_gift():
        """Проверить код секретного слова и вернуть ссылку на подарок."""
        return await ContentApi._get_content()

    @staticmethod
    async def _get_content():
        """Получить запись из таблицы Content."""
        try:
            response = await async_http_get(
                bot_env.url_api + f'{CONTENT_PATH}'
            )
            if response['status'] == HTTPStatus.OK:
                contents = json.loads(response['text'])
                if len(contents) > 0:
                    content = ContentOne.parse_obj(contents[0])
                    return content
            return None
        except Exception:
            return None
