from concurrent.futures import ProcessPoolExecutor
import os


def task(n):
    print('Processo {}'.format(os.getpid()))
    return n


def main():
    with ProcessPoolExecutor(max_workers=3) as executor:
        task1 = executor.submit(task, 12)
        task2 = executor.submit(task, 20)
        print('task1: ', task1.result())
        print('task2: ', task2.result())


if __name__ == '__main__':
    main()
