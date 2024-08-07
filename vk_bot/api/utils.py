import logging

import aiohttp

log = logging.getLogger(__name__)

TIMEOUT = 2


async def async_http_get(url, full_response=True, timeout=TIMEOUT):
    log.info('Get: %s', url)

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=timeout) as response:
                # if not full_response:
                #     response_read = await response.read()
                text = await response.read()
        # return response
        return {
            'status': response.status,
            'text': text
        }
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
                return {
                    'status': response.status,
                    'text': resp
                }
                # return await response.text()
    except Exception as e:
        log.error('HTTP POST error: %s', e)
        return e


async def async_http_patch(
    url, data=None, headers=None, json=None, timeout=TIMEOUT
):
    log.info('Patch: %s', url)

    try:
        async with aiohttp.ClientSession() as session:
            async with session.patch(
                    url,
                    timeout=timeout,
                    data=data,
                    json=json,
                    headers=headers) as response:
                resp = await response.text()
                log.info('Patch: %s', resp)
                return {
                    'status': response.status,
                    'text': resp
                }
                # return await response.text()
    except Exception as e:
        log.error('HTTP PATCH error: %s', e)
        return e


async def async_http_put(
    url, data=None, headers=None, json=None, timeout=TIMEOUT
):
    log.info('Put: %s', url)

    try:
        async with aiohttp.ClientSession() as session:
            async with session.put(
                    url,
                    timeout=timeout,
                    data=data,
                    json=json,
                    headers=headers) as response:
                resp = await response.text()
                log.info('Put: %s', resp)
                return {
                    'status': response.status,
                    'text': resp
                }
                # return await response.text()
    except Exception as e:
        log.error('HTTP PUT error: %s', e)
        return e