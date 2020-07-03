"""Formas de fazer uma tupla
tupla = (1,) -> precisa ter uma virgula no final, senao vai tratar como um inteiro
tupla = 12, 'luiz', [12, 45, 6]
tupla = tuple([34, 67, 88])

Tuplas são imutaveis
"""

tupla = (1, 23, 45, 75, 7, 4, 23, 89, 45, 23, 56)
print(tupla)

print(tupla[1])  # 23
print(tupla[1:4])  # (23, 45, 75)
print(tupla[1:8:2])  # (23, 75, 4, 89)
print(tupla[::-1])  # (56, 23, 45, 89, 23, 4, 7, 75, 45, 23, 1)

# del tupla  # excluindo uma tupla

print(tupla.count(23))  # 3
print(tupla.index(4))  # 5
