import logging

from bot_cfg import bot

log = logging.getLogger(__name__)


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
