import logging

import bot_cfg
from api.api_notification import NotificationApi

log = logging.getLogger(__name__)


async def periodicaly_notification_job():
    if not bot_cfg.notification.make_notification():
        return None

    log.info('Periodicaly notification job at: %s', bot_cfg.notification.get_time_to_notify())
    print(f'periodicaly_notification_job at {bot_cfg.notification.get_time_to_notify()}')
    contents = await NotificationApi.get_notification_by_time(
        bot_cfg.notification.get_time_to_notify()
    )
    if not contents:
        return None
    #     await bot.send_message(content.chat_id, content.text)
    #     log.info(f'Send notification to chat_id: {content.chat_id}, text: {content.text}')

    # for alert in contents.notifications:
    #     print(f'{alert.time} {alert.user_id}')
    peer_ids = [alert.user_id for alert in contents.notifications]
    # print(peer_ids)
    if not peer_ids:
        return None

    await bot_cfg.bot.api.messages.send(
        # peer_id=792239065,
        # peer_ids=[792239065],
        peer_ids=peer_ids,
        random_id=0,
        message='Event Message'
    )
