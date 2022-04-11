from cgitb import text
from tkinter import *
from tkinter import font
import requests
import json

cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

cotacoes = cotacoes.json()

class Application():
    def __init__(self):
        self.janela = Tk()
        self.especificacoes_janela()
        self.imagens()
        self.labels()
        self.caixas_de_texto()
        self.botoes()
        self.selecionar()
        self.janela.mainloop()

    def especificacoes_janela(self):
        self.janela.title('Cotações de todas as moedas')
        self.janela.iconbitmap('codificando/imagens/icon_cotacoes.ico')
        self.janela.geometry('600x260')
        self.janela.config(bg='beige')
        self.janela.resizable(0, 0)

    def imagens(self):
        self.bitcoin = PhotoImage(file='codificando/imagens/bitcoin.png')
        self.dolar = PhotoImage(file='codificando/imagens/dolar.png')
        self.euro = PhotoImage(file='codificando/imagens/euro.png')

    def labels(self):
        self.titulo = Label(self.janela,
                text='Conversor de moedas',
                font=('Anonymous Pro', 23),
                fg='#F3B03C',
                bg='#ffffff')

        self.titulo_bitcoin = Label(self.janela,
                image=self.bitcoin,
                bg='#ffffff')

        self.titlulo_euro = Label(self.janela,
                image=self.euro,
                bg='#ffffff')

        self.titulo_dolar = Label(self.janela,
                image=self.dolar,
                bg='#ffffff')

        self.resultado = Label(self.janela,
                text='R$',
                font=('times', 20),
                fg='#B22222',
                bg='#FAF0E6')

        self.titulo.place(x=20, y=10)
        self.titulo_bitcoin.place(x=550, y=11)
        self.titlulo_euro.place(x=510, y=11)
        self.titulo_dolar.place(x=469, y=11)
        self.resultado.place(x=200, y=205)

    def caixas_de_texto(self):
        self.inserir = Entry(self.janela,
                font=('Times', 15),
                borderwidth=1,
                relief='raised')

        self.inserir.place(x=340, y=100, width=150, height=25)

    def botoes(self):
        self.conversor = Button(self.janela,
                text='Converter',
                font=('verdana', 13, 'bold'),
                borderwidth=0,
                fg='#ffffff',
                bg='#5271FF')

        self.conversor.place(x=300, y=150)

    def selecionar(self):
        self.dolar_radio = Radiobutton(self.janela,
                text='Dolar',
                font=('verdana', 12),
                value='d',
                bg='#ffffff')
        self.euro_radio = Radiobutton(self.janela,
                text='Euro',
                font=('verdana', 12),
                value='e',
                bg='#ffffff')
        self.bitcoin_radio = Radiobutton(self.janela,
                text='Euro',
                font=('verdana', 12),
                value='b',
                bg='#ffffff')

        self.dolar_radio.place(x=50, y=80)
        self.euro_radio.place(x=50, y=120)
        self.bitcoin_radio.place(x=50, y=160)

Application()
