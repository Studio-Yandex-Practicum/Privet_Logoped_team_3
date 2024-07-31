import logging

from api.utils import async_http_get

log = logging.getLogger(__name__)


async def send_id(id):
    response = await async_http_get('None')
    print(response)
    log.info('Response: %s', response)
    """
        if isinstance(response, PostResponse):
            print(response.status)
            print(response.message)
        
    """

    return True
