import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    bot_token: str = os.getenv('BOT_TOKEN')
    host: str = os.getenv('HOST')
    owner_tg: str = os.getenv('OWNER_TG')


bot_env = Config()
