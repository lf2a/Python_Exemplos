from abc import ABCMeta, abstractmethod


class Veiculo(metaclass=ABCMeta):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass


class Carro(Veiculo):
    def ligar(self):
        print('ligando')

    def desligar(self):
        print('desligando')


try:
    v = Veiculo()  # error
except TypeError as e:
    print(e)

c = Carro()
c.ligar()
c.desligar()
