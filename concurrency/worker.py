import time
from time import sleep
from threading import Thread

def count(t='', delay=5):
    for i in range(5):
        print('[count - %s] index: %d' % (t, i))
        print(time.time())
        sleep(delay)


class CountWorker(Thread):
    def __init__(self):
        Thread.__init__(self)
    
    def run(self):
        count()


class CountWorker_tow(Thread):
    def __init__(self):
        Thread.__init__(self)
    
    def run(self):
        count(t='teste')


def main():    
    worker = CountWorker()
    worker.daemon = True
    worker.start()
    
    worker = CountWorker_tow()
    worker.daemon = True
    worker.start()

    
if __name__ == '__main__':
    main()