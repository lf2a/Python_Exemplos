import io

"""
    Um buffer que fornece acesso de nível superior a um objeto RawIOBase sequencial e gravável. 
    Ele herda o BufferedIOBase. Ao gravar neste objeto, os dados são normalmente colocados em um buffer interno. 
    O buffer será gravado no objeto RawIOBase subjacente sob várias condições, incluindo:
    
    - Quando o buffer fica muito pequeno para todos os dados pendentes;
    - quando `flush()` é chamado;
    - quando uma `seek()` é solicitada (para objetos BufferedRandom);
    - quando o objeto BufferedWriter é fechado ou destruído.
    
    O construtor cria um BufferedWriter para o fluxo bruto gravável fornecido. 
    Se o buffer_size não for fornecido, o padrão será DEFAULT_BUFFER_SIZE.
"""

bio = io.BytesIO(b'Luiz Filipy')

bw = io.BufferedWriter(bio)

# flush(): Força os bytes mantidos no buffer no fluxo bruto.
# Um BlockingIOError deve ser gerado se o fluxo bruto bloquear.
bw.flush()

# write(): Escreve o objeto semelhante a bytes, 'b' e retorna o número de bytes gravados.
# Quando no modo sem bloqueio, um BlockingIOError é gerado se o buffer precisar ser gravado,
# com o fluxo bruto bloqueado.
tamanho_gravado = bw.write(b' Brasil 1234')
print(tamanho_gravado)

""" Exemplo 2, com arquivo (FileIO)"""
with io.FileIO(file='buffered_writer.io', mode='w') as fio:
    bw2 = io.BufferedWriter(fio)
    bw2.write(b'Luiz Filipy - Brasil 1234')
    bw2.flush()
