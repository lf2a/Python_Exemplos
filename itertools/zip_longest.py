import itertools

""" zip_longest(*iterables, fillvalue)

    Faz um iterator agragando elementos de cada iterable. 
    O fillvalue irá preencher os lugares restantes com o valor.
"""

for i in itertools.zip_longest('ABC', '12345', 'luiz', fillvalue='*'):
    print(i)
