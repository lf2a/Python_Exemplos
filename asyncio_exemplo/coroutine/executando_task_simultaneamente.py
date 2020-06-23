"""
    As tarefas são uma das principais maneiras de interagir com o loop de eventos.
    As tarefas envolvem corotinas e rastreiam quando são concluídas. As tarefas são
    subclasses de Future, portanto, outras corotinas podem esperar por elas e cada uma
    tem um resultado que pode ser recuperado após a conclusão da tarefa.
"""

import asyncio


async def task_func():
    print('task_func')
    return 'resultado'


async def task_func2():
    print('task_func2')
    return 'resultado2'


async def main(loop):
    print('criando task')

    task = loop.create_task(task_func())
    task2 = loop.create_task(task_func2())

    print(f'esperando por {task}')
    print(f'esperando por {task2}')

    # para cancelar uma task, gera uma exception (asyncio.CancelledError)
    # task.cancel()

    retorno = await task
    retorno2 = await task2

    print(f'task finalizada {task}')
    print(f'task finalizada {task2}')

    print(f'retorno: {retorno}')
    print(f'retorno2: {retorno2}')


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
