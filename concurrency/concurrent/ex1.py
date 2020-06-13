# ThreadPoolExecutor é uma subclasse Executor que usa um pool de threads para executar chamadas de forma assíncrona.
from concurrent.futures import ThreadPoolExecutor


def task(n):
    print('n: {}'.format(n))
    return n


def main():
    print('Inicio')
    with ThreadPoolExecutor(max_workers=3) as executor:
        future = executor.submit(task, 2)
        future = executor.submit(task, 3)
        future = executor.submit(task, 4)
        print(future.result())
    print('OK')


if __name__ == '__main__':
    main()
