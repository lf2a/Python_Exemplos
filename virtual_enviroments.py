import os

# definindo uma variavel de ambiente
os.environ['TEST'] = 'test environ'

# visualizando uma variavel de ambiente
test = os.getenv('TEST')
print(test)

# outra forma de visualizar uma variavel de ambiente
print(os.getenv('TEST'))

# excluir variavel de ambiente
del os.environ['TEST']
