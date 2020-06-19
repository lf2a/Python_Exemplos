import base64

url = b'\xff\xff'

# Codifica objetos do tipo bytes usando o alfabeto seguro para o sistema de arquivos e URLs,
# que substitui '+' por '-' e '/' por '_' no alfabeto Base64 padrão e retorna os bytes codificados.
saida_cod = base64.urlsafe_b64encode(url)
print(f'codificado:\t{url}\t{saida_cod}')

# Decodifica o objeto do tipo bytes ou uma sequência de caracteres ASCII usando o alfabeto
# seguro para sistemas de arquivos e URLs, que substitui '+' por '-' e '/' por '_' no alfabeto
# Base64 padrão e retorna os bytes decodificados.
saida_ori = base64.urlsafe_b64decode(saida_cod)
print(f'decodificado:\t{url}\t{saida_ori}')
