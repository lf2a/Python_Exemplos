"""Set é uma coleção de items não ordenados e não há valores duplicados"""

conjunto = {23, 45, 767, 45, 776, 45, 34, 23, 45, 63, 45}
print(conjunto)  # {34, 776, 45, 23, 63, 767}

conjunto.add(100)
print(conjunto)  # {34, 100, 776, 45, 23, 63, 767}

conjunto.update([1, 2, 2, 3])
print(conjunto)  # {1, 34, 2, 100, 3, 776, 45, 23, 63, 767}

conjunto.discard(34)  # removendo o elemento 34
print(conjunto)  # {1, 2, 100, 3, 776, 45, 23, 63, 767}

conjunto.remove(100)  # removendo o elemento 100
print(conjunto)  # {1, 2, 3, 776, 45, 23, 63, 767}

conjunto.pop()  # remove o primeiro elemento
print(conjunto)  # {2, 3, 776, 45, 23, 63, 767}

# conjunto.clear()  # limpa o set

# OPERAÇÕES

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(f'a: {a}\nb: {b}')

print(a | b)  # União -> irá unir todos os conjunto em um unico conjunto | {1, 2, 3, 4, 5, 6, 7, 8}
print(a.union(b))  # a mesma coisa que a de cima| outra forma | {1, 2, 3, 4, 5, 6, 7, 8}

print(a & b)  # Interseção -> ira pegar os items que existem nos dois conjuntos | {4, 5}
a.intersection(b)  # a mesma coisa que a de cima| outra forma | {4, 5}

print(a - b)  # Diferença -> irá pegar os de a qua não há em b | {1, 2, 3} | a.difference(b) outra forma
print(b - a)  # Diferença -> irá pegar os items de b que não há em a | {8, 6, 7} | b.deifference(a) outra forma

# Diferenca simetrica -> irá pegar os items de a que não há em b e os items de b que não há em a
print(a ^ b)  # a.symmetric_difference(b) | outra forma | {1, 2, 3, 6, 7, 8}
