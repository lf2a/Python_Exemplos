class NotFoundException(Exception):
    ''' not found excepetion '''
    pass

def find():
    nomes = ['luiz', 'Carla', 'Filipy', 'Ana']

    if 'José' in nomes:
        print('Encontrado')
    else:
        raise NotFoundException('Pessoa não encontrada')


try:
    find()
except NotFoundException as nfe:
#    print(nfe.with_traceback())
    print('Error: %s' % nfe)