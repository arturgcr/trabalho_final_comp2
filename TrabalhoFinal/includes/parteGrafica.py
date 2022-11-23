"""
comentários do arquivo

"""

# importa a biblioteca que cria a aba do app
from tkinter import *

def janela_cadastro():
     # define a aba como a chamada da criação da biblioteca
    tela_de_cadastro = Tk()

    # define o nome da aba criada
    tela_de_cadastro.title("CADASTRO")

    #tamanho da aba do app (todas as medidas são em pixels)
    largura = 500
    altura = 550

    #resoluçaõ da tela do usuário
    largura_tela = tela_de_cadastro.winfo_screenwidth()
    altura_tela = tela_de_cadastro.winfo_screenheight()

    #posição da janela (conta realizada para centralizar a aba do app, o valor 50 foi acrescentado devido a aba do pc)
    posicao_x = largura_tela/2 - largura/2
    posicao_y = altura_tela/2 - (altura/2 + 50)

    # define as dimensões tela exibida
    tela_de_cadastro.geometry("%dx%d+%d+%d" %(largura, altura, posicao_x, posicao_y))
    # define que as dimensões da tela não podem ser alteradas pelo usuário
    tela_de_cadastro.resizable(False,False)
    #define a logo de canto da tela, puxando-a do arquivo
    tela_de_cadastro.iconbitmap("imagens/logo.ico")
    #define o fundo menu inicial com a cor vermelho escura
    tela_de_cadastro["bg"] = "darkred"

    # exibe a aba
    tela_de_cadastro.mainloop()


def janela_login():
    # define a aba como a chamada da criação da biblioteca
    tela_de_login = Tk()

    # define o nome da aba criada
    tela_de_login.title("")

    #tamanho da aba do app (todas as medidas são em pixels)
    largura = 500
    altura = 550

    #resoluçaõ da tela do usuário
    largura_tela = tela_de_login.winfo_screenwidth()
    altura_tela = tela_de_login.winfo_screenheight()

    #posição da janela (conta realizada para centralizar a aba do app, o valor 50 foi acrescentado devido a aba do pc)
    posicao_x = largura_tela/2 - largura/2
    posicao_y = altura_tela/2 - (altura/2 + 50)

    # define as dimensões tela exibida
    tela_de_login.geometry("%dx%d+%d+%d" %(largura, altura, posicao_x, posicao_y))
    # define que as dimensões da tela não podem ser alteradas pelo usuário
    tela_de_login.resizable(False,False)
    #define a logo de canto da tela, puxando-a do arquivo
    tela_de_login.iconbitmap("imagens/logo.ico")
    #define o fundo menu inicial com a cor vermelho escura
    tela_de_login["bg"] = "darkred"

    faixa_superior = Frame(tela_de_login, width=largura, height=(altura/5), bg="white")
    faixa_superior.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

    texto = Label(faixa_superior, text="LOGIN", font=("Arial 45"), fg="darkred", bg="white")
    texto.place(x=largura/3.5, y=altura/25)

    # exibe a aba e mantem
    tela_de_login.mainloop()

janela_login()

