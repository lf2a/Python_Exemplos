from multiprocessing import Process, Queue


def get_dados(q: Queue):
    q.put([12, True, None, ''])


if __name__ == '__main__':
    """Queue é utilizado para criar um canal de comunicação entre processos
    Queues são thread e process safe.
    """
    q = Queue()
    p = Process(target=get_dados, args=(q,))
    p.start()
    print(q.get())
    p.join()
