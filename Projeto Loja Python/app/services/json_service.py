import json
import os
from typing import List, Any

class JSONService:
    @staticmethod
    def carregar_dados(caminho: str) -> List[Any]:
        """Carrega dados de arquivo JSON"""
        try:
            with open(caminho, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    @staticmethod
    def salvar_dados(caminho: str, dados: List[Any]) -> bool:
        """Salva dados em arquivo JSON"""
        try:
            os.makedirs(os.path.dirname(caminho), exist_ok=True)
            with open(caminho, "w", encoding="utf-8") as arquivo:
                json.dump(dados, arquivo, ensure_ascii=False, indent=4)
            return True
        except Exception:
            return False