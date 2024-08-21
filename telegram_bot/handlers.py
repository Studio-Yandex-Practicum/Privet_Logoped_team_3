import aiohttp
from aiogram import F, Router
from aiogram.filters.state import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import CallbackQuery, Message

import keyboards
from crutches import get_notification
from config import bot_env
from lexicon import lexicon
from states import FSMGift, FSMInputTime

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
    tg_id = message.from_user.id
    notification = await get_notification(tg_id)
    if notification:
        await message.answer(
            text=f'Уведомления включены\n{notification.time}',
            reply_markup=keyboards.exist_notification_kb,
        )
    else:
        await message.answer(
            text='Уведомления выключены',
            reply_markup=keyboards.non_exist_notification_kb,
        )


@router.callback_query(F.data == 'add_notification')
async def add_notification(callback: CallbackQuery, state: FSMContext):
    """Добавление уведомления"""
    await callback.answer()
    await state.set_state(FSMInputTime.input_time)
    await callback.message.answer(
        text=lexicon.messages.input_time,
        reply_markup=keyboards.back_to_main_menu_kb,
    )


@router.callback_query(F.data == 'delete_notification')
async def delete_notification(callback: CallbackQuery):
    """Удаление уведомления"""
    await callback.answer()
    notification = await get_notification(callback.from_user.id)
    if notification:
        async with aiohttp.ClientSession() as session:
            async with session.delete(
                f'{bot_env.host}/api/v1/notification/{notification.id}',
            ) as response:
                if response.status == 204:
                    await callback.message.answer(
                        text='Уведомление отключено',
                    )
    else:
        await callback.message.answer(
            text='Уведомления выключены',
        )


@router.callback_query(F.data == 'edit_notification')
async def edit_notification(callback: CallbackQuery, state: FSMContext):
    """Редактирование уведомления"""
    await callback.answer()
    await state.set_state(FSMInputTime.input_time)
    await callback.message.answer(
        text=lexicon.messages.input_time,
        reply_markup=keyboards.back_to_main_menu_kb,
    )


@router.message(StateFilter(FSMInputTime.input_time))
async def set_time_notification(message: Message, state: FSMContext):
    """Установка времени уведомления"""
    try:
        hours, minutes = message.text.split(':')
    except ValueError:
        await message.answer(
            text='Неверный формат времени :(\nПопробуйте ещё раз',
            reply_markup=keyboards.back_to_main_menu_kb,
        )
    else:
        check_hours = 0 <= int(hours) <= 23
        check_minutes = 0 <= int(minutes) <= 59
        if check_hours and check_minutes:
            notification = await get_notification(message.from_user.id)
            if notification:
                async with aiohttp.ClientSession() as session:
                    async with session.patch(
                        f'{bot_env.host}/api/v1/notification/{notification.id}/',
                        json={'time': f'{hours}:{minutes}'},
                    ) as response:
                        if response.status == 200:
                            await state.set_state(default_state)
                            await message.answer(
                                text='Уведомление обновлено',
                            )
            else:
                async with aiohttp.ClientSession() as session:
                    async with session.get(
                        f'{bot_env.host}/api/v1/profile/uid/{message.from_user.id}',
                    ) as response:
                        if response.status == 200:
                            user = await response.json()
                            user_id = user.get('id')
                            async with session.post(
                                f'{bot_env.host}/api/v1/notification/',
                                json={
                                    'time': f'{hours}:{minutes}',
                                    'days_of_week': '0',
                                    'user_id': user_id,
                                    'platform': 'tg',
                                },
                            ) as response:
                                if response.status == 201:
                                    await state.set_state(default_state)
                                    await message.answer(
                                        text='Уведомление установлено',
                                    )
        else:
            await message.answer(
                text='Неверный формат времени :(\nПопробуйте ещё раз',
                reply_markup=keyboards.back_to_main_menu_kb,
            )


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
