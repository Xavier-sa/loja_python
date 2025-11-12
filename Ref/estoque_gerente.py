import login_gerente
import time
import funcoes as f
import json

def r_estoque_produtos():
        #caminho do arquivo json com os dados
        caminho = "data/Estoque/Produtos/produtos.json"
        try:
            #carregar lista co dados
            with open(caminho, "r", encoding="utf-8") as arquivo:
                lista = json.load(arquivo)
            return lista
        except:
            return []
def w_estoque_produtos(produto, produtos):      
    produtos.append(produto)    
    with open("data/Estoque/Produtos/produtos.json","w", encoding= "utf-8") as arquivo:
        json.dump(produtos, arquivo, ensure_ascii=False, indent=4)
def r_vendas_dia():
        #caminho do arquivo json com os dados
        caminho = "data/Estoque/Vendas/vendas_dia.json"
        try:
            #carregar lista co dados
            with open(caminho, "r", encoding="utf-8") as arquivo:
                lista = json.load(arquivo)
            return lista
        except:
            return []
def r_vendas_semana():
        #caminho do arquivo json com os dados
        caminho = "data/Estoque/Vendas/vendas_semana.json"
        try:
            #carregar lista co dados
            with open(caminho, "r", encoding="utf-8") as arquivo:
                lista = json.load(arquivo)
            return lista
        except:
            return []
def r_vendas_mes():
        #caminho do arquivo json com os dados
        caminho = "data/Estoque/Vendas/vendas.mes.json"
        try:
            #carregar lista co dados
            with open(caminho, "r", encoding="utf-8") as arquivo:
                lista = json.load(arquivo)
            return lista
        except:
            return []

def gerente():
    
    vendas_dia =r_vendas_dia()

    vendas_semana = r_vendas_semana()

    vendas_mes =r_vendas_mes()
    
    login_gerente.login_adm()


    #Lista de produtos
    lista_produtos = r_estoque_produtos() 
    
   
    opcao =1
    while  opcao != 6:
        print('########################################')
        print('#           MENU PRINCIPAL             #')
        print('#                                      #')
        print('#   (1) - CADASTRAR NOVO PRODUTO       #')
        print('#   (2) - EDITAR PRODUTO               #')
        print('#   (3) - EXCLUIR PRODUTO              #')
        print('#   (4) - RELATORIO DE VENDAS          #')
        print('#   (5) - LISTA DOS PRODUTOS           #')
        print('#   (6) - SAIR DO SISTEMA              #')
        print('#                                      #')
        print('########################################')
        
        # Solicita ao usuário que escolha uma opção
        try:    
            opcao = int(input('\nOpção: '))
        except ValueError:
            print('\n\tDigite um numero inteiro')
            
        except NameError:
            print('\n\tDigite um numero inteiro!')
        else:    
            if opcao > 6 or opcao < 0 :
                print('\n\tOpcão invalida, digite uma opção de 1 a 6!')
            else:
                match opcao:
                    case 1:
                        print('#################################################################')
                        print('--------------------- CADASTRAR NOVO PRODUTO -----------------')
                        nome =f.validar_letras('\nInforme o nome do produto: ')
                        quantidade = f.validar_numeros('\nInforme a nova quantidade: ')
                        valor = f.validar_numeros('Informe o valor do produto: ')
                        
                        novo_produto = {
                            'nome': nome,
                            'quantidade': quantidade,
                            'valor': valor
                        }
                        #json
                        w_estoque_produtos(novo_produto, lista_produtos)

                        print('\nNovo produto cadastrado com sucesso!\n')
                        print(f"  Nome: {novo_produto["nome"]} | Quanidade: {novo_produto["quantidade"]} | Valor: {novo_produto["valor"]}\n")
                    case 2:
                        
                        print('#################################################################')
                        print('------------------------ EDITAR PRODUTO -------------------------')
                        for i, produto in enumerate(lista_produtos):
                            print(f'\nÍndice: {i} - {produto['nome']} | Quantidade:{produto['quantidade']} | Valor:{produto['valor']}')

                        try:    
                            indice = f.validar_numeros_int('\nInforme o índice, do produto que deseja editar: ')
                            
                            
                        except NameError:
                            print('\n\tDigite um numero inteiro!')
                        except ValueError:
                            print('\n\tDigite um valor  inteiro!')
                        else:
                        
                            if 0 <= indice < len(lista_produtos):
                                print(f"\nProduto:\n  Nome: {lista_produtos[indice]["nome"]} | Quantidade: {lista_produtos[indice]["quantidade"]} | Valor: {lista_produtos[indice]["valor"]}\n")
                                
                            
                                while True:
                                    print('######################################')
                                    print('#       SUBMENU DE EDIÇÃO            #')
                                    print('#                                    #')
                                    print('#      (1) - EDITAR NOME             #')
                                    print('#      (2) - EDITAR VALOR            #')
                                    print('#      (3) - EDITAR QUANTIDADE       #')
                                    print('#      (4) - VOLTAR                  #')
                                    print('######################################')
                                
                                
                                    try:    
                                        submenu = f.validar_numeros_int('\nEscolha uma opção: ')
                                    except ValueError:
                                        print('\n\tDigite um numero inteiro')
                                    match submenu:
                                        case 1:
                                            novo_nome = f.validar_letras('\nQual o novo nome? ')
                                            lista_produtos[indice]['nome'] = novo_nome
                                            print('\nNome do produto editado com sucesso!\n')
                                            print(f"\nNome: {lista_produtos[indice]["nome"]} | Quantidade: {lista_produtos[indice]["quantidade"]} | Valor: {lista_produtos[indice]["valor"]}\n")

                                        case 2:
                                            novo_preco = f.validar_numeros('\nInforme o novo valor? ')
                                            lista_produtos[indice]['valor'] = novo_preco
                                            print('\nValor do produto editado com sucesso!\n')
                                            print(f"Nome: {lista_produtos[indice]["nome"]} | Quantidade: {lista_produtos[indice]["quantidade"]} | Valor: {lista_produtos[indice]["valor"]}\n")

                                        case 3:
                                            nova_quantidade = f.validar_numeros_int('\nQual a nova quantidade: ')
                                            lista_produtos[indice]['quantidade'] = nova_quantidade
                                            print('\nQuantidade do produto editado com sucesso!\n')
                                            print(f"Nome: {lista_produtos[indice]["nome"]} | Quantidade: {lista_produtos[indice]["quantidade"]} | Valor: {lista_produtos[indice]["valor"]}\n")

                                        case 4:
                                            break
                                    
                                        case _:
                                            print('\n\tOpção inválida!\n')

                            else:
                                print('\n\tÍndice inválido!\n')

                    case 3:
                        print('#################################################################')
                        print('------------------------ EXCLUIR PRODUTO ------------------------')
                        for i, produto in enumerate(lista_produtos):
                            print(f'\nÍndice: {i} - {produto['nome']} | Quantidade:{produto['quantidade']} | Valor:{produto['valor']}\n')

                        indice = f.validar_numeros_int('Informe o índice, do produto que deseja excluir: ')
                        if 0 <= indice < len(lista_produtos):
                            produto_excluido = lista_produtos.pop(indice)
                            print(f'\nO Produto {produto_excluido["nome"]}, foi excluído com sucesso!\n')

                        else:
                            print('\n\tÍndice inválido!\n')

                    case 4:
                        while True:
                            print('########################################')
                            print('#      RELATÓRIO DE VENDAS             #')
                            print('#                                      #')
                            print('#       (1) - VENDAS DO DIA            #')
                            print('#       (2) - VENDAS DA SEMANA         #')
                            print('#       (3) - VENDAS DO MÊS            #')
                            print('#       (4) - VOLTAR                   #')
                            print('#                                      #')
                            print('########################################')
                        
                            try:    
                                opcao_menu = f.validar_numeros_int('\nOpção:')
                            except ValueError:
                                print('\n\tDigite um numero inteiro\n')
                            else:
                            
                                match opcao_menu:
                                    case 1:
                                        print("\nProdutos:" )
                                        soma_total=0
                                        for i, produto in enumerate(vendas_dia):
                                            total = produto['quantidade'] * produto['valor']
                                            soma_total += total
                                            print(f'\tNome: {produto['nome']} | Quantidade:{produto['quantidade']} | Valor:{produto['valor']}\n')

                                        print(f'\tTotal R$: {soma_total:,.2f}\n')
                                        
                                    case 2:
                                        print("\nProdutos:" )
                                        soma_total=0
                                        for i, produto in enumerate(vendas_semana):
                                            total = produto['quantidade'] * produto['valor']
                                            soma_total += total
                                            print(f'\tNome: {produto['nome']} | Quantidade:{produto['quantidade']} | Valor:{produto['valor']}\n')

                                        print(f'\tTotal R$: {soma_total:,.2f}\n')

                                    case 3:
                                        print("\nProdutos:" )
                                        soma_total=0
                                        for i, produto in enumerate(vendas_mes):
                                            total = produto['quantidade'] * produto['valor']
                                            soma_total += total
                                            print(f'\tNome: {produto['nome']} | Quantidade:{produto['quantidade']} | Valor:{produto['valor']}\n')

                                        print(f'\tTotal R$: {soma_total:,.2f}\n')
                                    
                                    case 4:
                                        break

                                    case _:
                                        print('\n\tOpção inválida!')
                                

                    
                    case 5:
                        print("\nProdutos")
                        for produto in lista_produtos:
                            print(f"\n\tNome: {produto["nome"]} | Quantidade: {produto["quantidade"]} | Valor: {produto["valor"]}\n")
                        
                    
                    case 6:
                        print('Saindo do sistema...')
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
                        break

                    case _:
                        print('opcão invalida, digite uma opção de 1 a 6')

        f.w_cliente_produtos(lista_produtos)
