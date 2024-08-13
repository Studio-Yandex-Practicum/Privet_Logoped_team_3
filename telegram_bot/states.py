from aiogram.filters.state import State, StatesGroup


class FSMGift(StatesGroup):
    input_promocode = State()
