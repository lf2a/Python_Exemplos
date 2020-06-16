'''Esta função retorna uma lista de tuplas,
    onde a i-ésima tupla contém o i-ésimo
    elemento de cada um dos argumentos.

    ex:
    input:  zip([1, 2], [3, 4])
    output: (1, 3)
            (2, 4)
'''

import itertools

print('# 0')
for i in zip([1, 2, 3]):
    print(i)

print('\n# 1')
for i in zip([1, 2, 3], ['A', 'B', 'C']):
    print(i)

print('\n# 2')
for i in zip([1, 2, 3], ['A', 'B', 'C'], ['#', '$', '%']):
    print(i)

print('\n# 3')
for i in zip([1, 2, 3], ['A', 'B']):
    print(i)

print('\n# 4')
for i in itertools.zip_longest([1, 2, 3], ['A', 'B']):
    print(i)

print('\n# 5')
values = zip([1, 2, 3], ['A', 'B'])
a, b = zip(*values)
print(a, b)

print('\n# 6')
values_zl = itertools.zip_longest([1, 2, 3], ['A', 'B'])
a, b = zip(*values_zl)
print(a, b)
