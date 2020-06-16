import itertools

""" chain(*iterable)
    Cria um iterador a partir dos elementos do primeiro iterável, depois a partir do segundo e assim por diante.
    Ele passa para o próximo iterável à medida que um iterável se esgota.
"""

for i in itertools.chain('Luiz', 'Filipy', 'Brasil'):
    print(i)
