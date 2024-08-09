import aiohttp
import keyboards
from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from config import bot_env
from lexicon import lexicon

router = Router()


@router.message(F.text == lexicon.buttons.logoped)
async def role_logoped(message: Message):
    data = {
        'username': message.from_user.username,
        'user_id': message.from_user.id,
        'role': 'speech_therapist',
        'platform': 'tg',
    }
    await message.answer(
        text=lexicon.messages.role_logoped,
        reply_markup=keyboards.main_kb,
    )
    async with aiohttp.ClientSession() as session:
        await session.post(
            f'{bot_env.host}/api/v1/profile/uid/',
            json=data,
        )


@router.message(F.text == lexicon.buttons.parent)
async def role_parent(message: Message):
    data = {
        'username': message.from_user.username,
        'user_id': message.from_user.id,
        'role': 'parent',
        'platform': 'tg',
    }
    await message.answer(
        text=lexicon.messages.role_parent,
        reply_markup=keyboards.main_kb,
    )
    async with aiohttp.ClientSession() as session:
        await session.post(
            f'{bot_env.host}/api/v1/profile/uid/',
            json=data,
        )


@router.message(F.text == lexicon.buttons.usefull_video)
async def take_usefull_video(message: Message):
    await message.answer('Тут будет ссылка на полезное видео')


@router.message(F.text == lexicon.buttons.track_results)
async def take_track_results(message: Message):
    await message.answer('Тут будет файл бланка')


@router.message(F.text == lexicon.buttons.payment)
async def help_with_payment(message: Message):
    await message.answer('Тут будет помощь с оплатой')


@router.message(F.text == lexicon.buttons.notifications)
async def set_notifications(message: Message):
    await message.answer('Как я понимаю настройки уведомлений')


@router.message(F.text == lexicon.buttons.gift)
async def take_gift(message: Message):
    await message.answer('Тут нужно будет ввести промокод?')


@router.message(F.text == lexicon.buttons.help)
async def take_help(message: Message):
    await message.answer('Какая-то помощь с приложением')


@router.message(F.text == lexicon.buttons.contact_logoped)
async def confirmation_contact(message: Message):
    await message.answer(
        text=lexicon.messages.confirmation_contact,
        reply_markup=keyboards.confirmation_contact_kb,
    )


@router.callback_query(F.data == 'main_menu')
async def callback_main_menu(callback: CallbackQuery):
    await callback.answer()
    await callback.message.delete()
    await callback.message.answer(
        text=lexicon.messages.menu,
        reply_markup=keyboards.main_kb,
    )
