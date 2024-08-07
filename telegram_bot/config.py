import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    bot_token: str = os.getenv('BOT_TOKEN')
    host: str = os.getenv('HOST')


bot_env = Config()
