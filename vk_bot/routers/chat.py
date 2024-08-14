import logging

from vkbottle.bot import BotLabeler, Message

log = logging.getLogger(__name__)

bl = BotLabeler()


# @bl.private_message()
# async def on_chat_message(message: Message):
#     log.info('Received message: %s', message.text)
#     await message.answer(message.text)
