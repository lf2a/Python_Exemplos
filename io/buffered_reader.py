import io

"""
    Um buffer que fornece acesso de nível superior a um objeto RawIOBase sequencial e legível. 
    Ele herda o BufferedIOBase. Ao ler dados desse objeto, uma quantidade maior de dados pode ser 
    solicitada no fluxo bruto subjacente e mantida em um buffer interno.  Os dados em buffer podem 
    ser retornados diretamente nas leituras subsequentes.
    
    O construtor cria um BufferedReader para o fluxo bruto legível fornecido e buffer_size. 
    Se buffer_size for omitido, DEFAULT_BUFFER_SIZE será usado.
"""

bio = io.BytesIO(b'Luiz Filipy - Brasil 1234')

br = io.BufferedReader(bio)

# peek(): Retorna bytes do fluxo sem avançar a posição. No máximo, uma única leitura no fluxo bruto
# é feita para satisfazer a chamada. O número de bytes retornados pode ser menor ou maior que o solicitado.
print(br.peek())

# read(): Lê e retorna bytes da tamanho fornecido, ou se o tamanho não for fornecido ou negativo,
# até o EOF ou se a chamada de leitura bloquearia no modo sem bloqueio.
print(br.read(11))  # retorno: b'Luiz Filipy'

# read1(): Lâ e retorna o tamanho de bytes com apenas uma chamada no fluxo bruto.
# Se pelo menos um byte for armazenado em buffer, somente bytes em buffer serão retornados.
# Caso contrário, é feita uma chamada de leitura de fluxo bruto.
print(br.read1())  # retorno: b' - Brasil 1234'
