from tkinter import *
import platform
import pygame


# Tela inicial
janela = Tk()
janela.title("Home")
janela.geometry("720x1400+0+0")

# Segunda tela
login = Toplevel()
login.title("Login")
login.geometry("720x1400+0+0")
login.withdraw()

# Terceira tela
dica = Toplevel()
dica.title("Dica")
dica.geometry("720x1400+0+0")
dica.withdraw()

# Quarta tela
game=Toplevel()
game.title("Game")
game.geometry("720x1400+0+0")
game.withdraw()

# Design da tela inicial
img_home = PhotoImage(file="inicio.png")
lab_home = Label(janela, image=img_home)
lab_home.place(x=0, y=0, relwidth=1, relheight=1)

# Design da segunda tela
login_img = PhotoImage(file="login.png")
lab_login = Label(login, image=login_img)
lab_login.place(x=0, y=0, relwidth=1, relheight=1)

# Design da terceira tela
dica_img = PhotoImage(file="dica.png")
lab_dica = Label(dica, image=dica_img)
lab_dica.place(x=0, y=0, relwidth=1, relheight=1)

# Design da quarta tela
game_img = PhotoImage(file="perguntas.png")
lab_game = Label(game, image=game_img)
lab_game.place(x=0, y=0, relwidth=1, relheight=1)


# Botão de iniciar, tela inicial
def on_click(event):
    janela.withdraw()
    login.deiconify()

iniciar_img = PhotoImage(file="tent.png")
iniciar = Label(janela, image=iniciar_img, borderwidth=0)
iniciar.bind("<Button-1>", on_click)
iniciar.configure(bg="#F9B233")
iniciar.place(x=105, y=907)

#posicionar no pc
if platform.system() == 'Windows' or platform.system() == 'Darwin':
    # Código para posicionar o botão corretamente no PC
    iniciar.place(x=155, y=907)
    # Código para posicionar o botão corretamente no dispositivo móvel

# Entrada de username
bg_color = '#F9B233'
# Criar widget Entry sem borda
username = Text(login, borderwidth=0, relief='solid', width=15, height=1)
username.config(highlightthickness=0)
# Outras configurações do widget Entry
username.config(bg=bg_color, fg='black', font=("Arial", 23))
username.place(x=250, y=663)

# Entrada de senha
senha = Entry(login, borderwidth=0, relief='solid', width=19)
senha.config(highlightthickness=0)
senha.config(bg=bg_color, fg='black', font=("Arial", 23))
senha.place(x=203, y=747)

#botão continuar, segunda tela
def on_click2(event):
      login.withdraw()
      dica.deiconify()

continuar_img = PhotoImage(file="continuar.png")
continuar = Label(login, image=continuar_img, borderwidth=0)
continuar.bind("<Button-1>", on_click2)
continuar.configure(bg="#F9B233")
continuar.place(x=250, y=830)


#botão ok, terceira tela
def on_click3(event):
	dica.withdraw()
	game.deiconify()

ok_img = PhotoImage(file="continuar.png")
ok = Label(dica, image=ok_img, borderwidth=0)
ok.bind("<Button-1>", on_click3)
ok.configure(bg="#F9B233")
ok.place(x=250, y=830)

janela.mainloop()
