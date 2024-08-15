import json
import logging
from http import HTTPStatus

import bot_cfg
from api.schemas import Notifications, Notification
from api.utils import async_http_get
from config import bot_env
from constants import NOTIFICATION_PATH

log = logging.getLogger(__name__)

async def periodicaly_notification_job():
    if bot_cfg.notification.make_notification():
        log.info('Periodicaly notification job at: %s', bot_cfg.notification.get_time_to_notify())
        print(f'periodicaly_notification_job at {bot_cfg.notification.get_time_to_notify()}')
        contents = await UserNotification._get_content(
            bot_cfg.notification.get_time_to_notify()
        )
        if contents:
        #     await bot.send_message(content.chat_id, content.text)
        #     log.info(f'Send notification to chat_id: {content.chat_id}, text: {content.text}')
            peer_ids = [alert.user_id for alert in contents.notifications]
            print(peer_ids)
            # for alert in contents.notifications:
            #     print(f'{alert.time} {alert.user_id}')
            if peer_ids:
                await bot_cfg.bot.api.messages.send(
                    # peer_id=792239065,
                    # peer_ids=[792239065],
                    peer_ids=peer_ids,
                    random_id=0,
                    message='Event Message'
                )


class UserNotification:

    @staticmethod
    async def _get_content(time):
        # print(time)
        time = '11:40'
        response = await async_http_get(
            bot_env.url_api + f'{NOTIFICATION_PATH}{time}'
        )
        if response['status'] == HTTPStatus.OK:
            response_json = json.loads(response['text'])
            contents = Notifications(notifications=[Notification(**item) for item in response_json])
        else:
            contents = None
        return contents
