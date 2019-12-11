import zipfile
import os
import datetime


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
    zf = zipfile.ZipFile('arquivo.zip', 'r')
    print(zf.namelist())
    for filename in zf.namelist():
        try:
            data = zf.read(filename)
            print(dir(zf))
        except KeyError:
            print ('ERROR: Did not find %s in zip file' % filename)
        else:
            print(filename, ':')
            print(repr(data))
        
    for info in zf.infolist():
        print(info.filename)
        print('\tComment:\t', info.comment)
        print('\tModified:\t', datetime.datetime(*info.date_time))
        print('\tSystem:\t\t', info.create_system, '(0 = Windows, 3 = Unix)')
        print('\tZIP version:\t', info.create_version)
        print('\tCompressed:\t', info.compress_size, 'bytes')
        print('\tUncompressed:\t', info.file_size, 'bytes')
    
    # create()
    create_dir()
    