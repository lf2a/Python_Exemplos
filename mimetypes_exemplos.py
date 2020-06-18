import mimetypes

# Lista de nomes de arquivos de mapas de tipos comumente instalados.
print(mimetypes.knownfiles)

# Sufixos de mapeamento de dicionário para sufixos.
print(mimetypes.suffix_map)

# Dicionário mapeando extensões de nome de arquivo para tipos de codificação
print(mimetypes.encodings_map)

# Dicionário mapeando extensões de nome de arquivo para tipos MIME.
print(mimetypes.types_map)

# Dicionário mapeando extensões de nome de arquivo para tipos MIME não padrão, mas comumente encontrados.
print(mimetypes.common_types)
