dicionario = {
    'nome': 'Luiz Filipy',
    'idade': 20,
    'is_developer': True,
    'languages': ['Python', 'Java', 'JavaScript', 'Golang']
}
print(dicionario)

"""Diferenca
dicionario["nome"] -> irá pegar o valor do item da chave nome, mas se a chave não existir ele lança um erro: KeyError
dicionario.get("nome") -> irá pegar o valor do item da chave nome, mas se ele não encontrar a chave ele retorna None
"""
print(dicionario["nome"])  # Luiz Filipy
print(dicionario.get('nome'))  # Luiz Filipy

dicionario["nome"] = 'Luiz'
print(dicionario.get('nome'))  # Luiz

print(dicionario.pop('idade'))  # remove idade e retorna o valor da chave idade
print(dicionario.get('idade'))  # None

# dicionario.clear()  # limpa o dicionario
# del dicionario  # exclui o dicionario

print(dicionario.items())  # retorna um novo dicionario no formato (key, value)
# dict_items([('nome', 'Luiz'), ('is_developer', True), ('languages', ['Python', 'Java', 'JavaScript', 'Golang'])])

print(dicionario.keys())  # retorna todas as chaves | dict_keys(['nome', 'is_developer', 'languages'])

# Retorna o valor correspondente se a chave estiver no dicionário. Senao, insere a chave com o valor e retorna o valor
# (o padrão é None).
dicionario.setdefault('ano', 2020)
print(dicionario.get('ano'))  # 2020

print(dicionario.values())  # retorna os valores do dicionario
# dict_values(['Luiz', True, ['Python', 'Java', 'JavaScript', 'Golang'], 2020])

notas = {}.fromkeys(['Mat', 'Eng', 'Port'], 10)
print(notas)  # {'Mat': 10, 'Eng': 10, 'Port': 10}
