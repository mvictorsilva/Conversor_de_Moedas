from tkinter import *
import requests
import json

cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

cotacoes = cotacoes.json()

class Application():
    def __init__(self):
        self.janela = Tk()
        self.especificacoes_janela()
        self.labels()
        self.janela.mainloop()

    def especificacoes_janela(self):
        self.janela.title('Cotações de todas as moedas')
        self.janela.iconbitmap('codificando/imagens/icon_cotacoes.ico')
        self.janela.geometry('700x500')
        self.janela.config(bg='#f8f8f7')
        self.janela.resizable(0, 0)

    def labels(self):
        self.titulo = Label(self.janela,
                text='Conversor de moedas',
                font=('Anonymous Pro', 25),
                fg='#ab8c67',
                bg='#f8f8f7')

        self.titulo.place(x=20, y=10)

    

Application()
