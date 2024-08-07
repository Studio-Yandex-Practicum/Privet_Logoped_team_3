import aiofiles
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

import keyboards


router = Router()


@router.message(F.text == 'Логопед')
async def role_logoped(message: Message):
    """Обработчик для логопеда."""
    async with aiofiles.open('logoped_id.txt', 'a') as file:
        await file.write(f'{message.from_user.id}\n')
    await message.answer(
        'Вы вошли как логопед.\n'
        'Вот с чем я могу Вам помочь:',
        reply_markup=keyboards.main_kb,
    )
    # Логика сохраниения или изменения пользователя в базе данных


@router.message(F.text == 'Родитель')
async def role_parent(message: Message):
    """Обработчик для родителя."""
    async with aiofiles.open('parent_id.txt', 'a') as file:
        await file.write(f'{message.from_user.id}\n')
    await message.answer(
        'Вы вошли как родитель.\n'
        'Вот с чем я могу Вам помочь:',
        reply_markup=keyboards.main_kb,
    )
    # Логика сохраниения или изменения пользователя в базе данных


@router.message(F.text == 'Полезное видео')
async def take_useful_video(message: Message):
    """Обработчик для кнопки "Полезное видео"."""
    await message.answer('Видео с полезной информацией')


@router.message(F.text == 'Отследить результаты')
async def take_track_results(message: Message):
    """Обработчик для кнопки "Отследить результаты"."""
    await message.answer('Отследить результаты')


@router.message(F.text == 'Оплата')
async def help_with_payment(message: Message):
    """Обработчик для кнопки "Оплата"."""
    await message.answer('Оплата')


@router.message(F.text == 'Уведомления')
async def set_notifications(message: Message):
    """Обработчик для кнопки "Уведомления"."""
    await message.answer('Уведомления')


@router.message(F.text == 'Подарок')
async def take_gift(message: Message):
    """Обработчик для кнопки "Подарок"."""
    await message.answer('Подарок')


@router.message(F.text == 'Помощь с приложением')
async def take_help(message: Message):
    """Обработчик для кнопки "Помощь с приложением"."""
    await message.answer('Помощь с приложением')


@router.message(F.text == 'Связаться с логопедом')
async def contact_logoped(message: Message):
    """Обработчик для кнопки "Связаться с логопедом"."""
    await message.answer(
        'Связаться с логопедом?',
        reply_markup=keyboards.confirmation_contact_kb,
    )


@router.callback_query(F.data == 'main_menu')
async def callback_main_menu(callback: CallbackQuery):
    """Обработчик для кнопки "Нет"."""
    await callback.answer()
    await callback.message.delete()
    await callback.message.answer(
        'Вот с чем я могу Вам помочь:',
        reply_markup=keyboards.main_kb,
    )
