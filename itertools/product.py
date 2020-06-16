import itertools

""" product(*iterables, repeat)
    Retorna o produto cartesiano das iteráveis​de entrada.
    Isso é equivalente a um loop for aninhado.
"""

for i in itertools.product([1, 2, 3], [4, 5, 6]):
    print(i)
