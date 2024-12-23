import json
import funcoes

def validar_login():
    while True:
        try:
            login = input('\nDigite o login: ')
            if not login:
                print('Login Invalido')
            else:
                return login
        except:
            print('Login Invalido')

def validar_senha():
    while True:
        try:
            senha = funcoes.get_password_masked("Digite sua senha: ")
            if not senha:
                print('Senha invalida') 
            else:
                return senha
        except:
            print('Seha Invalida')


#criando arquivo json
def dados_json(lista):      
    with open("data/log/login_gerente.json","w", encoding= "utf-8") as arquivo:
        json.dump(lista,arquivo, indent=4)
#carregar arquivos json
def abrir_lista():
        #caminho do arquivo json com os dados
        caminho = "data/log/login_gerente.json"

        #carregar lista co dados
        with open(caminho, "r", encoding="utf-8") as arquivo:
            lista = json.load(arquivo)
        return lista
        

def login_adm():     
            
    while True:
        # dados_json(lista_credenciais)
        lista_credenciais = abrir_lista()

        login = validar_login()

        senha = validar_senha()

        if login == lista_credenciais['email'] and senha == lista_credenciais['senha']:
            print()
            print('\nBem vindo.Você esta logado como administrador\n')
            break
        else:
            print()
            print('\nInformações incorretas.LOGIN ou SENHA estão incorretas.')


