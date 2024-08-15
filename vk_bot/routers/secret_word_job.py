import json
from http import HTTPStatus

from api.schemas import ContentOne
from api.utils import async_http_get
from config import bot_env
from constants import CONTENT_PATH

SECRET_WORD_CORRECT = 'Правильно! Вот ваш подарок: {url_gift}'
SECRET_WORD_INCORRECT = 'Неправильно! Но Вы можете попробовать еще раз!'
SERVICE_ERROR = 'Сервис недоступен. Попробуйте позднее'


class SecretWord:

    @staticmethod
    async def check(word):
        try:
            content = await SecretWord._get_secret_word()
            if content and word == content.code_gift:
                return {
                    'text': SECRET_WORD_CORRECT
                }
            return {
                'text': SECRET_WORD_INCORRECT
            }
        except Exception:
            return {
                'text': SERVICE_ERROR
            }


    @staticmethod
    async def _get_secret_word():
        response = await async_http_get(
            # bot_env.url_api + 'content/'
            bot_env.url_api + f'{CONTENT_PATH}'
        )
        if response['status'] == HTTPStatus.OK:
            contents = json.loads(response['text'])
            content = ContentOne.parse_obj(contents[0])
            return content
        return None
