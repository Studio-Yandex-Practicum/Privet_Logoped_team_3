import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

import keyboard

bot = Bot(
    "7436763245:AAE8FHxQVuuPcpNSEtuQcQ-D1EiPY6OdGAg",
)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        (
            'Добро пожаловать в бота "Привет, Логопед!".\n'
            'Давайте познакомимся, выберите свою роль:'
        ),
        reply_markup=keyboard.main_kb
    )


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
