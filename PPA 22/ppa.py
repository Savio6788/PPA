from tkinter import *
import platform
import pygame

ARQUIVO = "texto.txt"

def validar_login():
    user = entry_username.get()
    senha = entry_senha.get()
    with open(ARQUIVO, "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip("\n")
            username, password = linha.rsplit(maxsplit=1)
            if user == username and senha == password:
                label_status["text"] = "Login realizado com sucesso!"
                login.withdraw()
                perfil.deiconify()
                return
        label_status["text"] = "Usuário ou senha incorretos!"

def cadastrar_usuario():
    user = entry_username.get()
    senha = entry_senha.get()
    with open(ARQUIVO, "r+") as arquivo:
        for linha in arquivo:
            linha = linha.strip("\n")
            username, _ = linha.rsplit(maxsplit=1)
            if user == username:
                label_status["text"] = "Nome de usuário indisponível. Por favor, tente outro."
                return
        arquivo.write(user + " " + senha + "\n")
    label_status["text"] = "Usuário cadastrado com sucesso!"


# Tela inicial
janela = Tk()
janela.title("Home")
janela.overrideredirect(True)
janela.geometry("720x1400+0+0")

# Segunda tela
login = Toplevel()
login.overrideredirect(True)
login.title("Login")
login.geometry("720x1400+0+0")
login.withdraw()

# Terceira tela
perfil = Toplevel()
perfil.title("Perfil")
perfil.overrideredirect(True)
perfil.geometry("720x1400+0+0")
perfil.withdraw()

# Quarta tela
game=Toplevel()
game.overrideredirect(True)
game.title("Game")
game.geometry("720x1400+0+0")
game.withdraw()

# Design da tela inicial
img_home = PhotoImage(file="home.png")
lab_home = Label(janela, image=img_home)
lab_home.place(x=0, y=0, relwidth=1, relheight=1)

# Design da segunda tela
login_img = PhotoImage(file="login.png")
lab_login = Label(login, image=login_img)
lab_login.place(x=0, y=0, relwidth=1, relheight=1)

# Design da terceira tela
dica_img = PhotoImage(file="perfil.png")
lab_dica = Label(perfil, image=dica_img)
lab_dica.place(x=0, y=0, relwidth=1, relheight=1)

# Design da quarta tela
game_img = PhotoImage(file="home.png")
lab_game = Label(game, image=game_img)
lab_game.place(x=0, y=0, relwidth=1, relheight=1)


# Botão de iniciar, tela inicial
def on_click(event):
    janela.withdraw()
    login.deiconify()

iniciar_img = PhotoImage(file="start.png")
iniciar = Label(janela, image=iniciar_img, borderwidth=0)
iniciar.bind("<Button-1>", on_click)
iniciar.configure(bg="#F9B233")
iniciar.place(x=152, y=1081)

# Entrada de username
bg_color ='#F4E038'
# Criar widget Entry sem borda
entry_username = Entry(login, borderwidth=0, relief='solid', width=15)
entry_username.config(highlightthickness=0)
# Outras configurações do widget Entry
entry_username.config(bg=bg_color, fg='#7E57B1', font=("Arial", 23))
entry_username.place(x=288, y=527)

# Entrada de senha
entry_senha = Entry(login, borderwidth=0, relief='solid', width=17)
entry_senha.config(highlightthickness=0)
entry_senha.config(bg=bg_color, fg='#7E57B1', font=("Arial", 23))
entry_senha.place(x=225,y=635)


botao_cadastro = Button(login, text="Cadastrar", command=cadastrar_usuario)
botao_cadastro.pack()

label_status = Label(janela, text="")


#botão continuar, segunda tela
#def on_click2(event):
    #  login.withdraw()
    #  perfil.deiconify()

continuar_img = PhotoImage(file="next.png")
continuar = Button(login, image=continuar_img, borderwidth=0, command=validar_login)
#continuar.bind("<Button-1>", on_click2)
continuar.configure(bg="#F9B233")
continuar.place(x=195, y=740)


#botão ok, terceira tela
def on_click3(event):
	perfil.withdraw()
	game.deiconify()

ok_img = PhotoImage(file="next.png")
ok = Label(perfil, image=ok_img, borderwidth=0)
ok.bind("<Button-1>", on_click3)
ok.configure(bg="#F9B233")
ok.place(x=315, y=1270)

#posicionar no pc
if platform.system() == 'Windows' or platform.system() == 'Darwin':
    # Código para posicionar o botão corretamente no PC
    janela.geometry("1900x1600")
    janela.overrideredirect(False)
    iniciar.place(x=695, y=738)
    login.geometry("1900x1600")
    login.overrideredirect(False)
    entry_username.place(x=850, y=501)
    continuar.place(x=855, y=658)
    perfil.geometry("1900x1600")
    perfil.overrideredirect(False)
    game.geometry("1900x1600")
    game.overrideredirect(False)


janela.mainloop()
