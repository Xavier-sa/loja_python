from services.validacao_service import ValidacaoService
from services.json_service import JSONService
from models.usuario import Usuario

class AuthController:
    CAMINHO_LOGIN_GERENTE = "data/log/login_gerente.json"
    CAMINHO_CLIENTES = "data/Clientes/cadastro_cliente.json"
    CAMINHO_LOG_CLIENTE = "data/log/log_cliente.json"
    
    def autenticar_gerente(self) -> bool:
        """Autentica usuário gerente"""
        print("\n--- LOGIN GERENTE ---")
        
        try:
            credenciais = JSONService.carregar_dados(self.CAMINHO_LOGIN_GERENTE)
            if not credenciais:
                print("Erro: Credenciais de administrador não encontradas!")
                return False
            
            email = input("Email: ")
            senha = ValidacaoService.get_password_masked("Senha: ")
            
            if email == credenciais.get("email") and senha == credenciais.get("senha"):
                print("\nBem-vindo! Login efetuado com sucesso.")
                return True
            else:
                print("\nErro: Email ou senha incorretos!")
                return False
                
        except Exception as e:
            print(f"\nErro durante autenticação: {e}")
            return False
    
    def autenticar_cliente(self, email: str, senha: str) -> bool:
        """Autentica cliente"""
        try:
            clientes = JSONService.carregar_dados(self.CAMINHO_LOG_CLIENTE)
            for cliente in clientes:
                if cliente.get("email") == email and cliente.get("senha") == senha:
                    return True
            return False
        except Exception:
            return False
    
    def cadastrar_cliente(self, cliente_data: dict) -> bool:
        """Cadastra novo cliente"""
        try:
            clientes = JSONService.carregar_dados(self.CAMINHO_CLIENTES)
            logins = JSONService.carregar_dados(self.CAMINHO_LOG_CLIENTE)
            
            # Verifica se email já existe
            if any(c.get("email") == cliente_data["email"] for c in clientes):
                print("Erro: Email já cadastrado!")
                return False
            
            clientes.append(cliente_data)
            logins.append({
                "nome": cliente_data["nome"],
                "email": cliente_data["email"],
                "senha": cliente_data["senha"]
            })
            
            return (JSONService.salvar_dados(self.CAMINHO_CLIENTES, clientes) and
                   JSONService.salvar_dados(self.CAMINHO_LOG_CLIENTE, logins))
                   
        except Exception as e:
            print(f"Erro ao cadastrar cliente: {e}")
            return False