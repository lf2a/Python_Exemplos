import asyncio


async def coroutine():
    print('coroutine')
    return True


event_loop = asyncio.get_event_loop()
try:
    retorno = event_loop.run_until_complete(coroutine())
    print(f'coroutine: {retorno}')
finally:
    event_loop.close()
