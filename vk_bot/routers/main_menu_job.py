class MainMenu:

    @staticmethod
    async def response(message):
        if message == 'Полезное видео':
            return await MainMenu.get_video()
        elif message == 'Отследить результаты':
            return await MainMenu.get_result()
        elif message == 'Оплата':
            return await MainMenu.get_payment()
        elif message == 'Помощь с приложением':
            return await MainMenu.get_app_help()

    @staticmethod
    async def get_video():
        return 'Получение видео в процессе реализации'

    @staticmethod
    async def get_payment():
        return 'get_result в процессе реализации'

    @staticmethod
    async def get_result():
        return 'get_result в процессе реализации'

    @staticmethod
    async def get_app_help():
        return 'get_app_help в процессе реализации'
