import logging

from bot_cfg import bot

log = logging.getLogger(__name__)



# @bot.loop_wrapper.interval(seconds=10)
# async def repeated_task():
#     print("I'll print this every 10 seconds!")


# @bot.on.message(text=MAIN_MENU_WORD)   # Обработка сообщений в лс и группе
#
# @bot.on.message(CommandRule(MAIN_MENU_WORD, COMMAND_PREFIXES, 0))   # Обработка сообщений в лс и группе
# async def on_message(message: Message):
#     log.info('Received message: %s', message.text)
#
#     print(message)
#     user = await bot.api.users.get()
#     await message.answer(
#         GREETING_MESSAGE,
#         keyboard=main_keyboard()
#     )


# @bot.on.message()
# async def on_chat_message(message: Message):
#     log.info('Received message: %s', message.text)
#     await message.answer(message.text)


def configure_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        datefmt='%Y-%m-%d %H:%M:%S',
        format='%(asctime)s - %(module)s - %(lineno)d - %(message)s'
    )


if __name__ == '__main__':
    configure_logging()
    log.info('..... S T A R T .....')
    bot.run_forever()
