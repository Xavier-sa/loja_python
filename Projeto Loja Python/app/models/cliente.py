from dataclasses import dataclass

@dataclass
class Cliente:
    nome: str
    sobrenome: str
    email: str
    senha: str
    cpf: str = ""
    telefone: str = ""
    endereco: dict = None
    
    def to_dict(self):
        return {
            "nome": self.nome,
            "sobrenome": self.sobrenome,
            "email": self.email,
            "senha": self.senha,
            "cpf": self.cpf,
            "telefone": self.telefone,
            "endereco": self.endereco or {}
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            nome=data["nome"],
            sobrenome=data["sobrenome"],
            email=data["email"],
            senha=data["senha"],
            cpf=data.get("cpf", ""),
            telefone=data.get("telefone", ""),
            endereco=data.get("endereco", {})
        )