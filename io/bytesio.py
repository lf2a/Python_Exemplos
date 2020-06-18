import io

""" io.BytesIO()
    Uma implementação de um stream usando um buffer de bytes na memória. Ele herda o BufferedIOBase. 
    O buffer é descartado quando o método `close()` é chamado.
"""
bio = io.BytesIO(b'Luiz Filipy')

# getbuffer(): Retorna uma exibição legível e gravável sobre o conteúdo do buffer sem copiá-lo.
# Além disso, a mutação da exibição atualizará de forma transparente o conteúdo do buffer.
read_write_view = bio.getbuffer()
read_write_view[3:5] = b's_'  # irá substituir os conteudos do buffer (do indice 2 ao 4)

# read1(): Lê e retorna o tamanho de bytes. Se o argumento for omitido, Nenhum ou negativo, os dados serão
# lidos e retornados até que o EOF seja alcançado.
print(bio.read1(3))  # retorno -> b'Lui'
print(bio.read1(2))  # retorno -> b's_Filipy'

# getvalue(): irá retornar bytes que contêm todo_ o conteúdo do buffer.
print(bio.getvalue())  # retorno -> b'luiz_Filipy'

# readinto1(): Lê bytes em um objeto de tipo 'b' pré-alocado e gravável, e retorna o número de bytes lidos.
# Por exemplo, 'b' pode ser um bytearray.
tamanho: int = bio.readinto1(read_write_view)
print(tamanho)  # retorno -> 6
