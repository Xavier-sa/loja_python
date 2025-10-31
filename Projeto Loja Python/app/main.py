from controllers.produto_controller import ProdutoController
from controllers.auth_controller import AuthController
from views.menu_view import MenuView
from views.produto_view import ProdutoView
from services.validacao_service import ValidacaoService
from utils.helpers import Helpers

class MainController:
    def __init__(self):
        self.produto_controller = ProdutoController()
        self.auth_controller = AuthController()
    
    def executar(self):
        Helpers.limpar_tela()
        print("🛒 SISTEMA LOJA PYTHON")
        print("=" * 30)
        
        while True:
            MenuView.mostrar_menu_principal()
            
            try:
                opcao = ValidacaoService.validar_inteiro("\nOpção: ")
            except KeyboardInterrupt:
                print("\n\nSaindo do sistema...")
                break
            
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
                    print(f"\n{ValidacaoService.RED}Opção inválida!{ValidacaoService.RESET}")
    
    def acessar_loja(self):
        print("\n🎁 ACESSANDO LOJA...")
        # Implementação simplificada para demonstração
        produtos = self.produto_controller.listar_produtos()
        ProdutoView.mostrar_produtos(produtos)
        input("\nPressione Enter para voltar...")
    
    def login_cadastro(self):
        while True:
            Helpers.limpar_tela()
            print("🔐 LOGIN / CADASTRO")
            print("=" * 30)
            MenuView.mostrar_menu_login()
            
            try:
                opcao = ValidacaoService.validar_inteiro("\nOpção: ")
            except KeyboardInterrupt:
                break
            
            match opcao:
                case 1:
                    self.login_cliente()
                    input("\nPressione Enter para voltar...")
                case 2:
                    self.cadastrar_cliente()
                    input("\nPressione Enter para voltar...")
                case 3:
                    break
                case _:
                    print(f"\n{ValidacaoService.RED}Opção inválida!{ValidacaoService.RESET}")
                    input("Pressione Enter para continuar...")        while True:
                MenuView.mostrar_menu_login()
                opcao = ValidacaoService.validar_inteiro("\nOpção: ")
                
                match opcao:
                    case 1:
                        self.login_cliente()
                    case 2:
                        self.cadastrar_cliente()
                    case 3:
                        break
                    case _:
                        print(f"\n{ValidacaoService.RED}Opção inválida!{ValidacaoService.RESET}")
    
    def login_cliente(self):
        print("\n--- LOGIN CLIENTE ---")
        email = ValidacaoService.validar_email("Email: ")
        senha = ValidacaoService.get_password_masked("Senha: ")
        
        if self.auth_controller.autenticar_cliente(email, senha):
            print("\n✅ Login efetuado com sucesso!")
        else:
            print(f"\n{ValidacaoService.RED}❌ Email ou senha incorretos!{ValidacaoService.RESET}")
    
    def cadastrar_cliente(self):
        print("\n--- CADASTRO CLIENTE ---")
        nome = ValidacaoService.validar_texto("Nome: ")
        sobrenome = ValidacaoService.validar_texto("Sobrenome: ")
        email = ValidacaoService.validar_email("Email: ")
        senha, _ = ValidacaoService.confirmar_senha()
        
        cliente_data = {
            "nome": nome,
            "sobrenome": sobrenome,
            "email": email,
            "senha": senha
        }
        
        if self.auth_controller.cadastrar_cliente(cliente_data):
            print("\n✅ Cadastro realizado com sucesso!")
        else:
            print(f"\n{ValidacaoService.RED}❌ Erro ao cadastrar cliente!{ValidacaoService.RESET}")
    
    def menu_gerente(self):
        if not self.auth_controller.autenticar_gerente():
            return
        
        print("\n🔧 MODO GERENTE ATIVADO")
        
        while True:
            MenuView.mostrar_menu_gerente()
            
            try:
                opcao = ValidacaoService.validar_inteiro("\nOpção: ")
            except KeyboardInterrupt:
                break
            
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
                    print(f"\n{ValidacaoService.RED}Opção inválida!{ValidacaoService.RESET}")
    
    def cadastrar_produto(self):
        print("\n--- CADASTRAR PRODUTO ---")
        nome = ValidacaoService.validar_texto("Nome do produto: ")
        quantidade = ValidacaoService.validar_inteiro("Quantidade: ")
        valor = ValidacaoService.validar_numero("Valor: R$ ")
        
        if self.produto_controller.adicionar_produto(nome, quantidade, valor):
            print("\n✅ Produto cadastrado com sucesso!")
        else:
            print(f"\n{ValidacaoService.RED}❌ Erro ao cadastrar produto!{ValidacaoService.RESET}")
    
    def editar_produto(self):
        produtos = self.produto_controller.listar_produtos()
        if not produtos:
            print("\nNenhum produto cadastrado!")
            return
        
        ProdutoView.mostrar_produtos(produtos)
        indice = ValidacaoService.validar_inteiro("\nÍndice do produto a editar: ")
        
        if 0 <= indice < len(produtos):
            self.submenu_edicao_produto(indice)
        else:
            print(f"\n{ValidacaoService.RED}Índice inválido!{ValidacaoService.RESET}")
    
    def submenu_edicao_produto(self, indice: int):
        produto = self.produto_controller.listar_produtos()[indice]
        
        while True:
            ProdutoView.mostrar_produto(produto, indice)
            MenuView.mostrar_submenu_edicao()
            
            opcao = ValidacaoService.validar_inteiro("\nOpção: ")
            
            match opcao:
                case 1:
                    novo_nome = ValidacaoService.validar_texto("Novo nome: ")
                    if self.produto_controller.atualizar_produto(indice, nome=novo_nome):
                        print("✅ Nome atualizado!")
                case 2:
                    novo_valor = ValidacaoService.validar_numero("Novo valor: R$ ")
                    if self.produto_controller.atualizar_produto(indice, valor=novo_valor):
                        print("✅ Valor atualizado!")
                case 3:
                    nova_quantidade = ValidacaoService.validar_inteiro("Nova quantidade: ")
                    if self.produto_controller.atualizar_produto(indice, quantidade=nova_quantidade):
                        print("✅ Quantidade atualizada!")
                case 4:
                    break
                case _:
                    print(f"\n{ValidacaoService.RED}Opção inválida!{ValidacaoService.RESET}")
    
    def excluir_produto(self):
        produtos = self.produto_controller.listar_produtos()
        if not produtos:
            print("\nNenhum produto cadastrado!")
            return
        
        ProdutoView.mostrar_produtos(produtos)
        indice = ValidacaoService.validar_inteiro("\nÍndice do produto a excluir: ")
        
        if 0 <= indice < len(produtos):
            produto = produtos[indice]
            confirmar = input(f"Confirma exclusão de '{produto.nome}'? (s/n): ").lower()
            
            if confirmar == 's':
                if self.produto_controller.remover_produto(indice):
                    print("✅ Produto excluído com sucesso!")
                else:
                    print(f"\n{ValidacaoService.RED}❌ Erro ao excluir produto!{ValidacaoService.RESET}")
            else:
                print("Exclusão cancelada.")
        else:
            print(f"\n{ValidacaoService.RED}Índice inválido!{ValidacaoService.RESET}")
    
    def listar_produtos(self):
        produtos = self.produto_controller.listar_produtos()
        if produtos:
            ProdutoView.mostrar_produtos(produtos)
        else:
            print("\nNenhum produto cadastrado!")
        input("\nPressione Enter para voltar...")
    
    def relatorio_vendas(self):
        print("\n--- RELATÓRIO DE VENDAS ---")
        print("Funcionalidade em desenvolvimento...")
        # Implementar relatórios baseados nos arquivos JSON existentes
        input("\nPressione Enter para voltar...")

if __name__ == "__main__":
    app = MainController()
    app.executar()