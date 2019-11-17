soma = lambda x, y: x + y
print(soma(2, 6))

idades = [2, 10, 34, 12, 46, 18, 22]

#maiores_de_idade = list(filter(lambda x: (x >= 18), idades))
#print(maiores_de_idade)

maiores_de_idade = list(map(lambda x: (x >= 18), idades))
print(maiores_de_idade)