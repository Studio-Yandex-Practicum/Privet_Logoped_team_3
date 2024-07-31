import logging

from vkbottle.bot import BotLabeler, Message
from vkbottle.dispatch.rules.base import CommandRule

from api.api import send_id
from constants import (GREETING_MESSAGE, COMMAND_PREFIXES,
    ROLE_MESSAGE, START_MENU_CMD)
from routers.keyboard import main_keyboard, ROLE_MENU, start_keyboard

log = logging.getLogger(__name__)

bl = BotLabeler()


@bl.private_message(CommandRule(START_MENU_CMD, COMMAND_PREFIXES, 0))
async def role_menu(message: Message):
    """Вабор роли Родитель/Логопед"""
    log.info('Received command: %s in %s', START_MENU_CMD, message.text)
    print("Вабор роли Родитель/Логопед")
    await message.answer(
        ROLE_MESSAGE,
        keyboard=start_keyboard()
    )


@bl.private_message(text=ROLE_MENU)
async def sub_role_menu(message: Message):
    """Установка роли для id Родитель/Логопед"""
    log.info('Received role command: %s', message.text)
    await send_id(message.from_id)
    print(message.from_id)
    print("Установка роли для id Родитель/Логопед")
    await message.answer(
        GREETING_MESSAGE,
        keyboard=main_keyboard()
    )


@bl.private_message(CommandRule(GREETING_MESSAGE, COMMAND_PREFIXES, 0))
async def main_menu(message: Message):
    """Главное меню."""
    print("Главное меню.")
    log.info('Received command: %s in %s', GREETING_MESSAGE, message.text)
    print(message)
    await message.answer(
        GREETING_MESSAGE,
        keyboard=main_keyboard()
        )
