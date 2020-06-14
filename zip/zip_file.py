import zipfile
import os
import datetime


def create():
    '''criar arquivo zip com os arquivos 'test/index.html' e 'test/index.html'
    '''
    with zipfile.ZipFile('arquivo.zip', 'w') as z:
        z.write('test/index.html')
        z.write('test/style.css')


def create_dir():
    with zipfile.ZipFile('arquivo2.zip', 'w') as z:
        # itera sobre todos os arquivos e diretorios
        for folderName, _, filenames in os.walk('../tests'):
            for filename in filenames:
                filePath = os.path.join(folderName, filename)
                z.write(filePath)


if __name__ == '__main__':
    zf = zipfile.ZipFile('arquivo.zip', 'r')
    print(zf.namelist())  # lista os arquivos detro de 'arquivo.zip'

    for filename in zf.namelist():
        try:
            data = zf.read(filename)
        except KeyError:
            print('ERROR: Did not find %s in zip file' % filename)
        else:
            print(f'{filename}:\t{data}') # nome do arquivo: seu conteudo
    print('')

    for info in zf.infolist():
        print(f'\n{info.filename} -> info')
        print('\tComment:\t', info.comment)
        print('\tModified:\t', datetime.datetime(*info.date_time))
        print('\tSystem:\t\t', info.create_system, '(0 = Windows, 3 = Unix)')
        print('\tZIP version:\t', info.create_version)
        print('\tCompressed:\t', info.compress_size, 'bytes')
        print('\tUncompressed:\t', info.file_size, 'bytes')

    create()
    create_dir()
