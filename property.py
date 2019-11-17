class Pessoa():
    def __init__(self, nome):
        self.__nome = nome
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise Exception('\'nome\' deve ser str')
            
    
if __name__ == '__main__':
    p = Pessoa('luiz fiilpy')
    
    print(p.nome)
    
    p.nome = 'filipy'
    print(p.nome)