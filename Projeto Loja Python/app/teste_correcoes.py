import sys
import os

# Adiciona a pasta app para procurar os metodos/funcoes necessarios
sys.path.append('app')

def testar_produto_controller():
    print("=== TESTANDO PRODUTOCONTROLLER ===")
    try:
        from controllers.produto_controller import ProdutoController
        
        controller = ProdutoController()
        
        # Testar métodos
        metodos_necessarios = [
            'atualizar_estoque',
            'buscar_produto_por_nome', 
            'listar_produtos',
            'adicionar_produto'
        ]
        
        for metodo in metodos_necessarios:
            if hasattr(controller, metodo):
                print(f"✅ {metodo} - EXISTE")
            else:
                print(f"❌ {metodo} - FALTANDO")
                
    except Exception as e:
        print(f"❌ Erro: {e}")

def testar_login_gerente():
    print("\n=== TESTANDO LOGIN GERENTE ===")
    caminho = "data/log/login_gerente.json"
    
    if os.path.exists(caminho):
        print(f"✅ Arquivo encontrado: {caminho}")
        try:
            import json
            with open(caminho, 'r') as f:
                dados = json.load(f)
                print(f"✅ Email: {dados.get('email')}")
                print(f"✅ Senha: {'*' * len(dados.get('senha', ''))}")
        except Exception as e:
            print(f"❌ Erro ao ler: {e}")
    else:
        print(f"❌ Arquivo NÃO encontrado: {caminho}")

if __name__ == "__main__":
    testar_produto_controller()
    testar_login_gerente()