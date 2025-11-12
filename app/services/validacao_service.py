import msvcrt

class ValidacaoService:
    RED = "\033[91m"
    RESET = "\033[0m"
    
    @staticmethod
    def validar_numero(mensagem: str, tipo=float) -> float:
        """Valida entrada numérica"""
        while True:
            try:
                valor = input(mensagem)
                if not valor:
                    raise ValueError
                return tipo(valor)
            except ValueError:
                print(f"\n{ValidacaoService.RED}Informe um número válido!{ValidacaoService.RESET}")
    
    @staticmethod
    def validar_inteiro(mensagem: str) -> int:
        """Valida entrada de número inteiro"""
        return ValidacaoService.validar_numero(mensagem, int)
    
    @staticmethod
    def validar_texto(mensagem: str) -> str:
        """Valida entrada de texto (apenas letras e espaços)"""
        while True:
            texto = input(mensagem).strip()
            if texto and all(c.isalpha() or c.isspace() for c in texto):
                return texto
            print(f"\n{ValidacaoService.RED}Digite apenas letras e espaços!{ValidacaoService.RESET}")
    
    @staticmethod
    def validar_email(mensagem: str) -> str:
        """Valida formato de email básico"""
        while True:
            email = input(mensagem).strip().lower()
            if "@" in email and "." in email:
                return email
            print(f"\n{ValidacaoService.RED}Email inválido!{ValidacaoService.RESET}")
    
    @staticmethod
    def get_password_masked(prompt: str = 'Senha: ') -> str:
        """Captura senha com mascaramento"""
        print(prompt, end='', flush=True)
        password = []
        
        while True:
            try:
                char = msvcrt.getch()
                char = char.decode('utf-8')
                
                if char in '\r\n':
                    break
                elif char == '\x03':  # Ctrl+C
                    raise KeyboardInterrupt
                elif char == '\x08':  # Backspace
                    if password:
                        password.pop()
                        print('\b \b', end='', flush=True)
                else:
                    password.append(char)
                    print('*', end='', flush=True)
            except UnicodeDecodeError:
                continue
        
        print()  # Nova linha após a senha
        return ''.join(password)
    
    @staticmethod
    def confirmar_senha() -> tuple[str, str]:
        """Solicita senha e confirmação"""
        while True:
            senha = ValidacaoService.get_password_masked("Senha: ")
            confirmacao = ValidacaoService.get_password_masked("Confirme a senha: ")
            
            if senha == confirmacao:
                return senha, confirmacao
            else:
                print(f"\n{ValidacaoService.RED}Senhas não coincidem! Tente novamente.{ValidacaoService.RESET}")