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


async def fetch_data_from_api(
    endpoint: str,
    message: Message = None,
    callback: CallbackQuery = None
):
    """Функция для получения данных из API"""
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f'{bot_env.host}/api/v1/{endpoint}'
        ) as response:
            if response.status == 200:
                data = await response.json()
                return data[0]
            else:
                return None


async def message_api_response(data_key, message: Message):
    """Обработка ответа от API и отправка сообщения пользователю"""
    data = await fetch_data_from_api('content/')
    if data:
        if data.get(data_key):
            await message.answer(data.get(data_key))
        else:
            await message.answer('Ссылка еще готовится :(')
    else:
        await message.answer('Ссылка еще готовится :(')


async def callback_api_response(data_key, callback: CallbackQuery):
    """Обработка ответа от API и отправка сообщения пользователю"""
    data = await fetch_data_from_api('content/')
    if data:
        if data.get(data_key):
            await callback.message.answer(data.get(data_key))
        else:
            await callback.message.answer('Ссылка еще готовится :(')
    else:
        await callback.message.answer('Ссылка еще готовится :(')


async def handle_role_selection(
        message: Message,
        role: str,
        response_text: str
):
    """Обработка выбора роли и отправка данных в API"""
    data = {
        'username': message.from_user.username,
        'user_id': message.from_user.id,
        'role': role,
        'platform': 'tg',
    }
    await message.answer(
        text=response_text,
        reply_markup=keyboards.main_kb,
    )
    async with aiohttp.ClientSession() as session:
        await session.post(
            f'{bot_env.host}/api/v1/profile/uid/',
            json=data,
        )


@router.message(F.text == lexicon.buttons.logoped)
async def role_logoped(message: Message):
    """Выбор роли логопеда"""
    await handle_role_selection(
        message,
        role='speech_therapist',
        response_text=lexicon.messages.role_logoped
    )


@router.message(F.text == lexicon.buttons.parent)
async def role_parent(message: Message):
    """Выбор роли родителя"""
    await handle_role_selection(
        message,
        role='parent',
        response_text=lexicon.messages.role_parent
    )


@router.message(F.text == lexicon.buttons.usefull_video)
async def take_usefull_video(message: Message):
    """Полезная ссылка"""
    await message_api_response('usefull_url', message)


@router.message(F.text == lexicon.buttons.track_results)
async def take_track_results(message: Message):
    """Отследить результат"""
    await message_api_response('track_file', message)


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
    await callback_api_response('payment_url', callback)


@router.callback_query(F.data == 'pay_ios_version')
async def pay_ios_version(callback: CallbackQuery):
    """Оплата iOS версии"""
    await callback.answer()
    await callback_api_response('ios_payment', callback)


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
    await message_api_response('code_gift', message)
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
    """Помощь с установкой"""
    await callback.answer()
    await callback_api_response('help_install_file', callback)


@router.callback_query(F.data == 'present_on_pc')
async def present_on_pc(callback: CallbackQuery):
    """Как вывести на ПК"""
    await callback.answer()
    await callback_api_response('present_on_pc', callback)


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
