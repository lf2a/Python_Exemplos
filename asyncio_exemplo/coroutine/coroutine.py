"""
    As coroutine são uma construção de linguagem projetada para operação simultânea.
    Uma função de coroutine cria um objeto de coroutine quando chamada, o chamador pode
    executar o código da função usando o método send() da coroutine. Uma coroutine pode
    pausar a execução usando a palavra-chave wait com outra coroutine. Enquanto está em
    pausa, o estado da coroutine é mantido, permitindo que ele retome de onde parou na
    próxima vez que for despertado.
"""

import asyncio


async def coroutine():
    print('coroutine')


# inicia o loop
event_loop = asyncio.get_event_loop()
try:
    print('Iniciando uma coroutine')
    cor = coroutine()
    print('Entrando no event loop')
    # Existem algumas maneiras diferentes de fazer com que o loop de eventos assíncronos inicie uma corrotina.
    # O mais simples é usar run_until_complete(), passando a coroutine diretamente para ele.
    event_loop.run_until_complete(cor)
finally:
    print('Fechando event loop')
    # para o loop
    event_loop.close()
