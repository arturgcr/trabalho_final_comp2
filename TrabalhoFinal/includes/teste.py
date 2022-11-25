import PySimpleGUI as sg

layout=[[sg.Text("qual o prolema dessa merda?")]]

janela = sg.Window("titulo", layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WINDOW.CLOSED:
        break

janela.close()