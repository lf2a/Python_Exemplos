import time


class Veiculo(object):
    """ Atributos que começam com '__' (self.__id) signifa que são 'privados' """

    def __init__(self, id, marca, modelo, preco, dono):
        """ metodo contrutor """
        self.__id = id  # atributo privado
        self.__marca = marca
        self.__modelo = modelo

        if isinstance(preco, float):
            self.__preco = preco  # private
        else:
            raise Exception('Precisa ser um valor decimal')

        self.dono = dono  # public

    def detalhes(self):
        print('ID: %s' % self.__id)
        print('Marca: %s' % self.__marca)
        print('Modelo: %s' % self.__modelo)
        print('Preco: %f.2' % self.__preco)
        print('Dono: %s' % self.dono)

    def ligar(self):
        pass

    def desligar(self):
        pass

    def __str__(self):
        return '%s' % self.__id


# herdando da super classe 'Veiculo'
class Carro(Veiculo):
    def __init__(self, id, marca, modelo, preco, portas, dono):
        self.__portas = portas
        # 'super().' serve para chamar metodos da classe pai ou super classe
        super().__init__(id=id, marca=marca, modelo=modelo, preco=preco, dono=dono)

    def detalhes(self):
        super().detalhes()
        print('Portas: %d\n' % self.__portas)

    def ligar(self):
        print('ligando motor pelo botão')
        time.sleep(4)
        print('Carro ligado.\n')

    def _iniciar_deligamento(self):
        """ este é um metodo 'privado' """
        print('iniciando desligamento')
        
    def desligar(self):
        self._iniciar_deligamento()
        print('desligando motor')
        time.sleep(4)
        print('Carro desligado.')


class Pessoa():
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso

    def __call__(self, *args, **kwargs):
        print('__call__')

    def __add__(self, x):
        return self.peso + x.peso

    def __sub__(self, x):
        return self.peso - x.peso

    def __mul__(self, x):
        return self.peso * x.peso

    def __pow__(self, x):
        return self.peso ** x.peso

    def __truediv__(self, x):
        return self.peso / x.peso

    def __floordiv__(self, x):
        return self.peso // x.peso

    def __mod__(self, x):
        return self.peso % x.peso

    def __lshift__(self, x):
        return self.peso << x.peso

    def __rshift__(self, x):
        return self.peso >> x.peso

    def __and__(self, x):
        return self.peso & x.peso

    def __or__(self, x):
        return self.peso | x.peso

    def __xor__(self, x):
        return self.peso ^ x.peso

    def __invert__(self):
        return ~self.peso

    def __lt__(self, x):
        return self.peso < x.peso

    def __le__(self, x):
        return self.peso <= x.peso

    def __eq__(self, x):
        return self.peso == x.peso

    def __ne__(self, x):
        return self.peso != x.peso

    def __gt__(self, x):
        return self.peso > x.peso

    def __ge__(self, x):
        return self.peso >= x.peso

    def __del__(self):
        print('destructor')

    def __str__(self):
        """ representando a instance da classe em forma de string """
        return f'{self.nome} - {self.idade} - {self.peso}'

    def show(self):
        pass


if __name__ == '__main__':
    v_1 = Veiculo(
        id='verhj3',
        marca='Pagani',
        modelo='Huayra',
        preco=1500000.00,
        dono='Luiz Filipy'
    )

    print('id: %s\n' % v_1)
    v_1.detalhes()
    c_1 = Carro(id='verhj3', marca='Pagani', modelo='Huayra', preco=1500000.00, dono='Luiz Filipy', portas=4)
    c_1.__portas = 10
    c_1.detalhes()
    c_1.ligar()
    c_1._iniciar_deligamento() # apesar de ser 'privado' ainda é possivel que seja acessado
    c_1.desligar()

    p1 = Pessoa(nome='luiz filipy', idade=19, peso=56)
    p2 = Pessoa(nome='Ans Carla', idade=34, peso=78)

    p1()
    p2()

    print(p1 + p2)
    print(p1 - p2)
    print(p1 * p2)
    print(p1 ** p2)
    print(p1 / p2)
    print(p1 // p2)
    print(p1 % p2)
    print(p1 << p2)
    print(p1 >> p2)
    print(p1 & p2)
    print(p1 | p2)
    print(p1 ^ p2)
    print(~p1)
    print(p1 < p2)
    print(p1 <= p2)
    print(p1 == p1)
    print(p1 != p2)
    print(p1 > p2)
    print(p1 >= p2)

    print(p1)
    print(p1)

    del p1
    del p2
