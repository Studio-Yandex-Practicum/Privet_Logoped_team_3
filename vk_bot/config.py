import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    def __init__(self):
        self.bot_token = os.getenv('BOT_TOKEN')
        self.group_token = os.getenv('GROUP_TOKEN')


bot_env = Config()
