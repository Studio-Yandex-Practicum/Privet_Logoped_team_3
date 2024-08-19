import aiohttp

from aiogram import F, Router
from aiogram.filters.state import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import CallbackQuery, Message

import keyboards
from config import bot_env
from lexicon import lexicon
from states import FSMGift

router = Router()


@router.message(F.text == lexicon.buttons.logoped)
async def role_logoped(message: Message):
    """Выбор роли логопеда"""
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
    """Выбор роли родителя"""
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
    """Полезная ссылка"""
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f'{bot_env.host}/api/v1/content/'
        ) as response:
            if response.status == 200:
                data = await response.json()
                data = data[0]
                if data.get('usefull_url'):
                    await message.answer(data.get('usefull_url'))
                else:
                    await message.answer('Ссылка еще готовится :(')
            else:
                await message.answer('Ссылка еще готовится :(')


@router.message(F.text == lexicon.buttons.track_results)
async def take_track_results(message: Message):
    """Отследить результат"""
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f'{bot_env.host}/api/v1/content/'
        ) as response:
            if response.status == 200:
                data = await response.json()
                data = data[0]
                if data.get('track_file'):
                    await message.answer(data.get('track_file'))
                else:
                    await message.answer('Ссылка еще готовится :(')
            else:
                await message.answer('Ссылка еще готовится :(')


@router.message(F.text == lexicon.buttons.payment)
async def help_with_payment(message: Message):
    """Переход в меню оплаты"""
    await message.answer(
        text=lexicon.messages.payment_menu,
        reply_markup=keyboards.payment_kb,
    )


@router.callback_query(F.data == 'pay_full_version')
async def pay_full_version(callback: CallbackQuery):
    """Оплата полной версии"""
    await callback.answer()
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f'{bot_env.host}/api/v1/content/'
        ) as response:
            if response.status == 200:
                data = await response.json()
                data = data[0]
                if data.get('payment_url'):
                    await callback.message.answer(data.get('payment_url'))
                else:
                    await callback.message.answer('Ссылка еще готовится :(')
            else:
                await callback.message.answer('Ссылка еще готовится :(')


@router.callback_query(F.data == 'pay_ios_version')
async def pay_ios_version(callback: CallbackQuery):
    """Оплата iOS версии"""
    await callback.answer()
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f'{bot_env.host}/api/v1/content/'
        ) as response:
            if response.status == 200:
                data = await response.json()
                data = data[0]
                if data.get('ios_payment'):
                    await callback.message.answer(data.get('ios_payment'))
                else:
                    await callback.message.answer('Ссылка еще готовится :(')
            else:
                await callback.message.answer('Ссылка еще готовится :(')



@router.message(F.text == lexicon.buttons.notifications)
async def set_notifications(message: Message):
    """Настройка уведомлений"""
    await message.answer('Как я понимаю настройки уведомлений')


@router.message(F.text == lexicon.buttons.gift)
async def take_gift(message: Message, state: FSMContext):
    """Меню промокода"""
    await message.answer(
        text=lexicon.messages.input_promocode,
        reply_markup=keyboards.back_to_main_menu_kb,
    )
    await state.set_state(FSMGift.input_promocode)


@router.message(StateFilter(FSMGift.input_promocode))
async def take_promocode(message: Message, state: FSMContext):
    """Выдача подарка по промокоду"""
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f'{bot_env.host}/api/v1/content/'
        ) as response:
            if response.status == 200:
                data = await response.json()
                data = data[0]
                print(data)
                if message.text == data.get('code_gift'):
                    await message.answer(data.get('url_gift'))
                else:
                    await message.answer('Неверный промокод :(')
            else:
                await message.answer('Ссылка еще готовится :(')
    await state.set_state(default_state)


@router.message(F.text == lexicon.buttons.help)
async def take_help(message: Message):
    """Переход в меню помощи"""
    await message.answer(
        text=lexicon.messages.help_menu,
        reply_markup=keyboards.help_menu_kb
    )


@router.callback_query(F.data == 'install_help')
async def install_help(callback: CallbackQuery):
    """Меню помощи с установкой"""
    await callback.answer()
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f'{bot_env.host}/api/v1/content/'
        ) as response:
            if response.status == 200:
                data = await response.json()
                data = data[0]
                if data.get('help_install_file'):
                    await callback.message.answer(data.get('help_install_file'))
                else:
                    await callback.message.answer('Ссылка еще готовится :(')
            else:
                await callback.message.answer('Ссылка еще готовится :(')


@router.callback_query(F.data == 'present_on_pc')
async def present_on_pc(callback: CallbackQuery):
    """Меню вывода на ПК"""
    await callback.answer()
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f'{bot_env.host}/api/v1/content/'
        ) as response:
            if response.status == 200:
                data = await response.json()
                data = data[0]
                if data.get('present_on_pc'):
                    await callback.message.answer(data.get('present_on_pc'))
                else:
                    await callback.message.answer('Ссылка еще готовится :(')
            else:
                await callback.message.answer('Ссылка еще готовится :(')


@router.message(F.text == lexicon.buttons.contact_logoped)
async def confirmation_contact(message: Message):
    """Меню подтверждения контакта"""
    await message.answer(
        text=lexicon.messages.confirmation_contact,
        reply_markup=keyboards.confirmation_contact_kb,
    )


@router.callback_query(F.data == 'main_menu')
async def callback_main_menu(callback: CallbackQuery):
    """Главное меню после выбора на inline-клавиатуре"""
    await callback.answer()
    await callback.message.delete()
    await callback.message.answer(
        text=lexicon.messages.menu,
        reply_markup=keyboards.main_kb,
    )
