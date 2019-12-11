# Python Standard Library
import concurrent.futures
import time
from datetime import datetime


def wait_func(id, sec):
    now = datetime.now()
    for i in range(4):
        time.sleep(sec)
    return 'ID: %d\t%02d:%02d.%d' % (
        id,
        now.minute,
        now.second,
        now.microsecond
    )


def for_test(id):
    for i in range(4):
        time.sleep(1)
        print('%d for_test: %d' % (id, i))
    return id


def even_odd(num):
    if num % 2 == 0:
        return True
    else:
        return False


def ex1():
    '''
    alvo -> funcao ou metodo
    submit() -> Prepara o alvo, para ser executado e retorna um objeto Future que
    representa a execução do alvo.
    '''
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        # future1 = executor.submit(func, *params, **kwargs) with params
        future1 = executor.submit(for_test, 1)
        future2 = executor.submit(for_test, 2)
        print(future1.result())
        print(future2.result())


def ex3():
    # A subclasse `Executor` usa um pool de no máximo `max_workers` de
    # threads para executar chamadas de forma assíncrona.
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_load = {
            # `load` alvo, `id, sec` parametros
            executor.submit(wait_func, id=id, sec=1): id for id in range(5)
        }

        for future in concurrent.futures.as_completed(future_load):
            # result() é o conteudo retornado pelo `alvo ou funcao ou metodo`
            print(future.result())


def ex2():
    '''
    map() -> o alvo é executado de forma assíncrona e
    várias chamadas para o alvo podem ser feitas simultaneamente
    retorna um iterator.
    Ao usar ProcessPoolExecutor, esse método divide iteráveis ​​em vários
    pedaços que ele envia ao pool como tarefas separadas. O tamanho
    (aproximado) desses chunks pode ser especificado configurando chunksize
    como um número inteiro positivo.
    Para iteráveis ​​muito longos, o uso de um valor grande para tamanho
    de chunks pode melhorar significativamente o desempenho em comparação
    com o tamanho padrão de 1. Com o ThreadPoolExecutor, o chunksize não
    tem efeito.
    '''
    nums = [2, 4, 7, 2, 8, 4, 9]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for number, type in zip(nums, executor.map(even_odd, nums)):
            print('%d\t%s' % (number, type))


if __name__ == '__main__':
    ex1()
    # ex3()
    # ex2()
