from models.produto import Produto
from services.json_service import JSONService
from services.validacao_service import ValidacaoService

class ProdutoController:
    CAMINHO_PRODUTOS = "data/Estoque/Produtos/produtos.json"
    
    def __init__(self):
        self.produtos = self.carregar_produtos()
    
    def carregar_produtos(self) -> list[Produto]:
        dados = JSONService.carregar_dados(self.CAMINHO_PRODUTOS)
        return [Produto.from_dict(item) for item in dados]
    
    def salvar_produtos(self) -> bool:
        dados = [produto.to_dict() for produto in self.produtos]
        return JSONService.salvar_dados(self.CAMINHO_PRODUTOS, dados)
    
    def listar_produtos(self) -> list[Produto]:
        return self.produtos
    
    def adicionar_produto(self, nome: str, quantidade: int, valor: float) -> bool:
        novo_produto = Produto(nome, quantidade, valor)
        self.produtos.append(novo_produto)
        return self.salvar_produtos()
    
    def atualizar_produto(self, indice: int, **kwargs) -> bool:
        if 0 <= indice < len(self.produtos):
            for key, value in kwargs.items():
                if hasattr(self.produtos[indice], key):
                    setattr(self.produtos[indice], key, value)
            return self.salvar_produtos()
        return False
    
    def remover_produto(self, indice: int) -> bool:
        if 0 <= indice < len(self.produtos):
            self.produtos.pop(indice)
            return self.salvar_produtos()
        return False