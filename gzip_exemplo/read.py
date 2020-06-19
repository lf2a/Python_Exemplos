"""
    Este módulo fornece uma interface simples para compactar e descomprimir arquivos,
    exatamente como os programas GNU e gzip e gunzip.
"""

import gzip
import io

# open(): Abre um arquivo compactado com gzip no modo binário ou de texto, retornando um objeto de arquivo.
with gzip.open('gzip_exemplo/write.py-compress.gz', 'rb') as arquivo:
    # Um fluxo de texto em buffer sobre um fluxo binário BufferedIOBase.
    with io.TextIOWrapper(arquivo, encoding='utf-8') as buf:
        # Lê e retorna o máximo caracteres de tamanho do fluxo como uma única string.
        # Se o tamanho for negativo ou Nenhum, lê até EOF
        print(buf.read())
