from tkinter import *
import awesometkinter as atk
import requests
import json

class BackEnd():
    def cotacoes_variaveis(self):
        self.cotacoes_site = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
        self.cotacoes = self.cotacoes_site.json()

        self.cotacao_dolar = self.cotacoes['USDBRL']['ask']
        self.dolar_inteiro = float(self.cotacao_dolar)

        self.cotacao_euro = self.cotacoes['EURBRL']['ask']
        self.euro_inteiro = float(self.cotacao_euro)

        self.cotacao_bitcoin = self.cotacoes['BTCBRL']['ask']
        self.bitcoin_inteiro = float(self.cotacao_bitcoin)

    def definindo_escolha(self):
        self.cotacoes_variaveis()
        self.selecionado = self.escolha.get()
        self.digitado = float(self.inserir.get().replace("-", ""))

        if self.selecionado == 0:
            self.resultado_dolar = self.dolar_inteiro * self.digitado
            self.dolar_label = Label(self.janela,
                text=self.resultado_dolar,
                font=('times', 20),
                fg='#B22222',
                bg='#ffffff')
            self.dolar_simbolo = Label(self.janela,
                    image=self.simbolo_dolar,
                    bg='#ffffff')

            self.dolar_label.place(x=240, y=205)
            self.dolar_simbolo.place(x=300, y=110)

        elif self.selecionado == 1:
            self.resultado_euro = self.euro_inteiro * self.digitado
            self.euro_label = Label(self.janela,
                    text=self.resultado_euro,
                    font=('times', 20),
                    fg='#B22222',
                    bg='#ffffff')
            self.euro_simbolo = Label(self.janela,
                    image=self.simbolo_euro,
                    bg='#ffffff')

            self.euro_label.place(x=240, y=205)
            self.euro_simbolo.place(x=300, y=110)

        elif self.selecionado == 2:
            self.resultado_bitcoin = self.bitcoin_inteiro * self.digitado
            self.bitcoin_label = Label(self.janela,
                    text=self.resultado_bitcoin,
                    font=('times', 20),
                    fg='#B22222',
                    bg='#ffffff')
            self.bitcoin_simbolo = Label(self.janela,
                    image=self.simbolo_bitcoin,
                    bg='#ffffff')

            self.bitcoin_label.place(x=240, y=205)
            self.bitcoin_simbolo.place(x=300, y=110)

        else:
            print('escolha uma opção')

class FrontEnd(BackEnd):
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
        self.janela.config(bg='#ffffff')
        self.janela.resizable(0, 0)

    def imagens(self):
        self.bitcoin = PhotoImage(file='codificando/imagens/bitcoin.png')
        self.dolar = PhotoImage(file='codificando/imagens/dolar.png')
        self.euro = PhotoImage(file='codificando/imagens/euro.png')
        self.simbolo_bitcoin = PhotoImage(file='codificando/imagens/simbolo_bitcoin.png')
        self.simbolo_dolar = PhotoImage(file='codificando/imagens/simbolo_dolar.png')
        self.simbolo_euro = PhotoImage(file='codificando/imagens/simbolo_euro.png')

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

        self.montante = Label(self.janela,
                text='Montante:',
                font=('verdana', 12),
                fg='blue',
                bg='#ffffff')

        self.resultado = Label(self.janela,
                text='R$',
                font=('times', 20),
                fg='#B22222',
                bg='#ffffff')
                
#        self.simbolo = Label(self.janela,
#                image=)

        self.titulo.place(x=20, y=10)
        self.titulo_bitcoin.place(x=550, y=11)
        self.titlulo_euro.place(x=510, y=11)
        self.titulo_dolar.place(x=469, y=11)
        self.montante.place(x=280, y=70)
        self.resultado.place(x=200, y=205)

    def caixas_de_texto(self):
        self.inserir = Entry(self.janela,
                font=('Times', 15),
                borderwidth=1,
                relief='raised')

        self.inserir.place(x=340, y=110, width=150, height=25)

    def botoes(self):
        self.conversor = Button(self.janela,
                command=self.definindo_escolha,
                text='Converter',
                font=('verdana', 13, 'bold'),
                borderwidth=0,
                fg='#ffffff',
                bg='#5271FF')

        self.conversor.place(x=300, y=150)

    def selecionar(self):

        self.escolha = IntVar()

        self.dolar_radio = atk.Radiobutton(self.janela,
                variable=self.escolha,
                text='Dolar',
                font=('verdana', 12),
                value=0,
                bg='#ffffff')
        self.euro_radio = atk.Radiobutton(self.janela,
                variable=self.escolha,
                text='Euro',
                font=('verdana', 12),
                value=1,
                bg='#ffffff')
        self.bitcoin_radio = atk.Radiobutton(self.janela,
                variable=self.escolha,
                text='Bitcoin',
                font=('verdana', 12),
                value=2,
                bg='#ffffff')

        self.dolar_radio.place(x=50, y=80)
        self.euro_radio.place(x=50, y=120)
        self.bitcoin_radio.place(x=50, y=160)

FrontEnd()