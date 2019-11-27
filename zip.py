'''Esta função retorna uma lista de tuplas,
    onde a i-ésima tupla contém o i-ésimo
    elemento de cada um dos argumentos.

    ex:
    input:  zip([1, 2], [3, 4])
    output: (1, 3)
            (2, 4)
'''


from itertools import zip_longest as zl # lines 35 and 44


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
for i in zl([1, 2, 3], ['A', 'B']):
    print(i)


print('\n# 5')
values = zip([1, 2, 3], ['A', 'B'])
a, b = zip(*values)
print(a, b)

values_zl = zl([1, 2, 3], ['A', 'B'])
a, b = zip(*values_zl)
print(a, b)
