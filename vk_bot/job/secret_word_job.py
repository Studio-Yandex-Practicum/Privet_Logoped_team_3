from api.api_content import ContentApi
from constants import ERROR_MESSAGE

SECRET_WORD_CORRECT = 'Правильно! Вот ваш подарок: {url_gift}'
SECRET_WORD_INCORRECT = 'Неправильно! Но Вы можете попробовать еще раз!'
SERVICE_ERROR = 'Сервис недоступен. Попробуйте позднее'


class SecretWord:

    @staticmethod
    async def check(word):
        # content = await SecretWord._get_secret_word()
        content = await ContentApi.check_secret_word_ad_return_gift()
        if not content:
            return {'text': ERROR_MESSAGE}

        if word == content.code_gift:
            return {'text': SECRET_WORD_CORRECT}
        return {'text': SECRET_WORD_INCORRECT}
