import logging
from http import HTTPStatus

from api.schemas import UserProfile
from api.utils import (
    async_http_get, async_http_post, async_http_put
)
from config import bot_env
from constants import PROFILE_ID_PATH, PLATFORM

log = logging.getLogger(__name__)


class Roles:

    @staticmethod
    async def check_user_registered(user_id):
        user = await Roles._get_id(str(user_id))
        if user and user['status'] == HTTPStatus.OK:
            return True
        return False


    @staticmethod
    async def _get_id(user_id):
        try:
            response = await async_http_get(
                bot_env.url_api + PROFILE_ID_PATH + user_id + '/'
            )
            print(response)
            log.info('Response: %s', response)
            return response
        except Exception as e:
            return None

    @staticmethod
    async def _post_id_with_role(user_id, role, username):
        try:
            response = await async_http_post(
                bot_env.url_api + PROFILE_ID_PATH,
                data=Roles.fill_user_data(user_id, role, username)
            )
            print(response)
            log.info('Response: %s', response)
            return response
        except Exception as e:
            return None

    @staticmethod
    async def send_role_for_id(user_id, role, username):
        user_id = str(user_id)
        response = await Roles._get_id(user_id)
        print(response)
        if not response or response['status'] == HTTPStatus.NOT_FOUND:
            log.info('Not found user, create new')
            await Roles._post_id_with_role(user_id, role, username)

        elif response['status'] == HTTPStatus.OK:
            current_user = UserProfile.parse_raw(response['text'])
            if not Roles.check_user_role(current_user.role, role):
                log.info('User has not required role, update')
                response = await Roles._modify_user(user_id, role, username)

        log.info('Response: %s', response)
        return True

    @staticmethod
    async def _modify_user(user_id, role, username):
        response = await async_http_put(
            bot_env.url_api + PROFILE_ID_PATH + user_id + '/',
            data=Roles.fill_user_data(user_id, role, username)
        )
        print(response)
        return response

    @staticmethod
    def fill_user_data(user_id, role, username):
        return {
            'user_id': user_id,
            'username': username,
            'platform': PLATFORM,
            'role': Roles.role(role)
        }

    @staticmethod
    def check_user_role(current_role, role):
        test_role = Roles.role(role)
        return current_role == test_role

    @staticmethod
    def role(role):
        return 'parent' if role == 'Родитель' else 'speech_therapist'
