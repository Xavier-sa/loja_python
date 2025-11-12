import time

class Helpers:
    @staticmethod
    def mostrar_loading(mensagem: str = "Processando", duracao: int = 3):
        """Exibe animação de loading"""
        print(f"\n{mensagem}", end="")
        for i in range(duracao):
            time.sleep(0.5)
            print(".", end="", flush=True)
        print()
    
    @staticmethod
    def formatar_moeda(valor: float) -> str:
        """Formata valor como moeda brasileira"""
        return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    
    @staticmethod
    def limpar_tela():
        """Limpa a tela do terminal"""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')