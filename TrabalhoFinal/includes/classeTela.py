# importa a biblioteca que cria a aba do app
from tkinter import *


class Tela:
  def __init__(self, titulo, largura, altura, cor_de_fundo):
    
    self.titulo = titulo
    self.largura_aba = largura
    self.altura_aba = altura
    self.cor_de_fundo = cor_de_fundo
    
  def iniciar_tela(self):
    global aba
    # define a aba como a chamada da criação da biblioteca
    aba = Tk()

    # define o nome da aba criada
    aba.title(self.titulo)
    #define a logo de canto da tela, puxando-a do arquivo
    aba.iconbitmap("imagens/logo.ico")
    #define o fundo menu inicial com a cor vermelho escura
    aba["bg"] = self.cor_de_fundo

    #resoluçaõ da tela do usuário
    largura_tela = aba.winfo_screenwidth()
    altura_tela = aba.winfo_screenheight()
    #posição da janela (conta realizada para centralizar a aba do app, o valor 50 foi acrescentado devido a aba do pc)
    self.posicao_x = largura_tela/2 - self.largura_aba/2
    self.posicao_y = altura_tela/2 - (self.altura_aba/2 + 50)
    # define as dimensões tela exibida
    aba.geometry("%dx%d+%d+%d" %(self.largura_aba, self.altura_aba, self.posicao_x, self.posicao_y))
    # define que as dimensões da tela não podem ser alteradas pelo usuário
    aba.resizable(False,False)

    #mantem a tela em exibição
    aba.mainloop()

  def destroi_tela(self):
    # define a aba como a chamada da criação da biblioteca
    aba = Tk()
    aba.destroy()

telaCadastro = Tela("aaaa", 500, 100, "red")
telaLogin = Tela("socco", 200, 300, "red")

telaLogin.label("fsfsafadsfsd", 0, 0)
telaLogin.iniciar_tela()




    