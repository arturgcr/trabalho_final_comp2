# importa a biblioteca que cria a aba do app
from tkinter import *
from csv import *
import pandas as pd

 # define a aba como a chamada da criação da biblioteca
menu = Tk()

# define o nome da aba criada
menu.title("Kilivros")

#tamanho da aba do app (todas as medidas são em pixels)
largura = 800
altura = 600

#resoluçaõ da tela do usuário
largura_tela = menu.winfo_screenwidth()
altura_tela = menu.winfo_screenheight()

#posição da janela (conta realizada para centralizar a aba do app, o valor 50 foi acrescentado devido a aba do pc)
posicao_x = largura_tela/2 - largura/2
posicao_y = altura_tela/2 - (altura/2 + 50)

# define as dimensões tela exibida
menu.geometry("%dx%d+%d+%d" %(largura, altura, posicao_x, posicao_y))
# define que as dimensões da tela não podem ser alteradas pelo usuário
menu.resizable(False,False)
#define a logo de canto da tela, puxando-a do arquivo
#menu.iconbitmap("imagens/logo.ico")
#define o fundo menu inicial com a cor vermelho escura
menu["bg"] = "darkred"
    
#define o botão
alterar_cadastro = Button(menu, text = "Usuário 𓀟",width = 13, command = lambda: print("oi"))
#exibe o botão na tela nas coordenadas expressas
alterar_cadastro.place(x=0,y=0)

#define o botão
termo = Button(menu, text = "Termo 🎮",width = 13, command = lambda: print("oi"))
#exibe o botão na tela nas coordenadas expressas
termo.place(x=97,y=0)

#define o botão
saida_usuario = Button(menu, text = "Sair ⍈",width = 13, command = lambda: print("oi"))
#exibe o botão na tela nas coordenadas expressas
saida_usuario.place(x=190,y=0)

#define o botão
carrinho = Button(menu, text = "Carrinho 🛒",width = 13, command = lambda: print("oi"))
#exibe o botão na tela nas coordenadas expressas
carrinho.place(x=283,y=0)

scroll_bar = Scrollbar(menu)
scroll_bar.pack(side = 'right', fill = 'y')

#define a variavel de leitura, lendo o arquivo por completo
arquivo = pd.read_csv("TrabalhoFinal/arquivosCsv/dataset_livros.csv", header = None)
#percorre os itens do dataset
for i in range(1,len(arquivo)):
    arquivo[0][i] = Button(menu, text = "+", command = lambda: arquivo[i])
    arquivo[0][i].place(x=764,y=i*20)

# exibe a aba
menu.mainloop()