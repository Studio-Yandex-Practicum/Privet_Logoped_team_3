import logging
import re

from api.utils import async_http_post
from config import bot_env
from constants import ERROR_MESSAGE

TIME_NOTIFICATION_CORRECT = 'Напоминание сохранено'
TIME_NOTIFICATION_INCORRECT = 'Время введено некорректно, действие отменено'

log = logging.getLogger(__name__)


class TimeNotification:

    @staticmethod
    async def response(time_string, uid):
        if TimeNotification.test_time_format(time_string):
            try:
                await TimeNotification.save_to_db(time_string, uid)
                return {
                    'text': TIME_NOTIFICATION_CORRECT
                }
            except Exception:
                log.error('Error saving time notification: %s')
                return {
                    'text': ERROR_MESSAGE
                }
        return {
            'text': TIME_NOTIFICATION_INCORRECT
        }

    @staticmethod
    def test_time_format(time_string):
        """Проверка формата введенного времени."""
        pattern = r'^(?:[01]?\d|2[0-3]):[0-5]\d$'
        return bool(re.match(pattern, time_string))

    @staticmethod
    async def save_to_db(time_string, uid):
        """Сохранение или обновление записи в бд."""
        response = await async_http_post(
            bot_env.url_api + 'notification/uid/',
            data=TimeNotification.fill_user_data(time_string, uid)
        )
        print(response)
        log.info('Response: %s', response)
        return response

    def fill_user_data(time_string, uid):
        return {
            'user': uid,
            'platform': 'vk',
            'days_of_week': '0',
            'time': time_string
        }

