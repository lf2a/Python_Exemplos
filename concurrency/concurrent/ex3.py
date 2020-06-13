import time
from concurrent.futures import ThreadPoolExecutor

'''Irá executar 'count' 3 (loop) vezes
    sendo que ira ser executado 'um' e 'dois' ao mesmo tempo 

    output:
        [count - um] index: 0
        [count - dois] index: 0
        
        [count - um] index: 1
        [count - dois] index: 1

        [count - um] index: 2
        [count - dois] index: 2
'''


def count(t):
    for i in range(3):
        print('[count - %s] index: %d' % (t, i))
        time.sleep(5)


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(count, ['um', 'dois'])
