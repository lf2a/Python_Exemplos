from configparser import ConfigParser
from sys import stdout

parser = ConfigParser()

parser.add_section('test')
parser.set('test', 'url', 'http://localhost:80/test')
parser.set('test', 'debug', 'True')

parser.write(stdout)