"""
A classe Pool representa um conjunto de worker processes. Possui métodos que permitem que as tarefas sejam
transferidas para os processos de trabalho de algumas maneiras diferentes.
"""
from multiprocessing import Pool
import os


def mult(x):
    return x * x


if __name__ == '__main__':
    # inicia o worker com 4 processos
    with Pool(processes=4) as pool:

        # print "[0, 1, 4,..., 81]"
        print(pool.map(mult, range(10)))

        # mostra os mesmos numeros de ordem abitraria
        for i in pool.imap_unordered(mult, range(10)):
            print(i)

        # calcula "mult(20)" assincronamente
        res = pool.apply_async(mult, (20,))  # runs in *only* one process
        print(res.get(timeout=1))  # mostra "400"

        # calcula "os.getpid()" assincronamente
        res = pool.apply_async(os.getpid, ())  # runs in *only* one process
        print(res.get(timeout=1))  # prints the PID of that process

        # launching multiple evaluations asynchronously *may* use more processes
        multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]
        print([res.get(timeout=1) for res in multiple_results])
