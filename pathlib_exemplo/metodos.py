from pathlib import Path

# cwd(): Retorna um novo objeto de caminho que representa o diretório atual
print(Path.cwd())

# home(): Retorna um novo objeto de caminho que representa o diretório inicial do usuário
print(Path.home())

p = Path('.gitignore')
# stat(): Retorna um objeto os.stat_result que contém informações sobre este caminho
print(p.stat())

# Muda o modo de arquivo e as permissões, igual `os.chmod()`:
# p.chmod(modo)

# exists(): verifica se o arquivo ou diretorio existe
print(p.exists())
