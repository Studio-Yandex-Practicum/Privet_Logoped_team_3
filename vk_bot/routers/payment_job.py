from routers.keyboard import PAYMENT_MENU


class PaymentMenu:

    @staticmethod
    async def response(message):
        if message == PAYMENT_MENU[0]:
            return await PaymentMenu.pay_full_version()
        elif message == PAYMENT_MENU[1]:
            return await PaymentMenu.pay_ios_version()

    @staticmethod
    async def pay_full_version():
        return {
            'text': 'pay_full_version в процессе реализации'
        }

    @staticmethod
    async def pay_ios_version():
        return {
            'text': 'pay_for_ios в процессе реализации'
        }
