from vkbottle import Bot

from config import bot_env
from routers import labelers

bot = Bot(token=bot_env.group_token)

for custom_labeler in labelers:
    bot.labeler.load(custom_labeler)
