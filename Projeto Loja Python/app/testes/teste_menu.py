import sys
sys.path.append('app')

from views.menu_view import MenuView

print("=== TESTE DE EXIBIÇÃO DO MENU ===")
MenuView.mostrar_menu_principal()
print("✅ Menu deve aparecer UMA vez apenas")