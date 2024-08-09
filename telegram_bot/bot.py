from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from handlers import router
from config import bot_env
from lexicon import lexicon
import keyboards

bot = Bot(bot_env.bot_token)
dp = Dispatcher()
dp.include_router(router)


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
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
