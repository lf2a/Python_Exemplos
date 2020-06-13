from typing import Optional


class Pessoa():
    def __init__(self, primeiro_nome: str, segundo_nome: str, altura: float, peso: float) -> None:
        self.primeiro_nome: str = primeiro_nome
        self.segundo_nome: str = segundo_nome
        self.altura: float = altura
        self.peso: float = peso

    def full_name(self) -> str:
        return '%s %s' % (self.primeiro_nome, self.segundo_nome)

    def imc(self) -> Optional[float]:
        if isinstance(self.peso, float) and isinstance(self.altura, float):
            imc = self.peso / (float(self.altura) * float(self.altura))
            return imc
        else:
            return None
