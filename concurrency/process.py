from time import sleep
from multiprocessing import Process

'''Rodando duas funcoes paralelamente
    criando dois processos e executando em paralelo
'''

def count_one():
    for i in range(6):
        print('[count_one] index: %d' % i)
        sleep(5)

def count_two():
    for i in range(6):
        print('[count_two] index: %d' % i)
        sleep(5)
        
if __name__ == '__main__':
    one = Process(target=count_one)
    one.start()
    
    two = Process(target=count_two)
    two.start()
    
    one.join()
    two.join()
    