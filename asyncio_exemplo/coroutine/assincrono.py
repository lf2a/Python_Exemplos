"""
    Um futuro representa o resultado de um trabalho que ainda não foi concluído.
    O loop de eventos pode observar o estado de um objeto Futuro para indicar que está pronto,
    permitindo que uma parte de um aplicativo aguarde que outra peça conclua algum trabalho.
"""

import asyncio


def func(future, result):
    print(f'colocando no futuro: {result}')
    future.set_result(result)


# event_loop = asyncio.get_event_loop()
# try:
#     feito = asyncio.Future()
#
#     print('agendando')
#     event_loop.call_soon(func, feito, 'OK')
#
#     print('Entrando no event loop')
#     resultado = event_loop.run_until_complete(feito)
#     print(f'valor retornado: {resultado}')
# finally:
#     print('closing event loop')
#     event_loop.close()
#
# print(f'valor futuro: {feito.result()}')


# usando await

async def main(loop):
    feito = asyncio.Future()

    print('scheduling mark_done')
    loop.call_soon(func, feito, 'OK')

    resultado = await feito
    print(f'valor retornado: {resultado}')


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
