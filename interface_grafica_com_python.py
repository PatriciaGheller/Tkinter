import tkinter as tk
from tkinter import ttk

# Criando a janela principal
janela = tk.Tk()
janela.title("Minha Interface Gráfica com Tkinter")

# Criando um frame dentro da janela principal
frm = ttk.Frame(janela, padding=10)
frm.grid()

# Adicionando widgets dentro do frame usando grid
ttk.Label(frm, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
ttk.Entry(frm).grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frm, text="Senha:").grid(row=1, column=0, padx=5, pady=5)
ttk.Entry(frm, show="*").grid(row=1, column=1, padx=5, pady=5)

ttk.Button(frm, text="Login", command=janela.destroy).grid(row=2, column=0, columnspan=2, pady=10)

# Iniciando o loop da aplicação
janela.mainloop()
