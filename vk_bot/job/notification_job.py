import logging

import bot_cfg
from api.api_notification import NotificationApi
from constants import EVENT_MESSAGE

log = logging.getLogger(__name__)


async def periodicaly_notification_job():
    if not bot_cfg.notification.make_notification():
        return None

    log.info(
        'Periodicaly notification job at: %s',
        bot_cfg.notification.get_time_to_notify()
    )
    print('periodicaly_notification_job at '
          f'{bot_cfg.notification.get_time_to_notify()}')
    contents = await NotificationApi.get_notification_by_time(
        bot_cfg.notification.get_time_to_notify()
    )
    if not contents:
        return None

    peer_ids = [alert.uid for alert in contents.notifications]
    if not peer_ids:
        return None

    await bot_cfg.bot.api.messages.send(
        peer_ids=peer_ids,
        random_id=0,
        message=EVENT_MESSAGE
    )
