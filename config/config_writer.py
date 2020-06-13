import sys
import configparser

parser = configparser.ConfigParser()

parser.add_section('test')

# set(sessao, chave, valor)
parser.set('test', 'url', 'http://localhost:80/test')
parser.set('test', 'debug', 'True')

# mostrando a configuração
parser.write(sys.stdout)

# escrevendo as configurações em um arquivo chamado 'config_writer.ini'
with open('config_writer.ini', 'w') as ini_file:
    parser.write(ini_file)
