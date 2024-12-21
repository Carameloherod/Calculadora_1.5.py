from tkinter import *
from tkinter import messagebox

programa = Tk()
programa.geometry("400x400")
programa.title("Calculadora")
programa.config(bd=20)
programa.resizable(False, False)
primeiro = Entry(programa, width=40)
primeiro.pack()
segundo = Entry(programa,  width=40)
segundo.pack()
terceiro = Entry(programa, width=15)
terceiro.pack()
#Função de Calcular
def calcular():
    primeiro_1 = primeiro.get()
    segundo_2 = segundo.get()
    terceiro1 = terceiro.get()
    if primeiro_1.isdigit() and segundo_2.isdigit() and terceiro1 == "*":
      inteiro = int(primeiro_1) * int(segundo_2)
      messagebox.showinfo("Resultado", f"O resultado é: {inteiro}") #O primeiro texto sempre é o titulo e o com f"" é o texto na messagebox!
    if primeiro_1.isdigit() and segundo_2.isdigit() and terceiro1 == "+":
      inteiro = int(primeiro_1) + int(segundo_2)
      messagebox.showinfo("Resultado", f"O resultado é: {inteiro}") #O primeiro texto sempre é o titulo e o com f"" é o texto na messagebox!
    if primeiro_1.isdigit() and segundo_2.isdigit() and terceiro1 == "-":
      inteiro = int(primeiro_1) - int(segundo_2)
      messagebox.showinfo("Resultado", f"O resultado é: {inteiro}") #O primeiro texto sempre é o titulo e o com f"" é o texto na messagebox!
    if primeiro_1.isdigit() and segundo_2.isdigit() and terceiro1 == "/":
      inteiro = int(primeiro_1) / int(segundo_2)
      messagebox.showinfo("Resultado", f"O resultado é: {inteiro}") #O primeiro texto sempre é o titulo e o com f"" é o texto na messagebox!
calcular()
button = Button(programa, text="Calcular", command=calcular)
button.pack()
programa.mainloop()