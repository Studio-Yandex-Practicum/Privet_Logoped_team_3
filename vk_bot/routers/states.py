from vkbottle import BaseStateGroup


class States(BaseStateGroup):
    waiting_for_code = 1


class TimeStates(BaseStateGroup):
    waiting_for_time = 1
