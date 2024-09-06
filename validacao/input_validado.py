import tkinter as tk
from tkinter import messagebox

def validar_entrada(valor):
    """Funcao para validar se o valor inserido e um numero"""
    try:
        float(valor)
        return True
    except ValueError:
        return False

def comp_numeros():
    num1 = entry_num1.get()
    num2 = entry_num2.get()

    if not validar_entrada(num1) or not validar_entrada(num2):
        messagebox.showerror("Erro", "Por favor, insira numeros validos.")
        return

    num1 = float(num1)
    num2 = float(num2)

    if num1 > num2:
        messagebox.showinfo("Resultado", f"O numero {num1} e maior que {num2}")
    elif num1 == num2:
        messagebox.showinfo("Resultado", f"O numero {num1} e igual a {num2}")
    else:
        messagebox.showinfo("Resultado", f"O numero {num1} e menor que {num2}")

# Criando a janela
janela = tk.Tk()
janela.title("Comparando Numeros")

# Criando os widgets
label_num1 = tk.Label(janela, text="Numero 1:")
label_num1.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_num1 = tk.Entry(janela)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2 = tk.Label(janela, text="Numero 2:")
label_num2.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_num2 = tk.Entry(janela)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

botao_comp = tk.Button(janela, text="Comparar", command=comp_numeros)
botao_comp.grid(row=2, columnspan=2, padx=10, pady=5)

# Rodando o loop principal
janela.mainloop()
