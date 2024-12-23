import funcoes as f

RED = "\033[91m"
RESET = "\033[0m"


def login_pagamento():

    #Lendo arquivos de cadastro no json
    cadastro_cliente= f.abrir_lista()
    #Lendo arquivos de login no json
    dados_login= f.dados_log_cliente()
   
    while True:
        
        print("\n")
        print("################################")
        print("#             LOGIN            #")
        print("#                              #")
        print("#  (1) LOGAR                   #")
        print("#  (2) CADASTRAR               #")
        print("#                              #")
        print("################################")

        menu=f.opcao_menu()
    
        match menu:

            #Login
            case 1:
                email=input("Informe O Email: ")
                senha= f.get_password_masked("Digite sua senha: ")
               
                cont=0
                for dado in dados_login:
                    if email==dado["email"] and senha==dado["senha"]:
                        print(f"\nMuito bem {dado["nome"]}, Login efetuado!\n")
                        cont+=1
                        break
                    elif email==dado["email"] and senha!=dado["senha"]:
                        print("Senha inválida!")
                    elif email!=dado["email"] and senha==dado["senha"]:
                        print("Email não cadastrado!")
                    
                    
                if cont==1:
                    break  
                else:
                        print(f"\n  {RED}Email e Senha inválidos!{RESET}\n") 

            #Cadastro        
            case 2:
                print("    Cadastro     \n")
                try:
                    nome= f.validar_letras("Informe seu nome: ")
                    
                    sobre_nome=f.validar_letras("Informe seu sobre nome: ")
                    
                    cpf=f.validar_numeros("Informe CPF: ")
                    telefone=f.validar_numeros("Informe Telefone: ")

                    print("\nEndereço\n")
                    bairro=f.validar_letras("Bairro: ")
                    
                    rua=f.validar_letras("Rua: ")
                    
                    numero=f.validar_numeros("Número: ")
                    cep=f.validar_numeros("Cep: ")
                    cidade=f.validar_letras("Cidade: ")
                    estado=f.validar_letras("Estado: ")
                    email=f.validar_letras("Email: ")
                    while True:
                        senha=input("Senha: ")
                        confirme_senha=input("Confirme sua senha: ")
                        if senha == confirme_senha:
                            break
                        else:
                            print("[ERRO] Digite novamente!")
                    finalizar_cadastro=f.validar_finalizar_cadastro()
                
                    if finalizar_cadastro =="S":
                        cadastro={
                            "nome":nome,
                            "sobre_nome":sobre_nome,
                            "cpf":cpf,
                            "telefone":telefone,
                            "bairro":bairro,
                            "rua":rua,
                            "numero":numero,
                            "cep":cep,
                            "cidade":cidade,
                            "estado":estado,
                            "email":email,
                            "senha":senha,
                            "confirme_senha":confirme_senha
                        }

                        login={
                            "nome":nome,
                            "email":email,
                            "senha":senha
                        }
                        
                        
                        f.dados_json(cadastro_cliente, cadastro)
                        f.salvar_dados_login(dados_login,login)
                        print("\n\tCadastro Finalizado")
                        pass
                    else:
                        pass
                except:
                    pass
            
            case _:
                print(f"\n\t{RED}Informe uma opção válida!{RESET}")