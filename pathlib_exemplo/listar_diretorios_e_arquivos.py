from pathlib import Path


def mostrar(p: Path):
    # iterdir(): retorna um generator que contem todos os diretorios e arquivos
    for item in p.iterdir():
        if item.is_dir():
            print(f'diretorio:\t{item}')
        elif item.is_file():
            print(f'arquivo:\t{item}')


p = Path('.')
mostrar(p)
