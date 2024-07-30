import logging

from vkbottle.bot import BotLabeler, Message
from vkbottle.dispatch.rules.base import CommandRule

from constants import MAIN_MENU_WORD, GREETING_MESSAGE, COMMAND_PREFIXES
from routers.keyboard import main_keyboard


log = logging.getLogger(__name__)

bl = BotLabeler()


@bl.private_message(CommandRule(MAIN_MENU_WORD, COMMAND_PREFIXES, 0))
async def main_menu(message: Message):
    log.info('Received command: %s in %s', MAIN_MENU_WORD, message.text)
    print(message)
    await message.answer(
        GREETING_MESSAGE,
        keyboard=main_keyboard()
    )
