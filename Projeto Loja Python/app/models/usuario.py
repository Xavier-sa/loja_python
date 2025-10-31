from dataclasses import dataclass

@dataclass
class Usuario:
    email: str
    senha: str
    nome: str = ""
    
    def to_dict(self):
        return {
            "email": self.email,
            "senha": self.senha,
            "nome": self.nome
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            email=data["email"],
            senha=data["senha"],
            nome=data.get("nome", "")
        )