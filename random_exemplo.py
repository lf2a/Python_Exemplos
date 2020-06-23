"""
    O módulo aleatório fornece um rápido gerador de números pseudoaleatórios
    baseado no algoritmo Mersenne Twister.
"""

import random
import time

# A função random() retorna o próximo valor aleatório de ponto flutuante da sequência gerada.
# Todos os valores de retorno estão dentro do intervalo 0 <= n <1.0.
print(f'1 - random: {random.random()}')

# Para gerar números em um intervalo numérico específico, use uniforme().
print(f'1 - uniform: {random.uniform(10, 100)}')

"""
    random() produz valores diferentes cada vez que é chamado e tem um período muito grande 
    antes de repetir qualquer número. Isso é útil para produzir valores ou variações exclusivas, 
    mas há momentos em que é útil ter o mesmo conjunto de dados disponível para ser processado 
    de maneiras diferentes. Uma técnica é usar um programa para gerar valores aleatórios e 
    salvá-los para serem processados por uma etapa separada. Porém, isso pode não ser prático 
    para grandes quantidades de dados, então random inclui a função seed() para inicializar o 
    gerador pseudo-aleatório, de modo que produza um conjunto esperado de valores.
    
    O valor da seed controla o primeiro valor produzido pela fórmula usada para produzir números 
    pseudo-aleatórios e, como a fórmula é determinística, também define a sequência completa 
    produzida após a alteração da semente. O argumento para seed() pode ser qualquer objeto hash. 
    O padrão é usar uma fonte de aleatoriedade específica da plataforma, se houver uma disponível. 
    Caso contrário, a hora atual é usada.
"""

random.seed(2)
print(f'1 - seed: {random.random()}')

# random() gera números de ponto flutuante. É possível converter os resultados em números inteiros,
# mas usar randint() para gerar números inteiros diretamente é mais conveniente.
print(f'1 - randint: {random.randint(20, 30)}')

# randrange() é uma forma mais geral de selecionar valores de um intervalo.
print(f'1 - randrange: {random.randrange(10, 1000, 45)}')

# random inclui uma classe Random para gerenciar o estado interno de vários geradores de números aleatórios
random1 = random.Random()

print(f'2 - random: {random1.random()}')

seed = time.time()
random2 = random.Random(seed)

print(f'2 - random: {random2.random()}')

"""
    Alguns sistemas operacionais fornecem um gerador de números aleatórios que tem acesso a 
    mais fontes de entropia que podem ser introduzidas no gerador. random expõe esse recurso 
    por meio da classe SystemRandom, que tem a mesma API que Random, mas usa os.urandom() para 
    gerar os valores que formam a base de todos os outros algoritmos.
"""
random3 = random.SystemRandom()

print(f'3 - random: {random3.random()}')

seed = time.time()
random4 = random.SystemRandom(seed)

print('4 - random: {random4.random()}')
