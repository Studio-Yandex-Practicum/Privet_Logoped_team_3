import logging

from vkbottle.bot import BotLabeler, Message
from vkbottle.dispatch.rules.base import CommandRule

from api.api import Roles
import bot_cfg
from constants import (
    GREETING_MESSAGE, COMMAND_PREFIXES, ROLE_MESSAGE, START_MENU_CMD
)
from routers.keyboard import (
    main_keyboard, MAIN_MENU, ROLE_MENU, start_keyboard
)
from routers.main_menu_job import MainMenu

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
    user = await bot_cfg.bot.api.users.get(message.from_id)
    await Roles.send_role_for_id(
        message.from_id,
        message.text,
        f'{user[0].first_name} {user[0].last_name}'
    )
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


@bl.private_message(text=MAIN_MENU)
async def sub_role_menu(message: Message):
    """Установка роли для id Родитель/Логопед"""
    log.info('Main menu command: %s', message.text)
    print(message.from_id)
    if message.text not in ('Уведомления','Подарок',):
        response_message = await MainMenu.response(message.text)
        await message.answer(response_message)

    #
    # await message.answer(
    #     GREETING_MESSAGE,
    #     keyboard=main_keyboard()
    # )
