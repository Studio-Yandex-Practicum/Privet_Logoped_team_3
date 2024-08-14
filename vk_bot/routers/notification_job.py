import json
import logging
from datetime import datetime
from http import HTTPStatus

from api.schemas import Notifications
from api.utils import async_http_get
import bot_cfg
from config import bot_env

log = logging.getLogger(__name__)

async def periodicaly_notification_job():
    if bot_cfg.notification.make_notification():
        log.info('Periodicaly notification job at: %s', bot_cfg.notification.get_time_to_notify())
        print(f'periodicaly_notification_job at {bot_cfg.notification.get_time_to_notify()}')
        # content = await UserNotification._get_content(
        #     bot_cfg.notification.get_time_to_notify()
        # )
        # if content:
        #     await bot.send_message(content.chat_id, content.text)
        #     log.info(f'Send notification to chat_id: {content.chat_id}, text: {content.text}')


class UserNotification:

    @staticmethod
    async def _get_content(time):
        response = await async_http_get(
            bot_env.url_api + f'notification/vk/?time={time}'
        )
        if response['status'] == HTTPStatus.OK:
            contents = json.loads(response['text'])
            content = Notifications.parse_obj(contents[0])
        else:
            content = None
        return content
