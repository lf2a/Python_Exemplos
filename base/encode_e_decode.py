"""
    Este módulo fornece funções para codificar dados binários em caracteres ASCII
    imprimíveis e decodificar essas codificações de volta para dados binários.
"""

import base64

texto = b'Luiz Filipy Brasil 99'

# Codifica os objetos do tipo bytes usando Base64 e retorna os bytes codificados.
b64 = base64.b64encode(texto)
print(f'codificado:\t{texto}\t{b64}')

# Decodifica o objeto bytes codificado em Base64 ou a string ASCII e retorna os bytes decodificados.
original = base64.b64decode(b64)
print(f'decodificado:\t{texto}\t{original}')
