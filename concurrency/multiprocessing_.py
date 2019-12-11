from multiprocessing import (
    Pool,
    Process,
    set_start_method,
    Queue, Pipe
)
import time
from datetime import datetime
import os

'''
O pacote de multiprocessamento oferece simultaneidade local e remota,
efetivamente ultrapassando o bloqueio global de intérpretes usando
subprocessos em vez de threads.

O objeto Pool oferece um meio conveniente de paralelizar a execução de uma
função entre vários valores de entrada, distribuindo os dados de entrada
entre processos (paralelismo de dados)
'''


def wait_func(id):
    now = datetime.now()
    for i in range(4):
        time.sleep(1)
        print('%d wait_func: %d | %02d:%02d.%d' % (
            id,
            i,
            now.minute,
            now.second,
            now.microsecond
            )
        )
    return '%d wait_func' % id


def ex1():
    with Pool(processes=5) as p:
        print(p.map(wait_func, [1, 2, 3, 4]))


'''
No multiprocessamento, os processos são gerados criando um objeto Process
e depois chamando seu método start ().
'''


def test_loop_p(id):
    for i in range(5):
        time.sleep(1)
        print('%d test_loop_p: %d' % (id, i))
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def ex2():
    p1 = Process(target=test_loop_p, args=(1, ))
    p2 = Process(target=test_loop_p, args=(2,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()


'''
spawn: O processo pai inicia um novo processo de intérprete de python.
O processo filho herdará apenas os recursos necessários para executar
o método run () dos objetos do processo. Em particular, descritores
de arquivo e identificadores desnecessários do processo pai não serão
herdados. O início de um processo usando esse método é bastante lento
comparado ao uso do fork ou forkserver.
Disponível no Unix e Windows. O padrão no Windows e no macOS.
'''


def test_queue(q):
    q.put('test_queue')


def ex3():
    set_start_method('spawn')
    q = Queue()
    # or
    # ctx = mp.get_context('spawn')
    # q = ctx.Queue()
    p = Process(target=test_queue, args=(q,))
    p.start()
    print(q.get())
    p.join()


'''
multiprocessing supports two types of communication channel
between processes: Queue e Pipe
'''


def pipe(p):
    p.send(['luiz', 19])
    p.close()


def ex4():
    q = Queue()
    p = Process(target=test_queue, args=(q,))
    p.start()
    print(q.get())
    p.join()


def ex5():
    parent_conn, child_conn = Pipe()
    p = Process(target=pipe, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()


if __name__ == '__main__':
    # ex1()
    # ex2()
    # ex3()
    # ex4()
    ex5()
