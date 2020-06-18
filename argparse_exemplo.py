import argparse

"""
    O módulo argparse facilita a criação de interfaces de linha de comando fáceis de usar. 
    O programa define quais argumentos ele requer e o argparse descobrirá como analisá-los no `sys.argv`. 
    O módulo argparse também gera automaticamente mensagens de ajuda e uso e emite erros quando os usuários 
    fornecem argumentos inválidos ao programa.
"""

# O objeto ArgumentParser manterá todas as informações necessárias para analisar
# a linha de comando nos tipos de dados Python.
parser = argparse.ArgumentParser(description='Exemplo olá mundo.')

""" add_argument(): O preenchimento de um ArgumentParser com informações sobre os argumentos do programa 
é feito fazendo chamadas para o método add_argument (). 
Geralmente, essas chamadas dizem ao ArgumentParser como pegar as seqüências de 
caracteres na linha de comando e transformá-las em objetos. Esta informação é 
armazenada e usada quando parse_args () é chamado."""
# adicionando argumentos
parser.add_argument('valores', type=int, nargs='*', help='string para acumular os valores')
parser.version = '1.0'

parser.add_argument('-a', action='store')
parser.add_argument('-b', action='store_const', const=42)
parser.add_argument('-c', action='store_true')
parser.add_argument('-d', action='store_false')
parser.add_argument('-e', action='append')
parser.add_argument('-f', action='append_const', const=42)
parser.add_argument('-g', action='count')
parser.add_argument('-i', action='help')
parser.add_argument('-j', action='version')
parser.add_argument('-s', '--soma', dest='funcao', const=lambda x: print(sum(int(v) for v in x)), action='store',
                    type=int, nargs='?')

""" ArgumentParser analisa argumentos através do método `parse_args()`. 
    Isso inspecionará a linha de comando, converterá cada argumento no tipo apropriado e, 
    em seguida, chamará a ação apropriada.
"""
args = parser.parse_args()

print(vars(args))

# chamando a função 'lambda' e passando os valores para ela mostrar
args.funcao(args.valores)

# python argparse_exemplo.py 1 2 3 4 --soma -a 2 -b -c -d -e a -f -gg
# >>> {'valores': [1, 2, 3, 4], 'a': '2', 'b': 42, 'c': True, 'd': False, 'e': ['a'], 'f': [42], 'g': 2, 'funcao': <function <lambda> at 0x7f7e5084eb80>}
# 10
