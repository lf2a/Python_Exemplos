import configparser

parser = configparser.ConfigParser()
parser.read('config_reader.ini', encoding='utf-8')

print('dev debug: %s\n' % parser.get('dev', 'debug'))

print('prod debug: %s' % parser.get('prod', 'debug'))

print('prod password: %s' % parser.get('prod', 'password'))
print('prod password (utf-8): %s' % parser.get('prod', 'password').encode('utf-8'))
