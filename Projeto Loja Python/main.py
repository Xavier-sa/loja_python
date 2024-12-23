import loja_online
import loja_online_logado
import funcoes as f
import estoque_gerente


RED = "\033[91m"
RESET = "\033[0m"


while True:
  print("")
  print("################################")
  print("#            MENU              #")
  print("#                              #")
  print("#  (1) ACESSAR LOJA            #")
  print("#  (2) LOGIN / CADASTRO        #")
  print("#  (3) GERENTE                 #")
  print("#  (0) SAIR                    #")
  print("#                              #")
  print("################################")
  #Menu
  menu= f.main_menu()

  match menu:
    case 1:
        loja_online.loja()
        break
     
    case 2:
        loja_online_logado.loja()
        break
                 
    case 3:
        estoque_gerente.gerente()
        
       
    case 0:
        print(f"\n\t{RED}Você Saiu!\n{RESET}")
        break
     
    case _:
        print(f"\n\t{RED}Opção inválida!{RESET}")
        pass

     


