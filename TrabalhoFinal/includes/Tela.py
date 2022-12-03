# importa a biblioteca que cria a aba do app
from tkinter import *
import cadastro_login as cl
from Usuario import *

global usuario_ativo

class Tela:
  def __init__(self, titulo, largura_aba, altura_aba, cor):
    self.titulo = titulo
    self.altura_aba = altura_aba
    self.largura_aba = largura_aba
    self.cor_de_fundo = cor

  def tela_de_cadastro_produto(self):
    """função para a criação da tela de cadastro de produtos"""

    # define a aba como a chamada da criação da biblioteca
    self.titulo = Tk()

    # define o nome da aba criada
    self.titulo.title("Cadastro de Produto")
    #define a logo de canto da tela, puxando-a do arquivo
    self.titulo.iconbitmap("TrabalhoFinal/imagens/logo.ico")
    #define o fundo menu inicial com a cor vermelho escura
    self.titulo["bg"] = self.cor_de_fundo

    #resoluçaõ da tela do usuário
    largura_tela = self.titulo.winfo_screenwidth()
    altura_tela = self.titulo.winfo_screenheight()
    #posição da janela (conta realizada para centralizar a aba do app, o valor 50 foi acrescentado devido a aba do pc)
    self.posicao_x = largura_tela/2 - self.largura_aba/2
    self.posicao_y = altura_tela/2 - (self.altura_aba/2 + 50)
 
    # define as dimensões tela exibida
    self.titulo.geometry("%dx%d+%d+%d" %(self.largura_aba, self.altura_aba, self.posicao_x, self.posicao_y))
    # define que as dimensões da tela não podem ser alteradas pelo usuário
    self.titulo.resizable(False,False)

    nome_produto = Entry(width=19, bg='white', font=('Comic Sans MS', '12'))
    nome_produto.place(x=152, y=20)
    info_nome = Label(font=('Comic Sans MS', '12', 'bold'), fg='white', bg=self.cor_de_fundo, text='Nome do Produto:')
    info_nome.place(x=4, y=20)

    preco = Entry(width=19, bg='white', font=('Comic Sans MS', '12'))
    preco.place(x=152, y=55)
    info_preco = Label(font=('Comic Sans MS', '12', 'bold'), fg='white', bg=self.cor_de_fundo, text='Preço:')
    info_preco.place(x=45, y=55)

    categoria = Entry(width=19, bg='white', font=('Comic Sans MS', '12'))
    categoria.place(x=152, y=90)
    info_categoria = Label(font=('Comic Sans MS', '12', 'bold'), fg='white', bg=self.cor_de_fundo, text='Categoria:')
    info_categoria.place(x=30, y=90)

    avaliacao = Entry(width=19, bg='white', font=('Comic Sans MS', '12'))
    avaliacao.place(x=152, y=125)
    info_avaliacao = Label(font=('Comic Sans MS', '12', 'bold'), fg='white', bg=self.cor_de_fundo, text='Avaliação:')
    info_avaliacao.place(x=30, y=125)

    quantidade = Entry(width=19, bg='white', font=('Comic Sans MS', '12'))
    quantidade.place(x=152, y=160)
    info_quantidade = Label(font=('Comic Sans MS', '12', 'bold'), fg='white', bg=self.cor_de_fundo, text='Quantidade:')
    info_quantidade.place(x=25, y=160)

    confirma_cadastro_produto = Button(self.titulo, width=40, fg=self.cor_de_fundo, text = "CADASTRAR", command = lambda: Usuario(cl.nome, cl.endereco, cl.senha, cl.email, cl.tipo_usuario).cadastrar_produtos(nome_produto.get(), categoria.get(), avaliacao.get(), preco.get(), "In Stock", quantidade.get()))
    confirma_cadastro_produto.place(x=30,y=210)

    self.titulo.mainloop()

  def tela_de_login(self):
    """função para criar a tela de login para o usuário"""
    # define a aba como a chamada da criação da biblioteca
    self.titulo = Tk()

    # define o nome da aba criada
    self.titulo.title("Login")
    #define a logo de canto da tela, puxando-a do arquivo
    self.titulo.iconbitmap("TrabalhoFinal/imagens/logo.ico")
    #define o fundo menu inicial com a cor vermelho escura
    self.titulo["bg"] = self.cor_de_fundo

    #resoluçaõ da tela do usuário
    largura_tela = self.titulo.winfo_screenwidth()
    altura_tela = self.titulo.winfo_screenheight()
    #posição da janela (conta realizada para centralizar a aba do app, o valor 50 foi acrescentado devido a aba do pc)
    self.posicao_x = largura_tela/2 - self.largura_aba/2
    self.posicao_y = altura_tela/2 - (self.altura_aba/2 + 50)
 
    # define as dimensões tela exibida
    self.titulo.geometry("%dx%d+%d+%d" %(self.largura_aba, self.altura_aba, self.posicao_x, self.posicao_y))
    # define que as dimensões da tela não podem ser alteradas pelo usuário
    self.titulo.resizable(False,False)

    email_usuario = Entry(width=19, bg='white', font=('Comic Sans MS', '12'))
    email_usuario.place(x=152, y=20)
    info_email = Label(font=('Comic Sans MS', '12', 'bold'), fg='white', bg=self.cor_de_fundo, text='Email:')
    info_email.place(x=45, y=20)

    senha_usuario = Entry(width=19, bg='white', font=('Comic Sans MS', '12'))
    senha_usuario.place(x=152, y=60)
    info_senha = Label(font=('Comic Sans MS', '12', 'bold'), fg='white', bg=self.cor_de_fundo, text='Senha:')
    info_senha.place(x=45, y=70)

    confirma_login = Button(self.titulo, width=40, fg=self.cor_de_fundo, text = "ENTRAR", command = lambda: cl.loginUsuario(email_usuario.get(), senha_usuario.get()) )
    confirma_login.place(x=30,y=140)

    self.titulo.mainloop()

  def tela_de_cadastro(self):
    """função responsável pela criação da tela de cadastro"""
    # define a aba como a chamada da criação da biblioteca
    self.titulo = Tk()

    # define o nome da aba criada
    self.titulo.title("Cadastro")
    #define a logo de canto da tela, puxando-a do arquivo
    self.titulo.iconbitmap("TrabalhoFinal/imagens/logo.ico")
    #define o fundo menu inicial com a cor vermelho escura
    self.titulo["bg"] = self.cor_de_fundo

    #resoluçaõ da tela do usuário
    largura_tela = self.titulo.winfo_screenwidth()
    altura_tela = self.titulo.winfo_screenheight()
    #posição da janela (conta realizada para centralizar a aba do app, o valor 50 foi acrescentado devido a aba do pc)
    self.posicao_x = largura_tela/2 - self.largura_aba/2
    self.posicao_y = altura_tela/2 - (self.altura_aba/2 + 50)
 
    #define as dimensões tela exibida
    self.titulo.geometry("%dx%d+%d+%d" %(self.largura_aba, self.altura_aba, self.posicao_x, self.posicao_y))
    #define que as dimensões da tela não podem ser alteradas pelo usuário
    self.titulo.resizable(False,False)

    nome_cadastro = Entry(width=19, bg='white', font=('Comic Sans MS', '12'))
    nome_cadastro.place(x=152, y=20)
    info_nome_cadastro = Label(font=('Comic Sans MS', '12', 'bold'), fg='white', bg=self.cor_de_fundo, text='Nome:')
    info_nome_cadastro.place(x=45, y=20)

    endereco_cadastro = Entry(width=19, bg='white', font=('Comic Sans MS', '12'))
    endereco_cadastro.place(x=152, y=60)
    info_endereco_cadastro = Label(font=('Comic Sans MS', '12', 'bold'), fg='white', bg=self.cor_de_fundo, text='Endereço:')
    info_endereco_cadastro.place(x=45, y=60)

    email_cadastro = Entry(width=19, bg='white', font=('Comic Sans MS', '12'))
    email_cadastro.place(x=152, y=100)
    info_email = Label(font=('Comic Sans MS', '12', 'bold'), fg='white', bg=self.cor_de_fundo, text='Email:')
    info_email.place(x=45, y=100)

    senha_cadastro = Entry(width=19, bg='white', font=('Comic Sans MS', '12'))
    senha_cadastro.place(x=152, y=140)
    info_senha_cadastro = Label(font=('Comic Sans MS', '12', 'bold'), fg='white', bg=self.cor_de_fundo, text='Senha:')
    info_senha_cadastro.place(x=45, y=140)

    tipo_usuario_cadastro = Entry(width=19, bg='white', font=('Comic Sans MS', '12'))
    tipo_usuario_cadastro.place(x=152, y=180)
    info_tipo_usuario_cadastro = Label(font=('Comic Sans MS', '12', 'bold'), fg='white', bg=self.cor_de_fundo, text='Tipo de Usuário:')
    info_tipo_usuario_cadastro.place(x=15, y=180)

    confirma_cadastro = Button(self.titulo, width=40, fg=self.cor_de_fundo, text = "CADASTRAR", command = lambda: cl.cadastroDeUsuario(nome_cadastro.get(), endereco_cadastro.get(), senha_cadastro.get(), email_cadastro.get(), tipo_usuario_cadastro.get()) )
    confirma_cadastro.place(x=30,y=250)

    self.titulo.mainloop()

login_usuario = Tela("titulo", 350, 180, "darkred")
cadastro_produto = Tela("titulo", 350, 250, "darkred")
cadastro_usuario = Tela("titulo", 350, 300, "darkred")

    