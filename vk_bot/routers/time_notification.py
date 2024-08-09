import re


class TimeNotification:

    @staticmethod
    async def response(message):
        if TimeNotification.test_time_format(message):
            TimeNotification.save_to_db(message)
            return {
                'text': 'Время введено корректно, нужно сохранить в БД'
            }
        return {
            'text': 'Время введено некорректно, действие отменено'
        }

    @staticmethod
    def test_time_format(time_string):
        pattern = r'^(?:[01]\d|2[0-3]):[0-5]\d$'
        return bool(re.match(pattern, time_string))

    @staticmethod
    def save_to_db(time_string):
        pass