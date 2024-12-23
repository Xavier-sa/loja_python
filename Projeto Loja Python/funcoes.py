import json
import msvcrt  


#Menu Main
def main_menu():
    RED = "\033[91m"
    RESET = "\033[0m"
    while True:
        try:
            menu= int(input("\nOpção menu: "))
            if menu== 0:
                return 0
            elif menu== 2:
                return 2
            else:
                return menu
        except:
            print(f"\n\t{RED}Opção inválida!{RESET}")
            pass


def cadastros_login():
    cadastro_cliente = []
    return cadastro_cliente

#Validação de entrada Loja
def exibir_produtos(lista_produtos):
    print("\nLista de Produtos")

    for i, produto in enumerate(lista_produtos):
        if produto["quantidade"]> 0:
            print(f"\n\tNome: {produto['nome']} | Valor: {produto['valor']} | Quantidade: {produto['quantidade']}\n")


def validar_produto_nome(lista_produtos):
    RED = "\033[91m"
    RESET = "\033[0m"
    while True:
        produto_nome=input("Informe o produto que deseja comprar, ou digite (s) para Sair: ").lower()
        for produto in lista_produtos: 
            if produto_nome == produto["nome"]:
                return produto_nome
        if not produto_nome:
            print(f"\n\t{RED}Opção inválida!{RESET}")
        elif produto_nome=="s":
            return produto_nome    
        else:
            print(f"\n\t{RED}Opção inválida!{RESET}")


def validar_entradas():
    RED = "\033[91m"
    RESET = "\033[0m"
    while True:
        try:  
            produto_quantidade=int(input("Informe a quantidade que deseja compra: "))
            return produto_quantidade
        except ValueError:
            print(f"\n\t{RED}[ERRO] Informe um valor numérico(inteiro)!{RESET}")
            
        except:
            print(f"\n\t{RED}Erro inesperado!{RESET}")           


def validar_adicionar():
    RED = "\033[91m"
    RESET = "\033[0m"
    continuar=True
    while continuar==True:
        try:  
            adicionar=input("\nDeseja adicionar Produto ao carrinho? S/N: ").upper()
            if adicionar == "S":
                
                return "S"
            elif adicionar == "N":
                
                return "N"
                
            else:
                print(f"\n\t{RED}Opção inválida!{RESET}")
            
        
        except:
            print(f"\n\t{RED}Opção inválida!{RESET}")


def validar_finalizar():
    RED = "\033[91m"
    RESET = "\033[0m"
    while True:
        try:  
            finalizar=input("Deseja finalizar o pedido? S/N: ").upper()
            if finalizar == "S":
                return "S"
            elif finalizar == "N":
                return "N"
                
            else:
                print(f"\n\t{RED}Opção inválida!{RESET}")
            
        except:
            print(f"\n\t{RED}Opção inválida!{RESET}") 


def validar_pagamento():
    RED = "\033[91m"
    RESET = "\033[0m"
    while True:
        try:  
            pagamento = int(input("\nEscolha a forma de pagamento: "))
            if pagamento > 3 or pagamento < 0:
                print(f"\n\t{RED}Opção inválida!{RESET}")
            else:
                return pagamento
        except ValueError:
            print(f"\n\t{RED}[ERRO] Informe um valor numérico(inteiro)!{RESET}")
            
        except:
            print(f"\n\t{RED}Erro inesperado!{RESET}")


def validar_finalizar_pagamento():
    RED = "\033[91m"
    RESET = "\033[0m"
    while True:
        try:  
            pagamento=input("\nDigite (F) para finalizar ou (C) para cancelar: ").upper()
            if pagamento == "F":
                return "F"
            elif pagamento == "C":
                return "C"
                
            else:
                print(f"\n\t{RED}Opção inválida!{RESET}")
            
        except:
            print(f"\n\t{RED}Opção inválida!{RESET}") 


#Login/ Cadastro Clientes
def validar_finalizar_cadastro():
        RED = "\033[91m"
        RESET = "\033[0m"
        while True:
            try:  
                finalizar_cadastro=input("\nDeseja finalizar cadastro: S/N: ").upper()
                if finalizar_cadastro == "S":
                    return "S"
                elif finalizar_cadastro == "N":
                    return "N"
                    
                else:
                    print(f"\n\t{RED}Opção inválida!{RESET}\n")
                
            except:
                print(f"\n\t{RED}Opção inválida!{RESET}\n")


def opcao_menu():
        try:
            menu= int(input("\nOpção menu: "))
            return menu
        except:
            pass


#JSON

#Adiciona novo dicionário na lista (append), e escreve no arquivo Json (w)
def dados_json(lista, cadastro):
    lista.append(cadastro)    
    with open("data/Clientes/cadastro_cliente.json","w", encoding= "utf-8") as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False, indent=4)


#Faz a leitura dos dados no arquivo Json (r), retorna o arquivo
def abrir_lista():
        #caminho do arquivo json com os dados
        caminho = "data/Clientes/cadastro_cliente.json"
        try:
            #carregar lista co dados
            with open(caminho, "r", encoding="utf-8") as arquivo:
                lista = json.load(arquivo)
            return lista
        except:
            return []


##Adiciona novo dicionário na lista (append), e escreve no arquivo Json (w)
def salvar_dados_login(lista,login): 
    lista.append(login)
    try:     
        with open("data/log/log_cliente.json","w", encoding= "utf-8") as arquivo:
            json.dump(lista, arquivo, ensure_ascii=False, indent=4)
    except:
        return


#Faz a leitura dos dados no arquivo Json (r), retorna o arquivo.
def dados_log_cliente():
        #caminho do arquivo json com os dados
        caminho = "data/log/log_cliente.json"
        try:
            #carregar lista co dados
            with open(caminho, "r", encoding="utf-8") as arquivo:
                lista = json.load(arquivo)
            return lista
        except:
            return []

#Sair ou Continuar na loja
def validar_finalizar_sistema():
    RED = "\033[91m"
    RESET = "\033[0m"
    while True:
        try:  
            opcao=int(input("OPÇÃO: "))
            if opcao==1:
                return
            elif opcao ==2:
                return 2
                
            else:
                print(f"\n\t{RED}Opção inválida!{RESET}")

        except:
            print(f"\n\t{RED}Opção inválida!{RESET}")

def carrinho():
    
    RED = "\033[91m"
    RESET = "\033[0m"
    while True:
        try:
            menu= int(input("\nOpção menu: "))
            return menu
        except:
            print(f"{RED}Opção inválida!{RESET}")
            pass

def carrinho_quantidade(lista_produtos,carrinho):
    
    RED = "\033[91m"
    RESET = "\033[0m"
    while True:

        editar=input("Informe nome do produto: ")

        for produto in lista_produtos:
            if editar ==produto["nome"]:
                estoque=  produto['quantidade'] 
        cont=0           
        for produto in carrinho:
            if editar == produto["nome"]:
                estoque_total=estoque+produto["quantidade"]
                
                quantidade=int(input("Informe a nova quantidade: "))
                
                if quantidade > estoque_total:
                    print(f"\n\t{RED}Quantidade maior que o estoque!{RESET}\n")
                    
                else:
                    valor_und= produto["valor"]/ produto["quantidade"]
                    produto["quantidade"] = quantidade
                    
                    produto["valor"]= produto["quantidade"]* valor_und
                    
                    print(f"Produto:\n\tNome: {produto["nome"]}\n\tquantidade: {produto["quantidade"]}\n\tValor: {produto["valor"]}")
                    cont=1
        if cont==1:
            return editar
    

def carrinho_excluir(carrinho):
    RED = "\033[91m"
    RESET = "\033[0m"

    while True:

        excluir=input("\nInforme nome do produto: ")
        for i,produto in enumerate(carrinho):
            if excluir == produto["nome"]:
                nome=carrinho.pop(i)
                print(f"\n{RED}Produto ({nome["nome"]}) foi excluído!{RESET}")
                break
            else:
                print(f"{RED}\nProduto não encontrado!{RESET}")
        return excluir

#json produtos clientes
def w_cliente_produtos(produtos):      
    with open("data/Estoque/Produtos/produtos.json","w", encoding= "utf-8") as arquivo:
        json.dump(produtos, arquivo, ensure_ascii=False, indent=4)

def enviar_carrinho(nome_lista,lista): 
    nome_lista.append(lista)     
    with open("data/Estoque/Vendas/vendas_dia.json","w", encoding= "utf-8") as arquivo:
        json.dump(nome_lista, arquivo, ensure_ascii=False, indent=4)
   
    with open("data/Estoque/Vendas/vendas_semana.json","w", encoding= "utf-8") as arquivo:
        json.dump(nome_lista, arquivo, ensure_ascii=False, indent=4)

    with open("data/Estoque/Vendas/vendas_mes.json","w", encoding= "utf-8") as arquivo:
        json.dump(nome_lista, arquivo, ensure_ascii=False, indent=4) 

def get_password_masked(prompt='Password: '):
    """Prompt for password input with masking."""
    print(prompt, end='', flush=True)

    password = []
    while True:
        char = msvcrt.getch()
        char = char.decode('utf-8')

        if char in '\r\n':
            break
        elif char == '\x03':  # handle Ctrl+C
            raise KeyboardInterrupt
        elif char == '\x04':  # handle Ctrl+D
            raise EOFError
        else:
            password.append(char)
            print('*', end='', flush=True)

    return ''.join(password)


def validar_letras(mensagem):
    while True:
        nome=input(mensagem)
        juntar= nome.replace(" ", "")
        juntar=nome.isalpha()
        
        if juntar==True:
            return nome
        else:
            print("Digite apenas letras!")
        
def validar_numeros(mensagem):
    while True:
        try:
            nome=float(input(mensagem))
            return nome
        except:
            print("Informe apenas números!")

def validar_numeros_int(mensagem):
    while True:
        try:
            nome=int(input(mensagem))
            return nome
        except:
            print("Informe apenas números!")