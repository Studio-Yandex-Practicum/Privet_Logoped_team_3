from datetime import datetime

from vkbottle import Bot, LoopWrapper

from config import bot_env
from constants import LOOPWRAPPER_INTERVAL
from routers import labelers
from routers.notification_job import periodicaly_notification_job

bot = Bot(token=bot_env.group_token)


for custom_labeler in labelers:
    bot.labeler.load(custom_labeler)


class Notification:
    def __init__(self):
        self.last_notification = self.current_time()

    def current_time(self):
        return datetime.now().strftime('%H:%M')

    def get_time_to_notify(self):
        return self.last_notification

    def make_notification(self):
        current_time = self.current_time()
        if self.last_notification != current_time:
            self.last_notification = current_time
            return True
        return False


notification = Notification()

lw = LoopWrapper()


@lw.interval(seconds=LOOPWRAPPER_INTERVAL)
async def repeated_task():
    await periodicaly_notification_job()

lw.run_forever()



