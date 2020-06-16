import itertools

""" cycle(iterable)
    Cria um iterador a partir de um iterável e vai imprimindo os elementos contidos dentro
    do iterável fazendo isso em um loop infinito. ex. 1, 2, 1, 2, ...
"""

max = 0
for value in itertools.cycle([1, 2]):
    if max < 10:
        max += 1
        print(value)
    else:
        break
