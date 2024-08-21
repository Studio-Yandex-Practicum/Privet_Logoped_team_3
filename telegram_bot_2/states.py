from aiogram.filters.state import State, StatesGroup


class FSMGift(StatesGroup):
    input_promocode = State()


class FSMInputTime(StatesGroup):
    input_time = State()
