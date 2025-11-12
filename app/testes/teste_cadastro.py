import sys
sys.path.append('app')

def testar_cadastro():
    print("=== TESTANDO CADASTRO ===")
    
    try:
        from services.validacao_service import ValidacaoService
        
        # Testar métodos específicos do cadastro
        metodos = ['validar_email', 'validar_texto', 'confirmar_senha']
        
        for metodo in metodos:
            if hasattr(ValidacaoService, metodo):
                print(f"✅ {metodo} - DISPONÍVEL")
            else:
                print(f"❌ {metodo} - FALTANDO")
                
        # Teste rápido do fluxo
        print("\n🧪 Teste rápido:")
        nome = ValidacaoService.validar_texto("Nome (teste): ")
        print(f"✅ Nome válido: {nome}")
        
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    testar_cadastro()