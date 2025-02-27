import logging

from vkbottle.bot import BotLabeler, Message
from vkbottle.dispatch.rules.base import CommandRule, ChatActionRule

import bot_cfg
from api.api import Roles
from constants import (COMMAND_PREFIXES, GREETING_MESSAGE, ROLE_MESSAGE,
                       START_MENU_CMD, MAIN_MENU_CMD, INVITE_MESSAGE)
from job.help_menu_job import HelpMenu
from job.main_menu_job import MainMenu
from job.payment_job import PaymentMenu
from job.secret_word_job import SecretWord
from routers.keyboard import (
    HELP_MENU, MAIN_MENU, MAIN_MENU_COMMAND, make_keyboard_menu,
    PAYMENT_MENU, ROLE_MENU,
)
from routers.states import States, TimeStates
from routers.time_notification import TimeNotification

log = logging.getLogger(__name__)

bl = BotLabeler()


@bl.private_message(CommandRule(START_MENU_CMD, COMMAND_PREFIXES, 0))
async def role_menu(message: Message):
    """Вабор роли Родитель/Логопед"""
    log.info('Received command: %s in %s', START_MENU_CMD, message.text)
    print("Вабор роли Родитель/Логопед")
    await message.answer(
        ROLE_MESSAGE,
        keyboard=make_keyboard_menu(ROLE_MENU)
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
        keyboard=make_keyboard_menu(MAIN_MENU)
    )


@bl.private_message(CommandRule(GREETING_MESSAGE, COMMAND_PREFIXES, 0))
async def main_menu(message: Message):
    """Главное меню."""
    log.info('Received command: %s in %s', GREETING_MESSAGE, message.text)
    if not Roles.check_user_registered(message.peer_id):
        log.info('Role not found')
        print("Выбор роли Родитель/Логопед")
        await message.answer(
            ROLE_MESSAGE,
            keyboard=make_keyboard_menu(ROLE_MENU)
        )
    else:
        await message.answer(
            GREETING_MESSAGE,
            keyboard=make_keyboard_menu(MAIN_MENU)
            )


@bl.private_message(text=MAIN_MENU)
async def sub_role_menu(message: Message):
    """Установка роли для id Родитель/Логопед"""
    log.info('Main menu command: %s', message.text)
    print(message.from_id)
    response_message = await MainMenu.response(message.text, message)
    await message.answer(
        response_message['text'],
        keyboard=response_message.get('keyboard'))


@bl.private_message(text=(MAIN_MENU_COMMAND,MAIN_MENU_CMD))
async def show_main_menu(message: Message):
    """Переключение в главное меню."""
    if not await Roles.check_user_registered(message.peer_id):
        log.info('Role not found')
        print("Выбор роли Родитель/Логопед")
        await message.answer(
            ROLE_MESSAGE,
            keyboard=make_keyboard_menu(ROLE_MENU)
        )
    else:
        log.info('Received switch to main menu command: %s', message.text)
        await message.answer(
            MAIN_MENU_COMMAND,
            keyboard=make_keyboard_menu(MAIN_MENU)
        )


@bl.private_message(text=HELP_MENU)
async def show_main_menu(message: Message):
    """Обработка команд HELP_MENU."""
    log.info('Received HELP_MENU command: %s', message.text)
    response_message = await HelpMenu.response(message.text)
    await message.answer(
        response_message['text'],
        keyboard=response_message.get('keyboard'))


@bl.private_message(state=States.waiting_for_code)
async def secret_word_handler(message: Message):
    """Обработка проверки секретного слова."""
    log.info('Check gift keyword: %s', message.text)
    await bot_cfg.bot.state_dispenser.delete(message.peer_id)
    response = await SecretWord.check(message.text)
    await message.answer(
        response['text'],
    )


@bl.private_message(state=TimeStates.waiting_for_time)
async def time_notification_handler(message: Message):
    """Обработка проверки времени уведомления."""
    log.info('Check time notificatiob: %s', message.text)
    await bot_cfg.bot.state_dispenser.delete(message.peer_id)
    response = await TimeNotification.response(message.text, message.peer_id)
    await message.answer(
        response['text'],
    )


@bl.private_message(text=PAYMENT_MENU)
async def show_payment_menu(message: Message):
    """Обработка команд PAYMENT_MENU."""
    log.info('Received PAYMENT_MENU command: %s', message.text)
    response_message = await PaymentMenu.response(message.text)
    await message.answer(
        response_message['text'],
    )


@bl.private_message(ChatActionRule('chat_invite_user'))
async def wrapper(message: Message):
    await message.answer(
        INVITE_MESSAGE,
    )
