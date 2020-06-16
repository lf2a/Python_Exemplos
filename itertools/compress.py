import itertools

""" compress(data, selectors)
    Isso cria um iterador que filtra elementos, dos dados, para os quais os valores do seletor são True.
"""

for i in itertools.compress('ABCDEF', [1, 'true', 0, True, 0, 1]):
    print(i)
