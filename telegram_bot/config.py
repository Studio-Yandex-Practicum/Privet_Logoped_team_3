import os


class Config:

    def __init__(self):
        self.bot_token = os.getenv('BOT_TOKEN')


bot_env = Config()
