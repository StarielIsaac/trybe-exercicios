from tkinter import *
from tkinter import messagebox
import json
import random
import os

json_path = os.path.join(os.path.dirname(__file__), "frases.json")


def salvar():
    frase = frase_entry.get()
    autor = autor_entry.get()

    if len(frase) == 0 or len(autor) == 0:
        messagebox.showinfo(title="Oops", message="Não pode ter campos vazios")
    else:
        new_data = {"frase": frase, "autor": autor}

        try:
            with open(json_path, "r") as frases_file:
                data = json.load(frases_file)
        except FileNotFoundError:
            data = []

        data.append(new_data)

        with open(json_path, "w") as frases_file:
            json.dump(data, frases_file, indent=4)

        messagebox.showinfo(title="Sucesso", message="Frase salva com sucesso.")
        frase_entry.delete(0, END)
        autor_entry.delete(0, END)


def get_frase():
    try:
        with open(json_path, "r") as frases_file:
            data = json.load(frases_file)
            if data:
                frase_data = random.choice(data)
                frase = frase_data.get("frase")
                autor = frase_data.get("autor")
                messagebox.showinfo(
                    title="Frase aleatória", message=f'"{frase}" - {autor}'
                )
            else:
                messagebox.showinfo(title="Sem Frases", message="Não temos frases")
    except FileNotFoundError:
        messagebox.showinfo(title="Sem Frases", message="Não temos frases")


window = Tk()
window.title("Frases Inspiradora")
window.config(padx=10, pady=10)

canvas = Canvas(width=600, height=400)
logo_png = PhotoImage(file="logo.png")
window.config(padx=30, pady=30)

canvas.grid(row=5, column=0, columnspan=2, pady=15)
canvas.create_image(360, 200, image=logo_png, anchor="center")

frase_label = Label(text="Frase:", font=("Arial", 12, "bold"))
frase_label.grid(row=0, column=0)
autor_label = Label(text="Autor:", font=("Arial", 12, "bold"))
autor_label.grid(row=1, column=0)

frase_entry = Entry(width=30)
frase_entry.grid(row=0, column=1)
frase_entry.focus()

autor_entry = Entry(width=30)
autor_entry.grid(row=1, column=1)

save_button = Button(text="Salvar uma frase", command=salvar)
save_button.grid(row=2, column=1, ipadx=100)

get_button = Button(text="Retornar uma frase", command=get_frase)
get_button.grid(row=6, column=1, ipadx=100)


window.mainloop()