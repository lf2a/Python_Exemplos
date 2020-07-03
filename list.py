lista = [12, 35, 84, 7, 23, 52, 7, 88, 24, 67, 80]
print(lista)

print(lista[1:4])  # [35, 84, 7]
print(lista[1:8:2])  # [35, 7, 52, 88]
print(lista[::-1])  # [80, 67, 24, 88, 7, 52, 23, 7, 84, 35, 12] lista reversa

lista.append(12)  # adiciona um item na lista
print(lista)  # [12, 35, 84, 7, 23, 52, 7, 88, 24, 67, 80, 12]

lista.extend([45, 56, 78])
print(lista)  # [12, 35, 84, 7, 23, 52, 7, 88, 24, 67, 80, 12, 45, 56, 78]

del lista[-1]  # exclui o ultimo item
print(lista)  # [12, 35, 84, 7, 23, 52, 7, 88, 24, 67, 80, 12, 45, 56]

del lista[8:]  # exclui até o oitavo item em diante
print(lista)  # [12, 35, 84, 7, 23, 52, 7, 88]

"""Exclui a lista inteira 
NameError: name 'lista' is not defined

>>> del lista 
"""

lista.remove(88)  # remove o item 88
print(lista)  # [12, 35, 84, 7, 23, 52, 7]

lista.pop()  # remove o ultimo item
print(lista)  # [12, 35, 84, 7, 23, 52]

lista.pop(0)  # remove o item do indice 0
print(lista)  # [35, 84, 7, 23, 52]

# lista.clear()  # limpa a lista []

nova_lista = lista.copy()  # copia a lista | faz um shallow copy
nova_lista.append(999)
print(f'lista:\t\t{lista}\nnova_lista:\t{nova_lista}')
del nova_lista

lista.insert(0, 23)  # insere 23 no indice 0
print(lista)  # [23, 35, 84, 7, 23, 52]

print(lista.index(7))  # retorna o index do valor 7 | 3

print(lista.count(23))  # conta quantos valores do indice são iguais a 23 | 2

lista.sort()  # ordena uma lista
print(lista)  # [7, 23, 23, 35, 52, 84]

lista.reverse()  # reverte a ordem dos items
print(lista)  # [84, 52, 35, 23, 23, 7] | igual a lista[::-1]
