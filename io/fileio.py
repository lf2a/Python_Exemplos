import io

"""
    FileIO representa um arquivo no nível do SO que contém dados de bytes. 
    Ele implementa a interface RawIOBase (e, portanto, a interface IOBase também).
    
    O modo pode ser 'r', 'w', 'x' ou 'a' para leitura (padrão), gravação, criação exclusiva ou anexação.
"""

with io.FileIO(file='file.io', mode='w') as w:
    w.write(b'Luiz Filipy')
