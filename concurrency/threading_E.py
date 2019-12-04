from threading import (
    active_count,
    current_thread,
    get_ident,
    enumerate,
    main_thread,
    Thread,
    currentThread
)
import time

'''active_count()
This returns the number of alive(currently) Thread objects.
This is equal to the length the of the list that enumerate() returns.
'''
num_objects = active_count()
print(num_objects)


'''current_thread()
Based on the caller’s thread of control,
this returns the current Thread object.
If this thread of control isn’t through ‘threading’,
it returns a dummy thread object with limited functionality.
'''
thread = current_thread()
print(thread)


'''get_ident()
returns the current thread’s identifier,
which is a non-zero integer.
We can use this to index a dictionary of thread-specific data.
Apart from that, it has no special meaning.
When one thread exits and another creates,
Python recycles such an identifier.
'''
id = get_ident()
print(id)


'''enumerate()
This returns a list of all alive(currently) Thread objects.
This includes the main thread, daemonic threads,
and dummy thread objects created by current_thread().
This obviously doesn’t include terminated threads as well
as those that haven’t begun yet.
'''
threads = enumerate()
print(threads)


'''main_thread()
This method returns the main Thread object.
Normally, it is that thread which started the interpreter.
'''
main_t = main_thread()
print(main_t)


def test(i):
    # time.sleep(i)
    for i in range(2):
        print('ola', i)
    print(currentThread().getName())


def main():
    for i in range(3):
        t = Thread(name=i,target=test, args=[i])
        t.start()


if __name__ == '__main__':
    main()
