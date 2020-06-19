"""Um decorator pega uma função adiciona algumas funcionalidades e em seguida a retorna
"""


# function decorator
def decorator(func):
    def inner(data):
        print(f'decorator: Olá {data}')
        return func('Luiz Filipy')

    return inner


@decorator
def test(data):
    print(f'test: {data}')


test('Mundo')


def decorator2(**kwargs):
    def inner(func):
        print(f'decorator2: {kwargs}')
        return func(12345, **kwargs)

    return inner


@decorator2(id='luiz')
def test2(num, **kwargs):
    print(f'test2: {kwargs}\t{num}\n')


# class decorator

class MeuDecorator:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        print(args)
        self.function(*args, **kwargs)


@MeuDecorator
def test3(n):
    print(n)


test3('Filipy')


class MeuDecorator2:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        print(f'__init__ args: {args}\tkwargs: {kwargs}')

    def __call__(self, *args, **kwargs):
        print(f'__call__ args: {args}\tkwargs: {kwargs}')
        if self.kwargs["login_requerido"]:
            print('logado')
            kwargs['user'] = {'id': 123, 'name': 'luiz'}
        else:
            print('não logado')
            kwargs['user'] = None
        self.function = args[0](kwargs, {'response': None})


@MeuDecorator2(path='/', login_requerido=True)
def test3(req, res):
    print(f'req: {req}\tres: {res}\n')


@MeuDecorator2(path='/', login_requerido=False)
def test4(req, res):
    print(f'req: {req}\tres: {res}')
