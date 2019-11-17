from abc import ABCMeta, abstractmethod

class Veiculo(metaclass=ABCMeta):
    
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

#v = Veiculo() # error