"""
    O módulo getpass fornece uma maneira portátil de lidar com tais solicitações de senha com segurança.
"""

import getpass
import sys

try:
    # A função getpass() imprime um prompt e lê a entrada do usuário até que pressione Enter.
    # Usar o sys.stderr para o prompt significa que a saída padrão pode ser redirecionada
    # (para um canal ou arquivo) sem ver o prompt da senha. O valor digitado pelo usuário ainda
    # não é repetido na tela.
    # python3 getpass_exemplo.py > /home/luiz/teste.txt
    p = getpass.getpass(prompt='Digite sua senha: ', stream=sys.stderr)
except KeyboardInterrupt:
    print('\nSaindo...')
else:
    print(f'Sua senha é: {p}')

"""
    No Unix, getpass() sempre exige um tty que possa controlar via termios, para que o eco da 
    entrada possa ser desativado. Isso significa que os valores não serão lidos de um fluxo não 
    terminal redirecionado para a entrada padrão. Em vez disso, o getpass tenta acessar o tty de 
    um processo e nenhum erro é gerado se eles puderem acessá-lo.
"""

# Cabe ao chamador detectar quando o fluxo de entrada não é um tty e usar um método alternativo
# para leitura nesse caso.
if sys.stdin.isatty():
    p = getpass.getpass('Usando getpass: ')
else:
    print('Usando readline')
    p = sys.stdin.readline().rstrip()

print(f'Read: {p}')

#  echo "luiz" | python3 getpass_exemplo.py
# para testar o readline (sem o tty)
