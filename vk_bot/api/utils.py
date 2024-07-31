import logging

import aiohttp

log = logging.getLogger(__name__)

TIMEOUT = 2


async def async_http_get(url, full_response=True, timeout=TIMEOUT):
    log.info('Get: %s', url)

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=timeout) as response:
                if not full_response:
                    response = await response.read()
        return response
        # return response.decode('utf-8')
    except Exception as e:
        log.error('HTTP GET error: %s', e)
        return None


async def async_http_post(
    url, data=None, headers=None, json=None, timeout=TIMEOUT
):
    log.info('Post: %s', url)

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    url,
                    timeout=timeout,
                    data=data,
                    json=json,
                    headers=headers) as response:
                resp = await response.text()
                log.info('Post: %s',resp)
                return response
                # return await response.text()
    except Exception as e:
        log.error('HTTP POST error: %s', e)
        return e
