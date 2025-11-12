from controllers.produto_controller import ProdutoController
from controllers.auth_controller import AuthController
from views.menu_view import MenuView
from views.produto_view import ProdutoView
from services.validacao_service import ValidacaoService
from utils.helpers import Helpers
import json
import os

class MainController:
    def __init__(self):
        self.produto_controller = ProdutoController()
        self.auth_controller = AuthController()
    
    def executar(self):
        Helpers.limpar_tela()
        print("=" * 30)
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
        Helpers.limpar_tela()
        print("🛒 LOJA ONLINE")
        print("=" * 40)
        
        produtos = self.produto_controller.listar_produtos()
        if not produtos:
            print("Nenhum produto disponível no momento.")
            input("\nPressione Enter para voltar...")
            return
        
        ProdutoView.mostrar_produtos(produtos)
        
        print("\nOpções:")
        print("  (1) Comprar produto")
        print("  (2) Voltar")
        
        try:
            opcao = ValidacaoService.validar_inteiro("\nOpção: ")
            if opcao == 1:
                self.comprar_produto()
        except KeyboardInterrupt:
            pass
        
        input("\nPressione Enter para voltar...")

    def comprar_produto(self):
        """Fluxo simplificado de compra"""
        nome_produto = input("\nNome do produto que deseja comprar: ").strip().lower()
        produto = self.produto_controller.buscar_produto_por_nome(nome_produto)
        
        if not produto:
            print(f"\n{ValidacaoService.RED}❌ Produto não encontrado!{ValidacaoService.RESET}")
            return
        
        if produto.quantidade <= 0:
            print(f"\n{ValidacaoService.RED}❌ Produto fora de estoque!{ValidacaoService.RESET}")
            return
        
        print(f"\nProduto: {produto.nome}")
        print(f"Estoque: {produto.quantidade}")
        print(f"Valor: R$ {produto.valor:.2f}")
        
        try:
            quantidade = ValidacaoService.validar_inteiro("\nQuantidade: ")
            
            if quantidade <= 0:
                print(f"\n{ValidacaoService.RED}❌ Quantidade inválida!{ValidacaoService.RESET}")
                return
            
            if quantidade > produto.quantidade:
                print(f"\n{ValidacaoService.RED}❌ Quantidade maior que estoque disponível!{ValidacaoService.RESET}")
                return
            
            valor_total = quantidade * produto.valor
            print(f"\n💳 Valor total: R$ {valor_total:.2f}")
            
            confirmar = input("\nConfirmar compra? (s/n): ").lower()
            if confirmar == 's':
                if self.produto_controller.atualizar_estoque(produto.nome, quantidade):
                    print("\n✅ Compra realizada com sucesso!")
                else:
                    print(f"\n{ValidacaoService.RED}❌ Erro ao processar compra!{ValidacaoService.RESET}")
            else:
                print("Compra cancelada.")
                
        except KeyboardInterrupt:
            print("\nCompra cancelada.")
    
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
                    input("Pressione Enter para continuar...")
    
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
        Helpers.limpar_tela()
        print("📊 RELATÓRIO DE VENDAS")
        print("=" * 50)
        
        # Carregar dados de vendas
        vendas_dia = self.carregar_vendas("data/Estoque/Vendas/vendas_dia.json")
        vendas_semana = self.carregar_vendas("data/Estoque/Vendas/vendas_semana.json") 
        vendas_mes = self.carregar_vendas("data/Estoque/Vendas/vendas_mes.json")
        
        while True:
            print("\n" + "=" * 40)
            print("       RELATÓRIOS DISPONÍVEIS")
            print("=" * 40)
            print("  (1) VENDAS DO DIA")
            print("  (2) VENDAS DA SEMANA")
            print("  (3) VENDAS DO MÊS")
            print("  (4) RESUMO GERAL")
            print("  (5) VOLTAR")
            print("=" * 40)
            
            try:
                opcao = ValidacaoService.validar_inteiro("\nOpção: ")
            except KeyboardInterrupt:
                break
            
            match opcao:
                case 1:
                    self.mostrar_relatorio(vendas_dia, "VENDAS DO DIA")
                case 2:
                    self.mostrar_relatorio(vendas_semana, "VENDAS DA SEMANA")
                case 3:
                    self.mostrar_relatorio(vendas_mes, "VENDAS DO MÊS")
                case 4:
                    self.mostrar_resumo_geral(vendas_dia, vendas_semana, vendas_mes)
                case 5:
                    break
                case _:
                    print(f"\n{ValidacaoService.RED}Opção inválida!{ValidacaoService.RESET}")

    def carregar_vendas(self, caminho: str):
        """Carrega dados de vendas do arquivo JSON"""
        try:
            with open(caminho, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def mostrar_relatorio(self, vendas, titulo: str):
        """Mostra relatório específico de vendas"""
        Helpers.limpar_tela()
        print(f"📊 {titulo}")
        print("=" * 50)
        
        if not vendas:
            print("\n📭 Nenhuma venda registrada neste período.")
            input("\nPressione Enter para continuar...")
            return
        
        total_vendas = 0
        total_quantidade = 0
        
        print(f"\n{'PRODUTO':<20} {'QTD':<8} {'VALOR UNIT':<12} {'TOTAL':<12}")
        print("-" * 55)
        
        for venda in vendas:
            if isinstance(venda, dict):
                nome = venda.get('nome', 'Desconhecido')
                quantidade = venda.get('quantidade', 0)
                valor_unit = venda.get('valor', 0)
                
                # Se o valor for total da venda, calcular unitário
                if quantidade > 0:
                    valor_unitario = valor_unit / quantidade
                else:
                    valor_unitario = valor_unit
                    
                valor_total = valor_unit
                total_vendas += valor_total
                total_quantidade += quantidade
                
                print(f"{nome:<20} {quantidade:<8} R$ {valor_unitario:<9.2f} R$ {valor_total:<9.2f}")
        
        print("-" * 55)
        print(f"{'TOTAL':<20} {total_quantidade:<8} {'':<12} R$ {total_vendas:<9.2f}")
        
        print(f"\n📈 Resumo:")
        print(f"   • Total de vendas: R$ {total_vendas:,.2f}")
        print(f"   • Quantidade de itens: {total_quantidade}")
        print(f"   • Ticket médio: R$ {total_vendas/max(total_quantidade, 1):.2f}")
        
        input("\nPressione Enter para continuar...")

    def mostrar_resumo_geral(self, vendas_dia, vendas_semana, vendas_mes):
        """Mostra resumo geral de todos os períodos"""
        Helpers.limpar_tela()
        print("📈 RESUMO GERAL DE VENDAS")
        print("=" * 50)
        
        def calcular_total(vendas):
            total = 0
            for venda in vendas:
                if isinstance(venda, dict):
                    total += venda.get('valor', 0)
            return total
        
        total_dia = calcular_total(vendas_dia)
        total_semana = calcular_total(vendas_semana)
        total_mes = calcular_total(vendas_mes)
        
        print(f"\n📅 VENDAS DO DIA:     R$ {total_dia:>10,.2f}")
        print(f"📅 VENDAS DA SEMANA: R$ {total_semana:>10,.2f}")
        print(f"📅 VENDAS DO MÊS:    R$ {total_mes:>10,.2f}")
        print("-" * 40)
        print(f"💰 TOTAL ACUMULADO:  R$ {(total_dia + total_semana + total_mes):>10,.2f}")
        
        # Estatísticas adicionais
        print(f"\n📊 Estatísticas:")
        print(f"   • Média diária:    R$ {total_mes/30:>10,.2f}")
        print(f"   • Projeção mensal: R$ {total_semana * 4:>10,.2f}")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    app = MainController()
    app.executar()