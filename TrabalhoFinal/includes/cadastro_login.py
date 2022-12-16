
"""arquivo de resolução diversa de problemas como de contagem utilizando classes para aplicações no filtro e verificção
de login e cadastro de usuario e a utilização do login em si para a criação do objeto usuario do arquivo Usuario. """

import pandas as pd
from csv import *
from Usuario import *
from tkinter import *

def verificaValidadedoUsuario(termo):
    """função utilizada para a verificação de se o email da tentativa de cadastro ja foi utilizada"""

    #define a variavel de leitura, lendo o arquivo por completo
    arquivo = pd.read_csv("TrabalhoFinal/arquivosCsv/cadastros.csv", header = None)
    #cria uma variavel boleana para fins de verificação
    verificao = True

    #olha termo a termo dos cadastros na coluna email e o compara com o novo inserido, verificando sua validade 
    for i in range(1,len(arquivo)):
        #se o arquivo verificado for igual ao inserido a verificacao é dada como falsa 
        if str(arquivo[3][i]) == str(termo):
            verificao = False       

    #retorna a verificao
    return(verificao)

def cadastroDeUsuario(nome,endereco,senha,email,tipo_usuario, aba , aba_a_ser_aberta):
    """função ques cadastro o usuario escrevendo seu nome no arquivo .csv"""

    #chama a função de verificação do email utilizado para saber se o mesmoe esta em uso, caso n esteja, entra no if
    if verificaValidadedoUsuario(email) and nome != "" and endereco != "" and senha != "" and email != "":
        aba.destroy()
        #abre o arquivo .csv de cadastro no modo append para adicionar usuarios
        with open("TrabalhoFinal/arquivosCsv/cadastros.csv", mode="a", newline="\n") as escrita_no_arquivo:
            #define o objeto de escrita
            objeto_de_escrita = writer(escrita_no_arquivo)
            #valida se a entrada opcional foi usada dentro do estabelecido se n for será tratado como usuario
            if tipo_usuario not in ["administrador", "usuario", "vendedor"]:
                #escreve os parametros passados na funç~qao no arquivo .csv
                objeto_de_escrita.writerow([nome,endereco,senha,email,"usuario"])
            else:
                #escreve os parametros passados na funç~qao no arquivo .csv
                objeto_de_escrita.writerow([nome,endereco,senha,email,tipo_usuario])

            print("__________CADASTRADO__________")
        aba_a_ser_aberta.tela_de_login()

    #caso o email ja tenha sido cadastrado não cadastra o novo, entrando no else
    else:
        print("email ja cadastrado ou espaços não foram preenchidos")

def loginUsuario(email_login,senha_login, aba, aba_a_ser_fechada):
    """função que cria o objeto usuario a partir de informada a senha e o email de 
    uma pessoa ja cadastrada, processo de login"""
    arquivo = pd.read_csv("TrabalhoFinal/arquivosCsv/cadastros.csv", header = None)

    #deixa global os parâmetros da criação do objeto para evitar possíveis erros
    global nome
    global endereco
    global senha
    global email
    global tipo_usuario
    global usuario_ativo

    #define um verificador
    logado = False
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
            usuario_ativo = Usuario(nome, endereco, senha, email, tipo_usuario)
            print("__________LOGADO__________")
            #desativa o verificador
            logado = True
            #destroi a aba de login
            aba.destroy()
            #inicia o menu
            aba_a_ser_fechada.tela_menu()
            break
        
        #utiliza do verificador para exibir a mensagem correspondente
        elif logado == False and i == (len(arquivo)-1):
            print("Senha ou usuário incorretos ou não cadastrados")

#filtro aplicado a exibição do dataset no menu
global filtro
#cria um dicionário para a aplicação do filtro
filtro = {0:None}
#le o dataset
arquivo = pd.read_csv("TrabalhoFinal/arquivosCsv/dataset_livros.csv", header = None)
#utiliza-se da função unique do panda para ler a coluna correspondente ao item do livro e percorre a 
#lista gerada pela função adicionando seus termos ao dicionário
for i in range(len(pd.unique(arquivo[1]))):
    filtro[i+1] = (pd.unique(arquivo[1]))[i]

#tamanho do filtro e utilizado na exibição somente, para evitar erros do tkinter em utilizar a função len() em seus botões
global n 
n = (len(filtro) - 1)

#classe para contar na exibição do filtro e de exibição adequada dos botões na interface
class Contador:
    def __init__(self, inicio):
        self.indice = inicio
    def aumenta_indice(self,limite, retorno):
        """função que aumenta o indice até um limite definido e depois o reseta"""
        self.indice += 1
        if self.indice > limite:
            self.indice = retorno
    def zerar(self):
        """função para zerar o contador"""
        self.indice = 0

#cria os objetos contadores para utilizar na exibição do filtro, assim n se perde a contagem
global contador_filtro
contador_filtro = Contador(0)

#cria os objetos contadores para utilizar na exibição do botão, assim se garante sua distribuição adequada na tela
global contador_botao
contador_botao = Contador(0)
            