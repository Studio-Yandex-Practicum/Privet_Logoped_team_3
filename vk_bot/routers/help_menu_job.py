from routers.keyboard import HELP_MENU


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
        return {
            'text': 'help_with_install в процессе реализации'
        }

    @staticmethod
    async def help_with_pc():
        return {
            'text': 'help_with_pc в процессе реализации'
        }
