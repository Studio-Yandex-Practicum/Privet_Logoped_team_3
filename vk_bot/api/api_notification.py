import json
from http import HTTPStatus

from api.schemas import Notifications, Notification
from api.utils import async_http_get
from config import bot_env
from constants import NOTIFICATION_PATH


class NotificationApi:

    @staticmethod
    async def get_notification_by_time(time):
        """Загрузить периодические уведомления для указанного времени."""
        # print(time)
        response = await async_http_get(
            bot_env.url_api + f'{NOTIFICATION_PATH}{time}'
        )
        if response['status'] == HTTPStatus.OK:
            response_json = json.loads(response['text'])
            notifications = Notifications(
                notifications=[Notification(**item) for item in response_json]
            )
            print(notifications)
        else:
            notifications = None
        return notifications
