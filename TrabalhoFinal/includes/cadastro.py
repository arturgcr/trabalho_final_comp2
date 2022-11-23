import pandas as pd
from csv import *
from classeUsuario import *

def verificaValidadedoUsuario(termo):
    """função utilizada para a verificação de se o email da tentativa de cadastro ja foi utilizada"""

    #define a variavel de leitura, lendo o arquivo por completo
    arquivo = pd.read_csv("arquivosCsv/cadastros.csv", header = None)
    #cria uma variavel boleana para fins de verificação
    verificao = True

    #olha termo a termo dos cadastros na coluna email e o compara com o novo inserido, verificando sua validade 
    for i in range(1,len(arquivo)):
        #se o arquivo verificado for igual ao inserido a verificacao é dada como falsa 
        if str(arquivo[3][i]) == str(termo):
            verificao = False       

    #retorna a verificao
    return(verificao)

def cadastroDeUsuario(nome,endereco,senha,email,tipo_usuario):
    """função ques cadastro o usuario escrevendo seu nome no arquivo .csv"""

    #chama a função de verificação do email utilizado para saber se o mesmoe esta em uso, caso n esteja, entra no if
    if verificaValidadedoUsuario(email):
        #abre o arquivo .csv de cadastro no modo append para adicionar usuarios
        with open("arquivosCsv/cadastros.csv", mode="a", newline="\n") as escrita_no_arquivo:
            #define o objeto de escrita
            objeto_de_escrita = writer(escrita_no_arquivo)
            #escreve os parametros passados na funç~qao no arquivo .csv
            objeto_de_escrita.writerow([nome,endereco,senha,email,tipo_usuario])
            #fecha o arquivo para evitar possíveis erros
            escrita_no_arquivo.close()   
            print("sucesso!!!")

    #caso o email ja tenha sido cadastrado não cadastra o novo, entrando no else
    else:
        print("email ja cadastrado")

def loginUsuario(email_login,senha_login):
    """função que cria o objeto usuario a partir de informada a senha e o email de uma pessoa ja cadastrada, processo de login"""
    global usuario_ativo
    arquivo = pd.read_csv("arquivosCsv/cadastros.csv", header = None)

    #percorre as linhas do arquivo de cadastros de usuarios
    for i in range(1,len(arquivo)):
        #verifica se o email e senha inseridos como parametro representam um usuario valido, se sim, executa oques esta dentro do if
        if str(arquivo[3][i]) == str(email_login) and str(arquivo[2][i]) == str(senha_login):
            #define as componentes que definem um usuario
            nome = arquivo[0][i]
            endereco = arquivo[1][i]
            senha = arquivo[2][i]
            email = arquivo[3][i]
            tipo_usuario = arquivo[4][i]

            #cria o objeto usuario, passando seus parametros
            usuario_ativo = Usuario(nome,endereco,senha,email,tipo_usuario)
            print("funcionou")
            #retorna o objeto
            return usuario_ativo
            break

        elif i == len(arquivo):
            loginUsuario()
