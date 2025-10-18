import tkinter as tk
from tkinter import ttk

# Janela principal
janela = tk.Tk()
janela.title("Tabela com Check")
janela.geometry("400x250")

# Título
titulo = tk.Label(janela, text="Lista de Tarefas", font=("Arial", 14, "bold"))
titulo.pack(pady=10)

# Frame para a tabela
frame = tk.Frame(janela)
frame.pack()

# Cabeçalhos
tk.Label(frame, text="Feito", font=("Arial", 10, "bold"), width=10).grid(row=0, column=0)
tk.Label(frame, text="Tarefa", font=("Arial", 10, "bold"), width=20).grid(row=0, column=1)

# Lista de tarefas
tarefas = ["Estudar Python", "Ler um livro", "Fazer exercício", "Revisar anotações"]

# Lista para armazenar variáveis dos checks
checks = []

# Cria as linhas da tabela
for i, tarefa in enumerate(tarefas, start=1):
    var = tk.BooleanVar()
    check = tk.Checkbutton(frame, variable=var)
    check.grid(row=i, column=0, pady=3)
    tk.Label(frame, text=tarefa).grid(row=i, column=1, sticky="w")
    checks.append(var)

# Função para mostrar o que foi marcado
def mostrar_selecionados():
    selecionados = [tarefas[i] for i, v in enumerate(checks) if v.get()]
    print("Selecionados:", selecionados)

# Botão para exibir no terminal o que foi marcado
botao = tk.Button(janela, text="Ver Selecionados", command=mostrar_selecionados)
botao.pack(pady=10)

janela.mainloop()