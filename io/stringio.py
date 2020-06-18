import io

""" StringIO
    Um fluxo na memória para E/S de texto. 
    O buffer de texto é descartado quando o método close () é chamado.
    
    O valor inicial do buffer pode ser definido, fornecendo o valor inicial `StringIO(valor)`. 
    Se a tradução de nova linha estiver ativada, as novas linhas serão codificadas como se fossem `write()`. 
    O fluxo é posicionado no início do buffer.
"""

strio = io.StringIO()
strio.write('Luiz\n')
strio.write('Filipy')

# getvalue(): Retorna um str contendo todo_ o conteúdo do buffer.
#  As novas linhas são decodificadas como se fossem `read()`, embora a posição do fluxo não seja alterada.
conteudo = strio.getvalue()
print(conteudo)

# close(): Fecha o objeto e descarta o buffer da memória
strio.close()
