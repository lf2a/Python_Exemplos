import itertools

""" groupby(iterable, key)
    Faz um iterator que recebe um iterável e retorna chaves de grupos consecutivos.
    Este são sub-iterators agrupados por uma chave.
"""

for i, j in itertools.groupby('AAAAABBCCCCCDDDCCCBBA'):
    print(f'{i} - {list(j)}')
