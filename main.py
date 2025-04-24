from customtkinter import (
    CTkSlider,
    CTk as Window,
    CTkLabel as Label,
    IntVar,
    StringVar,
    CTkButton as Button,
)
from math import floor
from PIL import Image, ImageTk
from random import randint
import pyperclip

win = Window(fg_color="#150025")
win.title("Gerador De Senhas Fortes")
win.iconbitmap("./imagens/icon-cadeado-fechado.ico")
width = 350
height = 500
pad_left = (win.winfo_screenwidth() - width) // 2
pad_top = (win.winfo_screenheight() - height) // 2
win.geometry(f"{width}x{height}+{pad_left}+{pad_top}")
win.resizable(False, False)

# IMAGEM
image = ImageTk.PhotoImage(Image.open("./imagens/cadeado-chave.png").resize((170, 170)))

# LABEL - IMAGEM
Label(win, image=image, text=None).pack(pady=(20, 50))

# LABEL - TAMANHO
length = StringVar(value="8")
Label(win, textvariable=length, font=("consolas", 30, "bold")).pack(pady=(20, 10))

# RANGE
value = IntVar(value=8)


# ACTUALIZA O VALOR DO TAMANHO
def Get_Value(vl):
    length.set(str(floor(vl)))


n_char = CTkSlider(
    win,
    from_=8,
    to=100,
    variable=value,
    width=300,
    button_hover_color="#9e6700",
    button_color="#ffa600",
    progress_color="#ff6600",
    command=Get_Value,
)
n_char.pack(pady=(10, 20))


# BOTÃO GERAR
def Password_Generator():
    chars = "abcdefghijklmnopqrstuvwxyw1234567890ABCDEFGHIJKLMNOPQRSTUVWXYW/*-+@{[]}!\"#$%&/()=?'_.:;"

    password = ""

    for i in range(0, value.get()):
        random_index = randint(0, (len(chars) - 1))
        password += chars[random_index]

    pyperclip.copy(password)

    return result.set(password)


button = Button(
    win,
    text="Criar senha forte",
    width=300,
    height=40,
    corner_radius=1,
    fg_color="#ffa600",
    hover_color="#9e6700",
    command=Password_Generator,
)
button.pack()

# LABEL - RESULTADO
result = StringVar(value="")
Label(win, wraplength=300, font=("consolas", 15), textvariable=result).pack(
    pady=(10, 0)
)

win.mainloop()
