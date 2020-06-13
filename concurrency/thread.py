import threading
import time

"""active_count()
Retorna o numero de threads ativas
"""
num_objects = threading.active_count()
print(num_objects)

"""current_thread()
Retorna o thread atual
"""
thread = threading.current_thread()
print(thread)

"""get_ident()
Retorna o identificador do segmento atual,
que é um número inteiro diferente de zero.
"""
id = threading.get_ident()
print(id)

'''main_thread()
Retorna o thread principal
'''
main_t = threading.main_thread()
print(main_t)


def test(i):
    for i in range(2):
        print('ola', i)
    print(threading.currentThread().getName())


def main():
    for i in range(3):
        t = threading.Thread(name=i, target=test, args=[i])
        t.start()


if __name__ == '__main__':
    main()
