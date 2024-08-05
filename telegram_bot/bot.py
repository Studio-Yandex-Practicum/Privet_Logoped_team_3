import keyboards

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

from config import bot_env

load_dotenv('.env')


bot = Bot(bot_env.bot_token)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        (
            'Добро пожаловать в бота "Привет, Логопед!".\n'
            'Давайте познакомимся, выберите свою роль:'
        ),
        reply_markup=keyboards.role_kb
    )


@dp.message(Command("menu"))
async def menu(message: Message):
    await message.answer(
        (
            'Вот с чем я могу Вам помочь:'
        ),
        reply_markup=keyboards.main_kb
    )


@dp.message()
async def role(message: Message):
    msg = message.text.lower()

    if msg in ["родитель", "логопед"]:
        await menu(message)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
