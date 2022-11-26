import pandas as pd
from csv import *
from datetime import date

class Usuario:
    def __init__(self,nome,endereco,senha,email,tipo_usuario):
        self.carrinho_de_compras = []
        self.nome = nome
        self.endereco = endereco
        self.senha = senha
        self.email = email
        self.tipo_usuario = tipo_usuario
        
    def adiciona_produto_ao_carrinho(self, produto):
        """Função responsável para adicionar itens a lista denominada carrinho"""
        #define a variavel de leitura, lendo o arquivo por completo
        arquivo = pd.read_csv("arquivosCsv/dataset_livros.csv", header = None)

        #percorre a linhas dos arquivos do dataset
        for i in range(1,len(arquivo)):
            #se o item do dataset for encontrado executa oque ta dentro do if
            if arquivo[0][i] == produto and arquivo[5][i] > 0 :
                #adiciona ao carrinho de compra o nome e o valor do produto encontrado
                self.carrinho_de_compras.append([arquivo[0][i], arquivo[3][i]])
                break
            
            elif i == len(arquivo):
                print("arquivo não encontrado ou esgotado de nossa loja")

    def remover_produto_do_carrinho(self, produto):
        """Função que remove um item selecionado da lista denominada carrinho"""
        #percorre os itens do carrinho de compras
        for i in range(len(self.carrinho_de_compras)):
            #compara os itens do carrinho com o produto qe deseja ser removido
            if self.carrinho[i][0] == produto:
                #depois de verificado remove o iten da lista
                self.carrinho_de_compras.remove(self.carrinho[i])

            #caso o produto não esteja no carrinho executa oque esta dentro do elif
            elif i == len(self.carrinho_de_compras):
                print("produto não encontrado no carrinho")
    
    def limpa_carrinho(self):
        """Função ques excluitodos os itens da lista carrinho"""
        self.carrinho_de_compras.clear() 

    def realizar_compra(self):
        """função que realiza a compra do carrinho a salvando em um historico, arquivo .csv"""

        #define a data para utilizar nas compras
        data = date.today()
        dia = data[0:4]
        mes = data[5:7]
        ano = data[8:10]

        #abreo arquivo de historico de compras para registrar a compra
        with open("arquivosCsv/historicoDeCompra.csv", mode="a", newline="\n") as escrita_no_arquivo:
            #define o objeto de escrita
            objeto_de_escrita = writer(escrita_no_arquivo)
            for i in range(len(self.carrinho_de_compras)):
                #escreve os parametros passados na funç~qao no arquivo .csv
                objeto_de_escrita.writerow([self.email, self.carrinho_de_compras[i],dia,mes,ano]) #verificar a forma como vai ser escreito no arquivo
            #exclui todos os itens da lista carrinho
            self.carrinho_de_compras.clear()  
            print("sucesso!!!")

        #define a variavel de leitura, lendo o arquivo por completo
        arquivo = pd.read_csv("arquivosCsv/dataset_livros.csv", header = None)
        #percorre os itens do carrinho
        for n in range(len(self.carrinho_de_compras)):
            #percorre as linhas do dataset
            for i in range(1,len(arquivo)):
                #compara o item do dataset com o item do carrinho, se for executa o if
                if self.carrinho_de_compras[n][0] == arquivo[i][0]:
                    #diminui a quantidade disponível do item no dataset
                    arquivo[5][i] = int(arquivo[5][i]) - 1
        
        print("compra realizada e enviada para o endereço " + str(self.endereco))

        #fecha o arquivo para evitar possíveis erros
        escrita_no_arquivo.close() 
    
    def modifica_estoque(self, produto, qtd):
        """função reponsável para alterar a quantidade de um determinado produto no arquivo csv"""
        if self.tipo_usuario == "administrador":
            #define a variavel de leitura, lendo o arquivo por completo
            arquivo = pd.read_csv("arquivosCsv/dataset_livros.csv", header = None)
            #percorre os itens do dataset
            for i in range(1,len(arquivo)):
                #se o item do dataset for encontrado executa oque ta dentro do if
                if arquivo[0][i] == produto:
                    #diminui a quantidade desejada do estoque
                    arquivo[5][i] = int(arquivo[5][i]) + qtd
                    break
                #para caso do aplicativo não ser encontrado
                elif i == len(arquivo):
                    print("arquivo não encontrado")
    
    def modifica_valor_do_produto(self, produto, preco):
        """função responsável por alterar o preço de um item no arquivo csv"""
        if self.tipo_usuario == "administrador":
            #define a variavel de leitura, lendo o arquivo por completo
            arquivo = pd.read_csv("arquivosCsv/dataset_livros.csv", header = None)
            #percorre os itens do dataset
            for i in range(1,len(arquivo)):
                #se o item do dataset for encontrado executa oque ta dentro do if
                if arquivo[0][i] == produto:
                    #iguala o preço ao produto
                    arquivo[3][i] =  preco
                    break
                #para caso do aplicativo não ser encontrado
                elif i == len(arquivo):
                    print("arquivo não encontrado")
    
    def cadastrar_produtos(self,titulo,categoria,avaliacao,preco,estoque,quantidade):
        if self.tipo_usuario == "administrador":
            #abre o arquivo .csv de cadastro no modo append para adicionar usuarios
            with open("arquivosCsv/dataset_livros.csv", mode="a", newline="\n") as escrita_no_arquivo:
                #define o objeto de escrita
                objeto_de_escrita = writer(escrita_no_arquivo)
                #adiciona produto ao dataset
                objeto_de_escrita.writerow([titulo,categoria,avaliacao,preco,estoque,quantidade])
