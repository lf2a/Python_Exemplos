# Expressão lambda permite escrever funções anônimas/sem-nome usando apenas uma linha de código.

# x e y são parametros que serão somados e retornados
soma = lambda x, y: x + y
print(soma(2, 6))

idades = [2, 10, 34, 12, 46, 18, 22]

# retorna uma lista com os numeros maiores ou iguais a 18
maiores_de_idade = list(filter(lambda x: (x >= 18), idades))
print(maiores_de_idade)

# retorna uma lista de valores booleanos em que os valores maiores ou iguais a 18 são True
# a lista retorna está na mesma ordem que a lista de entrada -> 'idades'
maiores_de_idade = list(map(lambda x: (x >= 18), idades))
print(maiores_de_idade)
