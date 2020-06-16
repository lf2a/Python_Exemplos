import itertools

""" count(start, step)
    Vai contando de 2 em 2 a partir de 0.
"""

for even in itertools.count(0, 2):
    if even > 20:
        break
    print(even)
