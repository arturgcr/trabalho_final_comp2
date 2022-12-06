# importa a biblioteca que cria a aba do app
from tkinter import *
import cadastro_login as cl
from Usuario import *

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

    nome_produto = Entry(self.titulo,width=19, bg='white', font=('Comic Sans MS', '12'))
    nome_produto.place(x=152, y=20)
    info_nome = Label(self.titulo,font=('Comic Sans MS', '12', 'bold'), fg='white', bg=self.cor_de_fundo, text='Nome do Produto:')
    info_nome.place(x=4, y=20)

    preco = Entry(self.titulo,width=19, bg='white', font=('Comic Sans MS', '12'))
    preco.place(x=152, y=55)
    info_preco = Label(self.titulo,font=('Comic Sans MS', '12', 'bold'), fg='white', bg=self.cor_de_fundo, text='Preço:')
    info_preco.place(x=45, y=55)

    categoria = Entry(self.titulo,width=19, bg='white', font=('Comic Sans MS', '12'))
    categoria.place(x=152, y=90)
    info_categoria = Label(self.titulo,font=('Comic Sans MS', '12', 'bold'), fg='white', bg=self.cor_de_fundo, text='Categoria:')
    info_categoria.place(x=30, y=90)

    avaliacao = Entry(self.titulo,width=19, bg='white', font=('Comic Sans MS', '12'))
    avaliacao.place(x=152, y=125)
    info_avaliacao = Label(self.titulo,font=('Comic Sans MS', '12', 'bold'), fg='white', bg=self.cor_de_fundo, text='Avaliação:')
    info_avaliacao.place(x=30, y=125)

    quantidade = Entry(self.titulo,width=19, bg='white', font=('Comic Sans MS', '12'))
    quantidade.place(x=152, y=160)
    info_quantidade = Label(self.titulo,font=('Comic Sans MS', '12', 'bold'), fg='white', bg=self.cor_de_fundo, text='Quantidade:')
    info_quantidade.place(x=25, y=160)

    confirma_cadastro_produto = Button(self.titulo, width=23, fg=self.cor_de_fundo, text = "CADASTRAR", command = lambda: cl.usuario_ativo.cadastrar_produtos(nome_produto.get(), categoria.get(), avaliacao.get(), preco.get(), "In Stock", quantidade.get(), self.titulo))
    confirma_cadastro_produto.place(x=2,y=210)

    volta_menu = Button(self.titulo, width=23, fg=self.cor_de_fundo, text = "MENU", command = lambda:[self.titulo.destroy(), menu.tela_menu()]) 
    volta_menu.place(x=178,y=210)

    self.titulo.mainloop(1)

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

    email_usuario = Entry(self.titulo, width=19, bg='white', font=('Comic Sans MS', '12'))
    email_usuario.place(x=152, y=20)
    info_email = Label(self.titulo, font=('Comic Sans MS', '12', 'bold'), fg='white', bg=self.cor_de_fundo, text='Email:')
    info_email.place(x=45, y=20)

    senha_usuario = Entry(self.titulo, width=19, bg='white', font=('Comic Sans MS', '12'))
    senha_usuario.place(x=152, y=60)
    info_senha = Label(self.titulo, font=('Comic Sans MS', '12', 'bold'), fg='white', bg=self.cor_de_fundo, text='Senha:')
    info_senha.place(x=45, y=70)

    ir_cadastrar = Button(self.titulo, width=40, fg=self.cor_de_fundo, text = "CADASTRAR", command = lambda: [cadastro_usuario.tela_de_cadastro(True, self.titulo)] )
    ir_cadastrar.place(x=30,y=110)

    confirma_login = Button(self.titulo, width=40, fg=self.cor_de_fundo, text = "ENTRAR", command = lambda: [cl.loginUsuario(email_usuario.get(), senha_usuario.get(), self.titulo, menu)] )
    confirma_login.place(x=30,y=140)

    self.titulo.mainloop()

  def tela_de_cadastro(self, verificador=False, aba=None):
    """função responsável pela criação da tela de cadastro"""
    if verificador:
      aba.destroy()

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

    nome_cadastro = Entry(self.titulo,width=19, bg='white', font=('Comic Sans MS', '12'))
    nome_cadastro.place(x=152, y=20)
    info_nome_cadastro = Label(self.titulo,font=('Comic Sans MS', '12', 'bold'), fg='white', bg=self.cor_de_fundo, text='Nome:')
    info_nome_cadastro.place(x=45, y=20)

    endereco_cadastro = Entry(self.titulo,width=19, bg='white', font=('Comic Sans MS', '12'))
    endereco_cadastro.place(x=152, y=60)
    info_endereco_cadastro = Label(self.titulo,font=('Comic Sans MS', '12', 'bold'), fg='white', bg=self.cor_de_fundo, text='Endereço:')
    info_endereco_cadastro.place(x=45, y=60)

    email_cadastro = Entry(self.titulo,width=19, bg='white', font=('Comic Sans MS', '12'))
    email_cadastro.place(x=152, y=100)
    info_email = Label(self.titulo,font=('Comic Sans MS', '12', 'bold'), fg='white', bg=self.cor_de_fundo, text='Email:')
    info_email.place(x=45, y=100)

    senha_cadastro = Entry(self.titulo,width=19, bg='white', font=('Comic Sans MS', '12'))
    senha_cadastro.place(x=152, y=140)
    info_senha_cadastro = Label(self.titulo,font=('Comic Sans MS', '12', 'bold'), fg='white', bg=self.cor_de_fundo, text='Senha:')
    info_senha_cadastro.place(x=45, y=140)

    tipo_usuario_cadastro = Entry(self.titulo,width=19, bg='white', font=('Comic Sans MS', '12'))
    tipo_usuario_cadastro.place(x=152, y=180)
    info_tipo_usuario_cadastro = Label(self.titulo,font=('Comic Sans MS', '12', 'bold'), fg='white', bg=self.cor_de_fundo, text='Tipo de Usuário:')
    info_tipo_usuario_cadastro.place(x=15, y=180)

    retorna_ao_login = Button(self.titulo, width=40, fg=self.cor_de_fundo, text = "LOGIN", command = lambda: [self.titulo.destroy(), login_usuario.tela_de_login()] )
    retorna_ao_login.place(x=30,y=220)

    confirma_cadastro = Button(self.titulo, width=40, fg=self.cor_de_fundo, text = "CADASTRAR", command = lambda: [cl.cadastroDeUsuario(nome_cadastro.get(), endereco_cadastro.get(), senha_cadastro.get(), email_cadastro.get(), tipo_usuario_cadastro.get(), self.titulo, login_usuario)] )
    confirma_cadastro.place(x=30,y=250)

    self.titulo.mainloop(1)

  def tela_menu(self):
    """função para criar a tela de login para o usuário"""
    # define a aba como a chamada da criação da biblioteca
    self.titulo = Tk()

    # define o nome da aba criada
    self.titulo.title("KeroLivros")
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

    if cl.usuario_ativo.tipo_usuario == "usuario" or cl.usuario_ativo.tipo_usuario == "vendedor":
      #define o botão
      historico = Button(self.titulo, text = "Histórico de Compras", command = lambda: [cl.usuario_ativo.exibe_historico()])
      #exibe o botão na tela nas coordenadas expressas
      historico.place(x=0,y=0)
    
    elif cl.usuario_ativo.tipo_usuario == "administrador":
      #define o botão
      muda_produto = Button(self.titulo, text = "   Cadastrar Produtos  ", command = lambda: [self.titulo.destroy(),cadastro_produto.tela_de_cadastro_produto()])
      #exibe o botão na tela nas coordenadas expressas
      muda_produto.place(x=0,y=0)

    #define o botão
    filtro = Button(self.titulo, text = "Filtro",width = 13, command = lambda: [self.titulo.destroy(), cl.contador_filtro.aumenta_indice(10,0), menu.tela_menu(), cl.contador_botao.zerar()])
    #exibe o botão na tela nas coordenadas expressas
    filtro.place(x=126,y=0)

    #define o botão
    saida_usuario = Button(self.titulo, text = "Sair ⍈",width = 13, command = lambda: self.titulo.destroy())
    #exibe o botão na tela nas coordenadas expressas
    saida_usuario.place(x=227,y=0)

    if cl.usuario_ativo.tipo_usuario == "usuario" or cl.usuario_ativo.tipo_usuario == "vendedor":
      #define o botão
      carrinho = Button(self.titulo, text = "Carrinho 🛒",width = 13, command = lambda: [self.titulo.destroy(), exibe_carrinho.tela_carrinho_de_compras()])
      #exibe o botão na tela nas coordenadas expressas
      carrinho.place(x=328,y=0)
    
    elif cl.usuario_ativo.tipo_usuario == "administrador":
      modifica = Button(self.titulo, text = "Modifica Estoque",width = 30, command = lambda: [self.titulo.destroy(), modifica_estoque.tela_de_estoque()])
      #exibe o botão na tela nas coordenadas expressas
      modifica.place(x=335,y=0)

    scroll_bar = Scrollbar(self.titulo)
    scroll_bar.pack(side = 'right', fill = 'y')

    #define a variavel de leitura, lendo o arquivo por completo
    arquivo = pd.read_csv("TrabalhoFinal/arquivosCsv/dataset_livros.csv", header = None)

    #percorre os itens do dataset
    for i in range(1, len(arquivo)):
      if arquivo[1][i] == cl.filtro[cl.contador_filtro.indice] or cl.filtro[cl.contador_filtro.indice] == None:
        cl.contador_botao.aumenta_indice(19,1)
        Button(self.titulo, text = "+", command = lambda: [cl.usuario_ativo.adiciona_produto_ao_carrinho(arquivo[0][i])]).place(x=614,y=int(cl.contador_botao.indice)*30)
        Label(self.titulo,width= 50,font=('Comic Sans MS', '8', 'bold'), fg='darkred', bg="white", text= arquivo[0][i]).place(x=10, y=int(cl.contador_botao.indice)*30)
        Label(self.titulo,width= 10,font=('Comic Sans MS', '8', 'bold'), fg='darkred', bg="white", text= arquivo[1][i]).place(x=398, y=int(cl.contador_botao.indice)*30)
        Label(self.titulo,width= 10,font=('Comic Sans MS', '8', 'bold'), fg='darkred', bg="white", text= arquivo[2][i]).place(x=512, y=int(cl.contador_botao.indice)*30)
        Label(self.titulo,width= 10,font=('Comic Sans MS', '8', 'bold'), fg='darkred', bg="white", text= arquivo[3][i]).place(x=650, y=int(cl.contador_botao.indice)*30)

    self.titulo.mainloop(1)

  def tela_carrinho_de_compras(self):
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

    Label(self.titulo,font=('Comic Sans MS', '12', 'bold'), fg='darkred', bg="white", text= "      CARRINHO DE COMPRAS      ").place(x= 3, y= 3)
    Button(self.titulo, font=('Comic Sans MS', '10', 'bold'), fg='darkred', bg="white", text= "CONCLUIR COMPRA", command= lambda: cl.usuario_ativo.realizar_compra()).place(x= 2, y= 365)
    Button(self.titulo, font=('Comic Sans MS', '10', 'bold'), fg='darkred', bg="white", text= "MENU", command= lambda: [self.titulo.destroy(), menu.tela_menu()]).place(x= 145, y= 365)
    Label(self.titulo,font=('Comic Sans MS', '10', 'bold'), fg='darkred', bg="white", text= "TOTAL:" + str(cl.usuario_ativo.soma_do_carrinho())).place(x= 200, y= 365)

    for i in range(len(cl.usuario_ativo.carrinho_de_compras)):

      Button(self.titulo, text = " - ", command = lambda: [cl.usuario_ativo.remover_produto_do_carrinho(cl.usuario_ativo.carrinho_de_compras[i][0]), self.titulo.destroy(), exibe_carrinho.tela_carrinho_de_compras()]).place(x=263,y=i*30 + 50)
      Label(self.titulo, width= 20,font=('Comic Sans MS', '8', 'bold'), fg='darkred', bg="white", text= cl.usuario_ativo.carrinho_de_compras[i][0]).place(x=10, y=i*30 + 50)
      Label(self.titulo, font=('Comic Sans MS', '8', 'bold'), fg='darkred', bg="white", text= cl.usuario_ativo.carrinho_de_compras[i][1]).place(x=200, y=i*30 + 50)
  
    self.titulo.mainloop(1)

  def tela_de_estoque(self):
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
    
    nome_produto = Entry(self.titulo,width=19, bg='white', font=('Comic Sans MS', '12'))
    nome_produto.place(x=152, y=20)
    info_nome = Label(self.titulo,font=('Comic Sans MS', '12', 'bold'), fg='white', bg=self.cor_de_fundo, text='Nome do Produto:')
    info_nome.place(x=4, y=20)

    preco = Entry(self.titulo,width=19, bg='white', font=('Comic Sans MS', '12'))
    preco.place(x=152, y=55)
    info_preco = Label(self.titulo,font=('Comic Sans MS', '12', 'bold'), fg='white', bg=self.cor_de_fundo, text='Preço:')
    info_preco.place(x=45, y=55)

    modificar = Button(self.titulo, width=45, fg=self.cor_de_fundo, text = "MODIFICAR", command = lambda:[cl.usuario_ativo.modifica_qtd_em_estoque(nome_produto.get(), preco.get())]) 
    modificar.place(x=15,y=95)

    exibir = Button(self.titulo, width=45, fg=self.cor_de_fundo, text = "EXIBIR", command = lambda:[cl.usuario_ativo.exibe_dataset()]) 
    exibir.place(x=15,y=130)

    volta_menu = Button(self.titulo, width=45, fg=self.cor_de_fundo, text = "MENU", command = lambda:[self.titulo.destroy(), menu.tela_menu()]) 
    volta_menu.place(x=15,y=165)

    self.titulo.mainloop(1)


login_usuario = Tela("login", 350, 180, "darkred")
cadastro_produto = Tela("cadastro", 350, 250, "darkred")
cadastro_usuario = Tela("cadastro_usuario", 350, 300, "darkred")
menu = Tela("menu", 650, 600, "darkred")
exibe_carrinho = Tela("exibe_usuario", 300, 400, "darkred")
modifica_estoque = Tela("modifica_estoque", 350, 200, "darkred")


login_usuario.tela_de_login()
