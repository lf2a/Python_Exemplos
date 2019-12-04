import zipfile
import os


def create():
    '''criar arquivo zip com os arquivos 'data.csv' e 'lorem.txt'
    '''
    with zipfile.ZipFile('arquivo.zip', 'w') as z:
        z.write('data.csv')
        z.write('lorem.txt')


def create_dir():
    with zipfile.ZipFile('arquivo2.zip', 'w') as z:
        # itera sobre todos os arquivos se diretorios
        for folderName, _, filenames in os.walk('stock_price'):
            for filename in filenames:
                filePath = os.path.join(folderName, filename)
                z.write(filePath)


if __name__ == '__main__':
    # create()
    create_dir()