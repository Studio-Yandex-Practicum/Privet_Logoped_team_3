import logging

from api.api_content import ContentApi
from constants import ERROR_MESSAGE
from routers.keyboard import HELP_MENU

log = logging.getLogger(__name__)


class HelpMenu:

    @staticmethod
    async def response(message):
        if message == HELP_MENU[0]:
            return await HelpMenu.help_with_install()
        elif message == HELP_MENU[1]:
            return await HelpMenu.help_with_pc()
        elif message == HELP_MENU[2]:
            return await HelpMenu.help_with_pc()

    @staticmethod
    async def help_with_install():
        content = await ContentApi.get_help_with_install()
        if not content:
            log.error("Content not found for help_with_install")
            return {'text': ERROR_MESSAGE}
        return {'text': content.help_install_file}

    @staticmethod
    async def help_with_pc():
        content = await ContentApi.get_help_with_pc()
        if not content:
            log.error("Content not found for help_with_pc")
            return {'text': ERROR_MESSAGE}
        return {'text': content.present_on_pc}
