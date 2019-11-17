from time import sleep
from multiprocessing import Pool, cpu_count

'''Utilizando todas as cpu para executar o codigo ao mesmo tempo
'''

def count(t):
    for i in range(3):
        print('[count - %d] index: %d' % (t, i))
        sleep(5)

if __name__ == '__main__':
    pool = Pool(cpu_count())
    pool.map(count, [i for i in range(3)])
    