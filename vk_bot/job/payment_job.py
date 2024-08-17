import logging

from api.api_content import ContentApi
from constants import ERROR_MESSAGE
from routers.keyboard import PAYMENT_MENU

log = logging.getLogger(__name__)


class PaymentMenu:

    @staticmethod
    async def response(message):
        if message == PAYMENT_MENU[0]:
            return await PaymentMenu.pay_full_version()
        elif message == PAYMENT_MENU[1]:
            return await PaymentMenu.pay_ios_version()

    @staticmethod
    async def pay_full_version():
        content = await ContentApi.get_pay_full_version()
        if not content:
            log.error("Content not found for help_with_install")
            return {'text': ERROR_MESSAGE}
        return {
            'text': content
        }

    @staticmethod
    async def pay_ios_version():
        content = await ContentApi.get_pay_ios_version()
        if not content:
            log.error("Content not found for pay_ios_version")
            return {'text': ERROR_MESSAGE}
        return {
            'text': content
        }
