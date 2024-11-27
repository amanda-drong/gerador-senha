import random
import string
from tkinter import *

def gerar_senha():
    tamanho = int(entrada_tamanho.get())
    incluir_numeros = variavel_numeros.get()
    incluir_simbolos = variavel_simbolos.get()

    caracteres = string.ascii_letters
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    label_senha['text'] = senha

# Criar a janela principal
janela = Tk()
janela.title("Gerador de Senhas")

# Rótulos e campos de entrada
label_tamanho = Label(janela, text="Tamanho da senha:")
label_tamanho.pack()
entrada_tamanho = Entry(janela)
entrada_tamanho.pack()

# Variáveis para checkboxes
variavel_numeros = BooleanVar()
variavel_simbolos = BooleanVar()

# Checkboxes
check_numeros = Checkbutton(janela, text="Incluir números", variable=variavel_numeros)
check_numeros.pack()
check_simbolos = Checkbutton(janela, text="Incluir símbolos", variable=variavel_simbolos)
check_simbolos.pack()

# Botão para gerar a senha
botao_gerar = Button(janela, text="Gerar Senha", command=gerar_senha)
botao_gerar.pack()

# Rótulo para exibir a senha gerada
label_senha = Label(janela, text="")
label_senha.pack()

janela.mainloop()