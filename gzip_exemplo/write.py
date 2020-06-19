"""
    Este módulo fornece uma interface simples para compactar e descomprimir arquivos,
    exatamente como os programas GNU e gzip e gunzip.
"""

import gzip
import io
import os
import hashlib


def get_hash(data):
    return hashlib.md5(data).hexdigest()


# comprimindo este arquivo
data = open(__file__, 'r').read()
cksum = get_hash(data.encode('utf-8'))

print('STATUS\t\tNIVEL\t\tTAMANHO (bytes)\t\tCHECKSUM (md5)')
print('original\t#\t\t{}\t\t\t{}'.format((len(data)), cksum))

arquivo = __file__ + '-compress.gz'

# open(): Abre um arquivo compactado com gzip no modo binário ou de texto, retornando um objeto de arquivo.
# open(): O argumento `compresslevel` é um número inteiro de 0 a 9, como no construtor GzipFile.
with gzip.open(arquivo, 'wb', compresslevel=9) as arquivo_gz:
    # Um fluxo de texto em buffer sobre um fluxo binário BufferedIOBase.
    with io.TextIOWrapper(arquivo_gz, encoding='utf-8') as buf:
        # write(): Escreve a sequência 's' no fluxo e retorna o número de caracteres gravados.
        buf.write(data)

tamanho = os.stat(arquivo).st_size
cksum = get_hash(open(arquivo, 'rb').read())
print('comprimido\t{}\t\t{}\t\t\t{}'.format(9, tamanho, cksum))
