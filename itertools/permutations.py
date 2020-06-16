import itertools

""" permutations(iterable, r)
    Ele gera todas as permutações possíveis em ordem lexicográfica, e não há repetição de elementos.
"""

for i in itertools.permutations('123'):
    print(i)
