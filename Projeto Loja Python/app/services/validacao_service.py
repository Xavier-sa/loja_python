import msvcrt

class ValidacaoService:
    RED = "\033[91m"
    RESET = "\033[0m"
    
    @staticmethod
    def validar_numero(mensagem: str, tipo=float) -> float:
        """Valida entrada numérica"""
        while True:
            try:
                return tipo(input(mensagem))
            except ValueError:
                print(f"\n{ValidacaoService.RED}Informe apenas números!{ValidacaoService.RESET}")
    
    @staticmethod
    def validar_texto(mensagem: str) -> str:
        """Valida entrada de texto"""
        while True:
            texto = input(mensagem).strip()
            if texto and all(c.isalpha() or c.isspace() for c in texto):
                return texto
            print(f"\n{ValidacaoService.RED}Digite apenas letras!{ValidacaoService.RESET}")
    
    @staticmethod
    def get_password_masked(prompt: str = 'Senha: ') -> str:
        """Captura senha com mascaramento"""
        print(prompt, end='', flush=True)
        password = []
        
        while True:
            char = msvcrt.getch().decode('utf-8')
            if char in '\r\n':
                break
            elif char == '\x03':  # Ctrl+C
                raise KeyboardInterrupt
            password.append(char)
            print('*', end='', flush=True)
        
        return ''.join(password)
    
    @staticmethod
    def validar_inteiro(mensagem: str) -> int:
        """Valida entrada de número inteiro"""
        while True:
            try:
                valor = input(mensagem)
                if not valor:
                    raise ValueError
                return int(valor)
            except ValueError:
                print(f"\n{ValidacaoService.RED}Informe um número inteiro válido!{ValidacaoService.RESET}")
                
                
    @staticmethod
    def validar_email(mensagem: str) -> str:
        """Valida formato de email básico"""
        while True:
            email = input(mensagem).strip().lower()
            if "@" in email and "." in email:
                return email
            print(f"\n{ValidacaoService.RED}Email inválido!{ValidacaoService.RESET}")