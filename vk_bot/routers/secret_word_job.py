import json
from http import HTTPStatus

from api.schemas import ContentOne
from api.utils import async_http_get
from config import bot_env


class SecretWord:

    @staticmethod
    async def check(word):
        content = await SecretWord._get_secret_word()
        if word == content.code_gift:
            return {
                'text': 'Правильно! Вот ваш подарок: {url_gift}'
            }
        return {
            'text': 'Неправильно! Но Вы можете попробовать еще раз!'
        }

    @staticmethod
    async def _get_secret_word():
        response = await async_http_get(
            bot_env.url_api + 'content/'
        )
        if response['status'] == HTTPStatus.OK:
            contents = json.loads(response['text'])
            content = ContentOne.parse_obj(contents[0])
        return content
