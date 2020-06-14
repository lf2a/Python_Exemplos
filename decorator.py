"""Um decorator pega uma função adiciona algumas funcionalidades e em seguida a retorna
"""


def decorator(func):
    def inner(data):
        print(f'decorator: Olá {data}')
        return func('Luiz Filipy')

    return inner


def decorator2(**kwargs):
    def inner(func):
        print(f'decorator2: {kwargs}')
        return func(12345, **kwargs)

    return inner


@decorator
def test(data):
    print(f'test: {data}')


test('Mundo')


@decorator2(id='luiz')
def test2(num, **kwargs):
    print(f'test2: {kwargs}\t{num}')
