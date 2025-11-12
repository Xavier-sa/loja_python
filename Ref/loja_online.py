import login_cliente
import funcoes as f
import time
import estoque_gerente



def loja():

    RED = "\033[91m"
    RESET = "\033[0m"

    
    lista_produtos= estoque_gerente.r_estoque_produtos()

    vendas=estoque_gerente.r_vendas_dia()
    carrinho=[]

    logado=False
    while True: 

        #ver produtos cadastrados
        f.exibir_produtos(lista_produtos)

        #Pesquisar o que deseja comprar
        produto_nome=f.validar_produto_nome(lista_produtos)
        if produto_nome=="s":
            print(f"\n\t{RED}Você saiu!{RESET}\n")
            continuar=False
            break
            
        elif produto_nome == '':
            pass
        else:
            finalizar=False
            for  produto in lista_produtos: 
                if produto_nome == produto["nome"]:
                    
                    if produto['quantidade']== 0:
                        print("Produto não disponível no momento!")
                        break
                            
                    produto_quantidade=f.validar_entradas()
                    if produto_quantidade > produto["quantidade"]:
                        print("\nQuatidade inválida, verifique a lista!")
                        break

                    #Adicionar ao carrinho
                    adicionar=f.validar_adicionar()
                    if adicionar=="N":
                        break
                    elif adicionar == "S":
                        valor_custo=produto['valor']
                        valor=produto_quantidade*valor_custo
                        #debitando estoque
                        quantidade_estoque=produto['quantidade']
                        quantidade_atualizada=quantidade_estoque - produto_quantidade
                        produto['quantidade']=quantidade_atualizada

                        
                        produto_carrinho={
                            "nome":produto_nome,
                            "quantidade": produto_quantidade,
                            "valor": valor
                        }
                        
                        carrinho.append(produto_carrinho)
                        

                        total_compra=0
                        print("\nCarrinho")
                        for i, produto in enumerate(carrinho):
                            valor=carrinho[i]['valor']
                            total_compra+= valor
                            print(f"\nProduto ({i+1}) - Nome: {produto['nome']} | Valor: {produto['valor']} | Quantidade: {produto['quantidade']}\n")
                        print(f"Total: R${total_compra:.2f}\n")
                        
                    else:
                        print(f"{RED}Opção inválida!{RESET}")   
                        break
                    
                    finalizar="A"
                    while True:
                        print()
                        print("#############################")
                        print("#                           #")
                        print("#  (1) EDITAR CARRINHO      #")
                        print("#  (2) CONTINUAR COMPRANDO  #")
                        print("#  (3) FINALIZAR PEDIDO     #")
                        print("#                           #")
                        print("#############################")
                    
                        menu = f.carrinho()
                        
                        match menu:
                            case 1:
                                while True:
                                    if not carrinho:
                                        print(f"\nCarrinho:\n\t{RED}(VAZIO){RESET}")
                                        break
                                    else:
                                        for i, produto in enumerate(carrinho):
                                            print(f"  Produto ({i+1}) - Nome: {produto['nome']} | Valor: {produto['valor']} | Quantidade: {produto['quantidade']}\n")
                                        
                                        print("#############################")
                                        print("#      EDITAR CARRINHO      #")
                                        print("#                           #")
                                        print("#  (1) QUANTIDADE PRODUTO   #")
                                        print("#  (2) EXCLUIR PRODUTO      #")
                                        print("#  (3) LIMPAR CARRINHO      #")
                                        print("#  (0) VOLTAR               #")
                                        print("#                           #")
                                        print("#############################")   

                                        menu = f.carrinho()
                                    
                                        match menu:

                                            #Editar Quantidade
                                            case 1:
                                                editar=f.carrinho_quantidade(lista_produtos,carrinho)

                                            #Excluir produto
                                            case 2:
                                                excluir=f.carrinho_excluir(carrinho)
                                            
                                            #Limpar carrinho
                                            case 3:
                                                carrinho=[]

                                            #Sair
                                            case 0:
                                                break


                            case 2:
                                break

                            case 3:
                                if carrinho:
                                    finalizar="S"
                                    break
                                else:
                                    print(f"Carrinho {RED}(VAZIO){RESET}, adicione Produto, antes de finalizar!")
                                    
                            case _:
                                print(f"{RED}Opção inválida!{RESET}")




                    
                    #Finalizar compra
                    # finalizar=f.validar_finalizar()
                    if finalizar == "N":
                        break
                    if finalizar == "S":
                        if logado==False:
                            print("\nSeu pedido foi finalizado, efetue o login ou faça seu cadastro, para efetuar o pagamento!\n")
                            logado=True

                            #Pagamento
                            continua=login_cliente.login_pagamento()
                            if continua  == False:
                                break

                        else:
                            print("\nSeu pedido foi finalizado, escolha a forma de Pagamento!\n")
                            pass
                    

                        #Dados Pagamento
                        print("################################")
                        print("#     FORMAS DE PAGAMENTO      #")
                        print("#                              #")
                        print("#  (1) PIX                     #")
                        print("#  (2) CARTÃO                  #")
                        print("#  (3) BOLETO                  #")
                        print("#                              #")
                        print("################################")

                        
                        pagamento = f.validar_pagamento()
                        
                        
                        match pagamento:
                            #Pix
                            case 1:
                                print("\nChave pix para pagamento:\n\t WQC$RS]xUwe")

                                pagamento=f.validar_finalizar_pagamento()

                                if pagamento== "F":
                                    print('Finalizando...')
                                    print('█▒▒▒▒▒▒▒▒▒')
                                    time.sleep(0.5)
                                    print('20%')
                                    print('██▒▒▒▒▒▒▒▒')
                                    time.sleep(0.8)
                                    print('30%')
                                    print('███▒▒▒▒▒▒▒')
                                    time.sleep(1)
                                    print('50%')
                                    print('█████▒▒▒▒▒')
                                    time.sleep(1.5)
                                    print('100%')
                                    print('██████████')

                                    print("""\n\n                   ▄ ▌ ▐ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▐
        ▄ ▄ █ █ ▌ █ ░  ░ O PRODUTO ESTÁ A CAMINHO ░ ░ ░ ░ ░ ░ ░ ░▐
    ▄ ▄ ▄ ▌ ▐ █ █ ▌ █ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░  ░ ░ ░ ░ ░ ░ ░ ░ ▐
    █ █ █ █ █ █ █ ▌ █ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄▌
    ▀ (@) ▀ ▀ ▀ ▀ ▀ ▀ ▀ (@)(@) ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ (@) ▀ ▘\n\n""") 
                                    
                                    
                                    
                                    print("\nCompra finalizada com sucesso! ")

                                    print("\nResumo da Compra:\n")

                                    total_compra=0
                                    for i, produto in enumerate(carrinho):
                                        valor=carrinho[i]['valor']
                                        total_compra+= valor

                                        print(f"\tNome: {produto['nome']} | Valor: {produto['valor']} | Quantidade: {produto['quantidade']}\n")

                                    print(f"\nValor Total: R${total_compra:.2f}\n")

                                    print("\nAcompanhe seu pedido pelo Código do Pedido:\n\t  Código: 5698452\n")


                                elif pagamento == "C":
                                    print(f"\n\t{RED}Pagamento Cancelado!{RESET}")
                                else:
                                    pass
                                    
                            #Cartão
                            case 2:
                                cartao = f.validar_letras("\nInforme tipo do cartão, (C)Crédito ou (D) Débito: ")
                                nome_cartão=f.validar_letras("\nInforme Nome conforme está no cartão: ")
                                numero_cartao=f.validar_numeros("\nInforme número do cartão: ")
                                data_validade = f.validar_numeros("\nInforme data de válidade: ")
                                cvv = f.validar_numeros("\nInforme CVV: ")
                                
                                confirmar=input("\nAs informações estão corretas? S/N: ").upper()
                                if confirmar== "S":
                                    print('\nFINALIZANDO A COMPRA…')

                                    print('█▒▒▒▒▒▒▒▒▒')
                                    time.sleep(0.5)
                                    print('20%')
                                    print('██▒▒▒▒▒▒▒▒')
                                    time.sleep(0.8)
                                    print('30%')
                                    print('███▒▒▒▒▒▒▒')
                                    time.sleep(1)
                                    print('50%')
                                    print('█████▒▒▒▒▒')
                                    time.sleep(1.5)
                                    print('100%')
                                    print('██████████')

                                    print("""\n\n                   ▄ ▌ ▐ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▐
        ▄ ▄ █ █ ▌ █ ░  ░ O PRODUTO ESTÁ A CAMINHO ░ ░ ░ ░ ░ ░ ░ ░▐
    ▄ ▄ ▄ ▌ ▐ █ █ ▌ █ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░  ░ ░ ░ ░ ░ ░ ░ ░ ▐
    █ █ █ █ █ █ █ ▌ █ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄▌
    ▀ (@) ▀ ▀ ▀ ▀ ▀ ▀ ▀ (@)(@) ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ (@) ▀ ▘\n\n""") 
                                    
                                    
                                    
                                    print("\nCompra finalizada com sucesso! ")

                                    print("\nResumo da Compra:\n")
                                    total_compra=0
                                    for i, produto in enumerate(carrinho):
                                        valor=carrinho[i]['valor']
                                        total_compra+= valor
                                        print(f"\tNome: {produto['nome']} | Valor: {produto['valor']} | Quantidade: {produto['quantidade']}\n")
                                    print(f"\nValor Total: R${total_compra:.2f}\n")

                                    print("\nAcompanhe seu pedido pelo Código do Pedido:\n\t  Código: 5698452\n")
                                    
                                    
                                else:
                                    pass
                            #Boleto
                            case 3:
                                cpf=f.validar_numeros("Informe número CPF, para gerar o boleto: ")
                                if cpf:
                                    print('\nGERANDO BOLETO…')
                                    print('█▒▒▒▒▒▒▒▒▒')
                                    time.sleep(0.5)
                                    print('20%')
                                    print('██▒▒▒▒▒▒▒▒')
                                    time.sleep(0.8)
                                    print('30%')
                                    print('███▒▒▒▒▒▒▒')
                                    time.sleep(1)
                                    print('50%')
                                    print('█████▒▒▒▒▒')
                                    time.sleep(1.5)
                                    print('100%')
                                    print('██████████')

                                    print("\nBoleto gerado com sucesso, a validação pode demorar até 5 dias ulteis.\nVocê receberá a confirmação via email, junto com código de rastreio da compra.\n")

                                    

                            case _:
                                print(f"\n{RED}Opção inválida!{RESET}")

        
        f.enviar_carrinho(vendas,lista_produtos)
        f.w_cliente_produtos(lista_produtos)
        
                   