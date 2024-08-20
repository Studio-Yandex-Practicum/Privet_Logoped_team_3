import aiohttp
import asyncio
from datetime import datetime, UTC

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message

from handlers import router

import keyboards
from config import bot_env
from lexicon import lexicon

bot = Bot(bot_env.bot_token)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
dp.include_router(router)


async def notify_users():
    utc_time = datetime.now(UTC)
    utc_time = f'{utc_time.hour}:{utc_time.minute}'
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f'{bot_env.host}/api/v1/notification/tg/?time={utc_time}'
        ) as response:
            if response.status == 200:
                date = await response.json()
                if not date:
                    return
                for user in date:
                    user_uid = user.get('uid')
                    await bot.send_message(user_uid, lexicon.messages.notification)


async def notify_users_job():
    while True:
        await notify_users()
        await asyncio.sleep(60)


@dp.message(Command('start'))
async def start(message: Message):
    await message.answer(
        text=lexicon.messages.start,
        reply_markup=keyboards.role_kb,
    )


@dp.message(Command('menu'))
async def menu(message: Message):
    await message.answer(
        text=lexicon.messages.menu,
        reply_markup=keyboards.main_kb,
    )


async def main():
    notification_job = asyncio.create_task(notify_users_job())
    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    finally:
        notification_job.cancel()
