class ProdutoView:
    @staticmethod
    def mostrar_produtos(produtos):
        print("\n" + "="*50)
        print("                PRODUTOS")
        print("="*50)
        for i, produto in enumerate(produtos):
            print(f"  {i:2d}. {produto.nome:15} | Estoque: {produto.quantidade:4} | R$ {produto.valor:8.2f}")
        print("="*50)
    
    @staticmethod
    def mostrar_produto(produto, indice=None):
        if indice is not None:
            print(f"\nProduto {indice}:")
        print(f"  Nome: {produto.nome}")
        print(f"  Quantidade: {produto.quantidade}")
        print(f"  Valor: R$ {produto.valor:.2f}")