# Sharing state between processes
from multiprocessing import Process, Value, Array


def sub(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]


if __name__ == '__main__':
    """ Os dados podem ser armazenados em um mapa de memória compartilhada usando Value ou Array.
    Os argumentos 'd' e 'i' usados​ao criar num e arr são códigos de tipo do tipo usado pelo módulo array: 'd' 
    indica uma float de precisão dupla (double) e 'i' indica um número inteiro assinado. Esses objetos 
    compartilhados serão seguros para processos e threads.

    Um gerente retornado por Manager () suportará tipos: list, dict, Namespace, Lock, RLock, Semaphore, 
    BoundedSemaphore, Condition, Event, Barrier, Queue, Value and Array.
    
    ex:
    from multiprocessing import Process, Manager

    def f(d, l):
        d[1] = '1'
        d['2'] = 2
        d[0.25] = None
        l.reverse()
    
    if __name__ == '__main__':
        with Manager() as manager:
            d = manager.dict()
            l = manager.list(range(10))
    
            p = Process(target=f, args=(d, l))
            p.start()
            p.join()
    
            print(d)
            print(l)
    """
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=sub, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])
