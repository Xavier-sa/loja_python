from dataclasses import dataclass

@dataclass
class Produto:
    nome: str
    quantidade: int
    valor: float
    
    def to_dict(self):
        return {
            "nome": self.nome,
            "quantidade": self.quantidade,
            "valor": self.valor
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            nome=data["nome"],
            quantidade=data["quantidade"],
            valor=data["valor"]
        )