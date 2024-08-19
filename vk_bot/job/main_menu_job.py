import logging

import bot_cfg
from api.api_content import ContentApi
from constants import ERROR_MESSAGE
from routers.keyboard import (
    HELP_MENU, MAIN_MENU, make_keyboard_menu, PAYMENT_MENU
)
from routers.states import States, TimeStates

log = logging.getLogger(__name__)


SECRET_WORD = 'Введите секретное слово:'
GET_VIDEO = 'Рекомендуем посмотреть это видео: '
GET_RESULT = ('У меня для Вас есть специальный файлик, который поможет вам '
              'следить за прогрессом ребенка:')
GET_HELP = 'Вот чем я могу Вам помочь:'
GET_NOTIFICATION = 'Введите время получения уведомления в формате ЧЧ:ММ'


class MainMenu:

    @staticmethod
    async def response(message, message_base):
        if message == MAIN_MENU[0]:
            return await MainMenu.get_video()
        elif message == MAIN_MENU[1]:
            return await MainMenu.get_result()
        elif message == MAIN_MENU[2]:
            return await MainMenu.get_payment('Меню оплаты:')
        elif message == MAIN_MENU[3]:
            return await MainMenu.get_notification(message_base)
        elif message == MAIN_MENU[4]:
            return await MainMenu.get_present(message_base)
        elif message == MAIN_MENU[5]:
            return await MainMenu.get_app_help()

    @staticmethod
    async def get_video():
        content = await ContentApi.get_video()
        if not content:
            log.error("Content not found for get_video")
            return {'text': ERROR_MESSAGE}
        return {
            'text': GET_VIDEO + content.url_gift
        }

    @staticmethod
    async def get_payment(text):
        return {
            'text': text,
            'keyboard': make_keyboard_menu(PAYMENT_MENU)
        }

    @staticmethod
    async def get_notification(message_base):
        await bot_cfg.bot.state_dispenser.set(
            message_base.peer_id,
            TimeStates.waiting_for_time
        )
        return {
            'text': GET_NOTIFICATION
        }

    @staticmethod
    async def get_present(message_base):
        await bot_cfg.bot.state_dispenser.set(
            message_base.peer_id,
            States.waiting_for_code
        )
        return {
            'text': SECRET_WORD
        }

    @staticmethod
    async def get_result():
        content = await ContentApi.get_result()
        if not content:
            log.error("Content not found for get_result")
            return {'text': ERROR_MESSAGE}
        return {
            'text': GET_RESULT + content.track_file
        }

    @staticmethod
    async def get_app_help():
        return {
            'text': GET_HELP,
            'keyboard': make_keyboard_menu(HELP_MENU)
        }
