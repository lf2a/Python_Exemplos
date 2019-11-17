class Pessoa():
    def __init__(self, primeiro_nome, segundo_nome, altura, peso):
        self.primeiro_nome = primeiro_nome
        self.segundo_nome = segundo_nome
        self.altura = altura
        self.peso = peso
    
    def full_name(self):
        return '%s %s' % (self.primeiro_nome, self.segundo_nome)
    
    def imc(self):
        if isinstance(self.peso, float) and isinstance(self.altura, float):
            imc = self.peso / (float(self.altura) * float(self.altura))
            return imc
        else:
            return None
        
