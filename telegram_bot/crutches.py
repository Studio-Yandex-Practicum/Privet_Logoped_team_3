import aiohttp

from collections import namedtuple

from config import bot_env

Notification = namedtuple('Notification', ['id', 'time'])


async def get_notification(uid: str) -> Notification:
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f'{bot_env.host}/api/v1/profile/uid/{uid}/'
        ) as response:
            if response.status == 200:
                user = await response.json()
                user_id = user.get('id')
                async with session.get(
                    f'{bot_env.host}/api/v1/notification/'
                ) as response:
                    if response.status == 200:
                        notifications = await response.json()
                        for notification in notifications:
                            if notification.get('user_id') == user_id:
                                return Notification(
                                    id=notification.get('id'),
                                    time=notification.get('time'),
                                )
