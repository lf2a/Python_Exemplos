import shutil
import os

# junta as string para formar um caminho de um diretorio
print(os.path.join('home', 'luiz'))

# retorna o caminho do diretorio atual
print(os.getcwd())

# cria um novo diretorio
os.mkdir('new_dir')
# lista todos os diretorios e arquivos neste diretorio e retorna uma lista
print(os.listdir())

# renomeia um diretorio
os.rename('new_dir', 'r_new_dir')
print(os.listdir())

os.remove('test.txt')  # remove um arquivo
print(os.listdir())

os.rmdir('r_new_dir')  # remove um diretorio
print(os.listdir())

# troca de diretorio
os.chdir('/home')
print(os.getcwd())

# remove um diretorio recursivamente
shutil.rmtree('example')
print(os.listdir())
