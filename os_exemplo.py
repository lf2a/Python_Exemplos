import os

# Um objeto de mapeamento que representa as variaveis de ambiente.
print(os.environ)

# retorna o diretorio atual
print(os.getcwd())

# retorna uma variavel de ambiente
print(os.getenv('PATH'))

# retorna o processo atual
print(os.getpid())

# retorna o nome do login
print(os.getlogin())

# cria uma pasta
# os.mkdir('cria_pasta')

# apaga uma pasta vazia
# os.rmdir('apgar')
# para apagar uma pasta com conteudo use `shutil.rmtree()`

# altera o diretorio
# os.chdir('/')

# lista o diretorio atual
print(os.listdir())

# renomeia um arquivo ou diretorio
# os.rename('atual_nome', 'novo_nome')

# remove um arquivo
# os.remove('a')