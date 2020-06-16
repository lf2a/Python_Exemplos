# retorna uma lista com 10 valores, em que cada iteração o valor (x) é incrementado e elevado ao quadrado.
nums = list(map(lambda x: x ** 2, range(10)))
print(nums)

# retorna uma lista com os valores pares de 0 a 9, verificando se o valor é par através de um 'if';
even1 = [x for x in range(10) if x % 2 == 0]
print(even1)

# o mesmo retorna que a expressão acima só que utilizando filter(função, iteravel) e convertendo o retorno para uma lista
even2 = list(filter(lambda x: x % 2 == 0, range(10)))
print(even2)

# matrix

# list
# retorna uma matriz de listas, usa dois for-loop com alcance até 2 e depois faz um if verificando se x e y são numeros pares.
matrix1 = [[x, y] for x in range(3) for y in range(3) if x % 2 == 0 and y % 2 == 0]
print(matrix1)

# tuple
# o mesmo que a expressão de cima, só que esta retona uma lista de tuplas
matrix2 = [(x, y) for x in range(3) for y in range(3) if x % 2 == 0 and y % 2 == 0]
print(matrix2)

# set
# o mesmo que a expressão de cima, só que esta retona uma lista de conjuntos
matrix3 = [{x, y} for x in range(3) for y in range(3) if x % 2 == 0 and y % 2 == 0]
print(matrix3)
