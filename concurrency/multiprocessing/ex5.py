# Sincronização entre processos
from multiprocessing import Process, Lock


def show(l, i):
    l.acquire()
    try:
        print('ok', i)
    finally:
        l.release()


if __name__ == '__main__':
    """
    Use o Lock() para garantir que apenas um processo seja impresso na saída padrão de cada vez
    """
    lock = Lock()

    print('Com sincronização')
    for i in range(10):
        Process(target=show, args=(lock, i)).start()
