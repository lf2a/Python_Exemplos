def is_admin(func):
    def inner(data):
        if data['is_admin'] == True:
            return func(data)
        else:
            print('not admin')
            return
#            raise Exception('not admin')
    return inner

@is_admin
def home(data):
    print('data')
    

data = {
        'is_admin': False,
        'nome': 'luiz filipy',
        'idade': 19
}

home(data)