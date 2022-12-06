from tkinter import *
import pandas as pd

janela = Tk()

#função x x.
x = pd.read_csv("TrabalhoFinal/arquivosCsv/dataset_livros.csv", header = None) #o x deve existir e estar na mesma pasta do progrma pra poder executar. 

cs = Scrollbar (janela)
cs.pack(side=RIGHT, fill=Y)
texto = Text(janela, font="Arial 12")
texto.pack(expand=YES, fill=BOTH)
texto.insert(0.0, x) #inserindo a leitura do x dentro do Text. 
#aqui configuramos o scrolbar no elemento Text. 
texto.config (yscrollcommand=cs.set)
cs.config (command=texto.yview)

janela.mainloop()