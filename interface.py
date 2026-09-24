import tkinter as tk
from tkinter import ttk

from sorteador import sorteador


class InterfaceSorteador:
    def __init__(self, janela):
        self.janela = janela
        self.minimo = tk.StringVar()
        self.maximo = tk.StringVar()
        self.resultado = tk.StringVar(value='—')
        self.mensagem = tk.StringVar(value='Escolha os limites e clique em Sortear.')

        self.configurar_janela()
        self.configurar_estilos()
        self.criar_componentes()
        self.janela.bind('<Return>', self.sortear)

    def configurar_janela(self):
        self.janela.title('Sorteador Kepler')
        self.janela.geometry('600x480')
        self.janela.resizable(False, False)
        self.janela.configure(background='#eef2f6')
        self.janela.update_idletasks()

        x = max(0, (self.janela.winfo_screenwidth() - self.janela.winfo_width()) // 2)
        y = max(0, (self.janela.winfo_screenheight() - self.janela.winfo_height()) // 2)
        self.janela.geometry(f'+{x}+{y}')

    def configurar_estilos(self):
        estilo = ttk.Style(self.janela)
        estilo.theme_use('clam')
        estilo.configure('Cartao.TFrame', background='white')
        estilo.configure('Texto.TLabel', background='white', foreground='#334155', font=('', 11))
        estilo.configure('Titulo.TLabel', background='white', foreground='#0f172a', font=('', 24, 'bold'))
        estilo.configure('Resultado.TLabel', background='white', foreground='#2563eb', font=('', 42, 'bold'))
        estilo.configure('Campo.TEntry', padding=8, fieldbackground='#f8fafc')
        estilo.configure('Placeholder.TLabel', background='#f8fafc', foreground='#64748b', font=('', 11))
        estilo.configure('Sortear.TButton', padding=12, background='#2563eb', foreground='white', font=('', 12, 'bold'))
        estilo.map('Sortear.TButton', background=[('active', '#1d4ed8')])

    def criar_componentes(self):
        cartao = ttk.Frame(self.janela, padding=28, style='Cartao.TFrame')
        cartao.place(relx=0.5, rely=0.5, anchor='center', width=500)
        cartao.columnconfigure((0, 1), weight=1, uniform='campos')

        ttk.Label(cartao, text='Sorteador Kepler', style='Titulo.TLabel').grid(
            row=0, column=0, columnspan=2, pady=(0, 24)
        )
        self.criar_campo(cartao, 'Limite mínimo', self.minimo, coluna=0)
        self.criar_campo(cartao, 'Limite máximo', self.maximo, coluna=1)

        ttk.Button(cartao, text='Sortear número', command=self.sortear, style='Sortear.TButton').grid(
            row=3, column=0, columnspan=2, sticky='ew', pady=20
        )
        ttk.Label(cartao, textvariable=self.resultado, style='Resultado.TLabel', wraplength=440).grid(
            row=4, column=0, columnspan=2
        )
        ttk.Label(cartao, textvariable=self.mensagem, style='Texto.TLabel', wraplength=440, justify='center').grid(
            row=5, column=0, columnspan=2, pady=(8, 0)
        )

    def criar_campo(self, painel, texto, variavel, coluna):
        margem = (0, 8) if coluna == 0 else (8, 0)
        ttk.Label(painel, text=texto, style='Texto.TLabel').grid(
            row=1, column=coluna, sticky='w', padx=margem, pady=(0, 6)
        )
        campo = ttk.Entry(painel, textvariable=variavel, style='Campo.TEntry', width=12, font=('', 13))
        campo.grid(row=2, column=coluna, sticky='ew', padx=margem)
        dica = ttk.Label(campo, text='Digite um inteiro', style='Placeholder.TLabel', cursor='xterm')

        def atualizar_dica(*args):
            if variavel.get() or campo.focus_get() == campo:
                dica.place_forget()
            else:
                dica.place(x=10, rely=0.5, anchor='w')

        dica.bind('<Button-1>', lambda event: campo.focus_set())
        campo.bind('<FocusIn>', atualizar_dica)
        campo.bind('<FocusOut>', atualizar_dica)
        variavel.trace_add('write', atualizar_dica)
        atualizar_dica()

    def sortear(self, event=None):
        try:
            minimo = int(self.minimo.get())
            maximo = int(self.maximo.get())
        except ValueError:
            self.mostrar_erro('Digite apenas números inteiros nos dois campos.')
            return

        try:
            numero = sorteador(minimo, maximo)
        except ValueError as erro:
            self.mostrar_erro(str(erro))
            return

        self.resultado.set(str(numero))
        self.mensagem.set('Número sorteado! Clique novamente para repetir.')

    def mostrar_erro(self, mensagem):
        self.resultado.set('—')
        self.mensagem.set(mensagem)


def iniciar_interface():
    janela = tk.Tk()
    InterfaceSorteador(janela)
    janela.mainloop()
