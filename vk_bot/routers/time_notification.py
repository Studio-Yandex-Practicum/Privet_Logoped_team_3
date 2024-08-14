import re

TIME_NOTIFICATION_CORRECT = 'Время введено корректно, нужно сохранить в БД'
TIME_NOTIFICATION_INCORRECT = 'Время введено некорректно, действие отменено'


class TimeNotification:

    @staticmethod
    async def response(time_string, uid):
        if TimeNotification.test_time_format(time_string):
            TimeNotification.save_to_db(time_string, uid)
            return {
                'text': TIME_NOTIFICATION_CORRECT
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
    def save_to_db(time_string, uid):
        """Сохранение или обновление записи в бд."""
