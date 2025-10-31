from controllers.produto_controller import ProdutoController
from controllers.auth_controller import AuthController
from views.menu_view import MenuView
from services.validacao_service import ValidacaoService

class MainController:
    def __init__(self):
        self.produto_controller = ProdutoController()
        self.auth_controller = AuthController()
    
    def executar(self):
        while True:
            MenuView.mostrar_menu_principal()
            
            try:
                opcao = int(input("\nOpção: "))
            except ValueError:
                print("\nErro: Digite um número válido!")
                continue
            
            match opcao:
                case 1:
                    self.acessar_loja()
                case 2:
                    self.login_cadastro()
                case 3:
                    self.menu_gerente()
                case 0:
                    print("\nSaindo do sistema...")
                    break
                case _:
                    print("\nOpção inválida!")
    
    def acessar_loja(self):
        # Implementar fluxo da loja
        print("\nAcessando loja...")
    
    def login_cadastro(self):
        # Implementar fluxo de login/cadastro
        print("\nLogin/Cadastro...")
    
    def menu_gerente(self):
        if not self.auth_controller.autenticar_gerente():
            return
        
        while True:
            MenuView.mostrar_menu_gerente()
            
            try:
                opcao = int(input("\nOpção: "))
            except ValueError:
                print("\nErro: Digite um número válido!")
                continue
            
            match opcao:
                case 1:
                    self.cadastrar_produto()
                case 2:
                    self.editar_produto()
                case 3:
                    self.excluir_produto()
                case 4:
                    self.relatorio_vendas()
                case 5:
                    self.listar_produtos()
                case 6:
                    break
                case _:
                    print("\nOpção inválida!")
    
    def cadastrar_produto(self):
        print("\n--- CADASTRAR PRODUTO ---")
        nome = ValidacaoService.validar_texto("Nome do produto: ")
        quantidade = ValidacaoService.validar_numero("Quantidade: ", int)
        valor = ValidacaoService.validar_numero("Valor: R$ ")
        
        if self.produto_controller.adicionar_produto(nome, quantidade, valor):
            print("\nProduto cadastrado com sucesso!")
        else:
            print("\nErro ao cadastrar produto!")
    
    def listar_produtos(self):
        produtos = self.produto_controller.listar_produtos()
        print("\n--- LISTA DE PRODUTOS ---")
        for i, produto in enumerate(produtos):
            print(f"{i:2d}. {produto.nome:15} | Estoque: {produto.quantidade:4} | R$ {produto.valor:8.2f}")

if __name__ == "__main__":
    app = MainController()
    app.executar()