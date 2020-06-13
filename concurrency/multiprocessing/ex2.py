import os
from multiprocessing import Process


def print_nome(nome):
    print(f'Olá {nome} | processo pai: {os.getppid()} | id: {os.getpid()}')


if __name__ == '__main__':
    """ Cria um processo para executar a função 'print_nome'
    """
    p = Process(target=print_nome, args=('Luiz',))
    p.start()
    p.join()
