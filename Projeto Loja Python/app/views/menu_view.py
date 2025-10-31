class MenuView:
    @staticmethod
    def mostrar_menu_principal():
        print("\n" + "="*40)
        print("           MENU PRINCIPAL")
        print("="*40)
        print("  (1) ACESSAR LOJA")
        print("  (2) LOGIN / CADASTRO") 
        print("  (3) GERENTE")
        print("  (0) SAIR")
        print("="*40)
    
    @staticmethod
    def mostrar_menu_gerente():
        print("\n" + "="*40)
        print("           MENU GERENTE")
        print("="*40)
        print("  (1) CADASTRAR PRODUTO")
        print("  (2) EDITAR PRODUTO")
        print("  (3) EXCLUIR PRODUTO")
        print("  (4) RELATÓRIO DE VENDAS")
        print("  (5) LISTAR PRODUTOS")
        print("  (6) SAIR")
        print("="*40)
    
    @staticmethod
    def mostrar_submenu_edicao():
        print("\n" + "="*30)
        print("     SUBMENU EDIÇÃO")
        print("="*30)
        print("  (1) EDITAR NOME")
        print("  (2) EDITAR VALOR")
        print("  (3) EDITAR QUANTIDADE")
        print("  (4) VOLTAR")
        print("="*30)