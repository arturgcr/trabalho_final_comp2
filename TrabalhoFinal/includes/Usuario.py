"""arquivo de criação da classe usuario com seus respectivos atributos que serão utilizados"""

#as variáveis a baixo são so caminhos do arquivo csv que devem ser trocadas para as do usuario
#caminho do histórico de compras
caminho_do_arquivo_historico_de_compra = r"C:\Users\artur\OneDrive\Área de Trabalho\Comp2\trabalho_no_git\trabalho_final_comp2\TrabalhoFinal\arquivosCsv\historicoDeCompra.csv"
#caminho do dataset_livros.csv
caminho_do_arquivo_dataset_livros = r"C:\Users\artur\OneDrive\Área de Trabalho\Comp2\trabalho_no_git\trabalho_final_comp2\TrabalhoFinal\arquivosCsv\dataset_livros.csv"

import pandas as pd
from csv import *
from datetime import date
from tkinter import *
from matplotlib import pyplot as plt
import numpy as np

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
        arquivo = pd.read_csv("TrabalhoFinal/arquivosCsv/dataset_livros.csv", header = None)

        #percorre a linhas dos arquivos do dataset
        for i in range(1,len(arquivo)):
            #se o item do dataset for encontrado executa oque ta dentro do if
            if arquivo[0][i] == produto and int(arquivo[5][i]) > 0 :
                #adiciona ao carrinho de compra o nome e o valor do produto encontrado
                self.carrinho_de_compras.append([arquivo[0][i], arquivo[3][i]])
                print(str(arquivo[0][i]) + " foi adicionada ao carrinho")
                break

    def remover_produto_do_carrinho(self, produto):
        """Função que remove um item selecionado da lista denominada carrinho"""
        #percorre os itens do carrinho de compras
        for i in range(len(self.carrinho_de_compras)):
            #compara os itens do carrinho com o produto qe deseja ser removido
            if self.carrinho_de_compras[i][0] == produto:
                #depois de verificado remove o iten da lista
                self.carrinho_de_compras.remove(self.carrinho_de_compras[i])
                print("produto removido")
                break

            #caso o produto não esteja no carrinho executa oque esta dentro do elif
            elif i == len(self.carrinho_de_compras):
                print("produto não encontrado no carrinho")

    def realizar_compra(self):
        """função que realiza a compra do carrinho a salvando em um historico, arquivo .csv"""

        #define a data para utilizar nas compras
        data = str(date.today())
        dia = data[8:10]
        mes = data[5:7]
        ano = data[0:4]

        #abreo arquivo de historico de compras para registrar a compra
        with open("TrabalhoFinal/arquivosCsv/historicoDeCompra.csv", mode="a", newline="\n") as escrita_no_arquivo:
            #define o objeto de escrita
            objeto_de_escrita = writer(escrita_no_arquivo)
            for i in range(len(self.carrinho_de_compras)):
                #escreve os parametros passados na funç~qao no arquivo .csv
                objeto_de_escrita.writerow([self.email, self.carrinho_de_compras[i][0],self.carrinho_de_compras[i][1],dia,mes,ano])

        #define a variavel de leitura, lendo o arquivo por completo
        arquivo = pd.read_csv("TrabalhoFinal/arquivosCsv/dataset_livros.csv", header = None)
        #percorre os itens do carrinho
        for n in range(len(self.carrinho_de_compras)):
            #percorre as linhas do dataset
            for i in range(1,len(arquivo)):
                #compara o item do dataset com o item do carrinho, se for igual executa oq ta dentro do if
                if str(self.carrinho_de_compras[n][0]) == str(arquivo[0][i]):
                    #diminui a quantidade disponível do item no dataset
                    arquivo[5][i] = int(arquivo[5][i]) - 1
                    arquivo.to_csv("TrabalhoFinal/arquivosCsv/dataset_livros.csv", header = None, index = False)
                    #exclui todos os itens da lista carrinho
        if self.carrinho_de_compras == []:
            print("O carrinho está vazio")
        else:
            self.carrinho_de_compras.clear()  
            if self.tipo_usuario == "usuario":
                print("Compra realizada e enviada para o endereço " + str(self.endereco) + ", agradecemos pela sua compra")
            else:
                print("Compra concluida")

        #fecha o arquivo para evitar possíveis erros
        escrita_no_arquivo.close() 
    

    def modifica_valor_do_produto(self, produto, preco):
        verifica = True
        """função responsável por alterar o preço de um item no arquivo csv"""
        if self.tipo_usuario == "administrador":
            #define a variavel de leitura, lendo o arquivo por completo
            arquivo = pd.read_csv("TrabalhoFinal/arquivosCsv/dataset_livros.csv", header = None)
            #percorre os itens do dataset
            for i in range(1, len(arquivo)):
                #se o item do dataset for encontrado executa oque ta dentro do if 
                if arquivo[0][i] == produto:
                    #define o item que representa o preço do produto q se deseja alterar como o preço desejado
                    arquivo[3][i] = preco
                    #define o dataset como o arquivo com o detalhe a cima modificado
                    arquivo.to_csv("TrabalhoFinal/arquivosCsv/dataset_livros.csv", header = None, index = False)
                    #quebra o loop para evitar execução do elif a baixo
                    verifica = False
                    break
                #para caso do aplicativo não ser encontrado
            if verifica:
                print("Arquivo não encontrado")
    
    def cadastrar_produtos(self,titulo,categoriaoria,avaliacao,preco,estoque,quantidade, aba):
        if self.tipo_usuario == "administrador":
            #abre o arquivo .csv de cadastro no modo append para adicionar usuarios
            with open("TrabalhoFinal/arquivosCsv/dataset_livros.csv", mode="a", newline="\n") as escrita_no_arquivo:
                #define o objeto de escrita
                objeto_de_escrita = writer(escrita_no_arquivo)
                if titulo != "" and avaliacao != "" and preco != "" and estoque != "" and quantidade != "":
                    #define a variavel de leitura, lendo o arquivo por completo
                    arquivo = pd.read_csv("TrabalhoFinal/arquivosCsv/dataset_livros.csv", header = None)
                    verificador = False
                    for i in range(len(arquivo)):
                        if str(titulo) == str(arquivo[0][i]):
                            verificador = False
                            break
                        else:
                            verificador = True
                    if verificador == False:
                        print("Produto ja cadastrado")
                    else:
                        #adiciona produto ao dataset
                        objeto_de_escrita.writerow([titulo,categoriaoria,avaliacao,preco,estoque,quantidade])
                        aba.destroy()
                        print("produto cadastrado com sucesso")
                else:
                    print("Insira valores válidos")

    def exibe_historico(self):
        #define a variavel de leitura, lendo o arquivo por completo
        arquivo = pd.read_csv("TrabalhoFinal/arquivosCsv/historicoDeCompra.csv", header = None)
        if self.tipo_usuario == "usuario":
            for i in range(1,(len(arquivo))):
                if arquivo[0][i] == self.email:
                    print([arquivo[0][i],arquivo[1][i],arquivo[2][i],arquivo[3][i],arquivo[4][i],arquivo[5][i]])
        
        if self.tipo_usuario == "vendedor" or self.tipo_usuario == "administrador":
            cliente = input("De qual cliente você gostaria de verificar o histórico? ")
            for i in range(1,(len(arquivo))):
                if cliente == arquivo[0][i]:
                    print(arquivo[0][i],arquivo[1][i],arquivo[2][i],arquivo[3][i],arquivo[4][i],arquivo[5][i])
    
    def soma_do_carrinho(self):
        lista_de_soma = []
        for i in range(len(self.carrinho_de_compras)):
            lista_de_soma.append(float(self.carrinho_de_compras[i][1]))
        return round(sum(lista_de_soma), 2)

    def modifica_qtd_em_estoque(self, produto, qtd):
        #define a variavel de leitura, lendo o arquivo por completo
        arquivo = pd.read_csv("TrabalhoFinal/arquivosCsv/dataset_livros.csv", header = None)
        verifica = True
        for i in range(1,(len(arquivo)-1)):
            if str(arquivo[0][i]) == str(produto):
                arquivo[5][i] = qtd
                #define o dataset como o arquivo com o detalhe a cima modificado
                arquivo.to_csv("TrabalhoFinal/arquivosCsv/dataset_livros.csv", header = None, index = False)
                print("modificado -> " + str(arquivo[0][i]) +" "+ str(arquivo[5][i]))
                verifica = False
                break
        if verifica:
            print("nome do produto errado")

    def exibe_dataset(self):
        arquivo = pd.read_csv("TrabalhoFinal/arquivosCsv/dataset_livros.csv", header = None)
        for i in range(1,(len(arquivo)-1)):
             print(arquivo[0][i],arquivo[1][i],arquivo[2][i],arquivo[3][i],arquivo[4][i],arquivo[5][i])

    def grafico_mediavend(self,dia,mes,ano):
        """cria um grafico de barras que contabiliza o numero de vendas de uma semana"""
        datelist = []
        vendassem = []
        n = dia
        numvend = 0
        historico = pd.read_csv(caminho_do_arquivo_historico_de_compra,header=None)
        # usa um loop while para contabilizar o numero de vendas totais de cada dia da semana
        while int(n) != int(dia) - 7:
            numvend = 0
            for i in range(1,len(historico)):
                if str(historico[3][i]) == str(n) and str(historico[4][i]) == str(mes) and str(historico[5][i]) == str(ano):
                    numvend = numvend + 1
            n = n - 1
            vendassem = vendassem + [numvend]
        l = dia
        
        for j in range(len(vendassem)):
            datelist.append([vendassem[j],str(l)+"/"+str(mes)+"/"+str(ano)])
            l = l - 1
        df = pd.DataFrame(data = datelist, columns =["vendas","dias"])
        print("média :" + str(sum(vendassem)/7))
        print("desvio padrão :" + str(np.std(vendassem)))
        janela = plt.figure(figsize=(10,5))
        grafico = janela.add_axes([0,0,1,1])
        grafico.bar(df["dias"],df["vendas"])

    def graficos_venda_fat(self,dia,mes,ano):
        """ plota um grafico do numero de vendas e do faturamento em um dia especifico"""
        vendas = 0
        faturamento = 0
        historico = pd.read_csv(caminho_do_arquivo_historico_de_compra,header=None)
        for i in range(len(historico)):
            if str(historico[3][i]) == str(dia) and str(historico[4][i]) == str(mes) and str(historico[5][i]) == str(ano):
                vendas += 1
                faturamento = faturamento + int(historico[4][i])
        df = pd.DataFrame(data =[["vendas",vendas],["faturamento",faturamento]], columns =["tipo","valor"])
        janela = plt.figure(figsize=(10,5))
        grafico = janela.add_axes([0,0,1,1])
        grafico.bar(df['tipo'],df['valor'])

    def cat_prod(self):
        """plota um grafico do numero de vendas por categoriaoria do dataset"""
        nomelist =[]
        categoria = []
        datelist = []
        livro = pd.read_csv(caminho_do_arquivo_dataset_livros, header = None)
        historico = pd.read_csv(caminho_do_arquivo_historico_de_compra,header=None)
        n = 0
        for m in range(len(livro)-1):
            if livro[1][m] not in categoria:
                categoria.append(livro[1][m])
                categoria.append(0)
        for j in range(len(historico)-1):
            nomelist.append(historico[1][j])
        for i in range(len(livro)-1):
            if nomelist[n] == livro[1][i]: 
                if livro[1][i] in categoria:
                    for k in range(len(categoria)-1):
                        if categoria[k] == livro[1][i]:
                            categoria[k+1] = categoria[k+1] + 1
            n = n + 1
            if n > len(nomelist):
                break
        for t in range(len(categoria)/2):
            datelist.append([[categoria[t],categoria[t+1]]])    
        df = pd.DataFrame(data = datelist, columns =["categoria","venda"])
        janela = plt.figure(figsize=(10,5))
        grafico = janela.add_axes([0,0,1,1])
        grafico.bar(df["categoriaoria"],df["venda"])
