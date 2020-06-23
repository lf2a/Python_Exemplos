import asyncio


async def func():
    print('Func')
    print('Esperando func1')
    result1 = await func1()
    print('Esperando func2')
    result2 = await func2(result1)
    return result1, result2


async def func1():
    print('Func 1')
    return True


async def func2(arg):
    print('Func 2')
    return 'result2 é ' + str(arg)


event_loop = asyncio.get_event_loop()
try:
    retorno = event_loop.run_until_complete(func())
    print(f'retorno: {retorno}')
finally:
    event_loop.close()
