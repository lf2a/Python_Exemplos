import itertools

""" combinations(iterabe, r)
    Isso retorna subsequências de comprimento (r) dos elementos do iterável.
"""

for i in itertools.combinations('ABCD', 3):
    print(i)
