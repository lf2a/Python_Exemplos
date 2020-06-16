# yield - retorna um generator

"""
    Na primeira vez que a função for executada, ela vai rodar do começo e parar até tocar no primeiro yield.

    Após encontrar o primeiro yield, ela vai continuar do ponto que foi parado até tocar o próximo yield.

    Quando não for encontrado um yield, a exceção StopIteration é lançada.
"""


def pares():
    for i in range(10):
        if i % 2 == 0:
            yield '%d' % i
        else:
            yield 'impar'


lista = pares()

# outra forma de acessar um generator, usando next()
print(next(lista))
print(next(lista))

# enumerate(iterable) - recebe um iterable e retora dois valores, o primeiro é o indice e o sundo é o valor
# referente a aquele indice
for index, value in enumerate(lista):
    print('lista[%s] = %s' % (index, value))

