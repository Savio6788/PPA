
from tkinter import *

ARQUIVO = "texto.txt"
SESSAO = "sessao.txt"

def validar_login():
    user = entry_username.get()
    senha = entry_senha.get()
    with open(ARQUIVO, "r") as arquivo:
        # criar um dicionário de credenciais a partir do arquivo
        credenciais = {}
        for linha in arquivo:
            linha = linha.strip("\n")
            username, password = linha.rsplit(maxsplit=1)
            credenciais[username] = password
        # verificar se a entrada do usuário corresponde a alguma credencial
        if user in credenciais and senha == credenciais[user]:
            label_status["text"] = "Login realizado com sucesso!"
            # salvar o nome de usuário na sessão
            with open(SESSAO, "w") as sessao:
                sessao.write(user)
            # fechar a janela de login e abrir a janela principal
            login.destroy()
            abrir_janela_principal()
        else:
            label_status["text"] = "Usuário ou senha incorretos!"

def cadastrar_usuario():
    user = entry_username.get()
    senha = entry_senha.get()
    with open(ARQUIVO, "r+") as arquivo:
        # verificar se o nome de usuário já existe no arquivo
        for linha in arquivo:
            linha = linha.strip("\n")
            username, _ = linha.rsplit(maxsplit=1)
            if user == username:
                label_status["text"] = "Nome de usuário indisponível. Por favor, tente outro."
                return
        # adicionar o novo usuário e senha no final do arquivo
        arquivo.write(user + " " + senha + "\n")
    label_status["text"] = "Usuário cadastrado com sucesso!"

def abrir_janela_login():
    global login, entry_username, entry_senha, label_status
    login = Tk()
    login.title("Login no tkinter")
    login.geometry("720x1400")
    login_img= PhotoImage(file="login.png")
    login_design=Label(login,image=login_img)
    login_design.pack()

    entry_username = Entry(login, font=("Arial",23), width=15, bg="#F4E038",highlightthickness=0,fg="#7E57B1")
    entry_senha = Entry(login, show="*",font=("Arial",23), width=18, bg="#F4E038",highlightthickness=0, fg="#7E57B1")

    botao_login = Button(login, text="Login", command=validar_login)
    botao_cadastro = Button(login, text="Cadastrar", command=cadastrar_usuario)

    label_status = Label(login, text="")

    entry_username.place(x=288, y=530)
    entry_senha.place(x=230, y=628)
    botao_login.place(x=250,y=730)
    botao_cadastro.place(x=10,y=100)
    label_status.place(x=100, y=200)

    login.mainloop()

def abrir_janela_principal():
    global perfil
    perfil = Tk()
    perfil.title("Janela principal")
    perfil.geometry("720x1400")
    perfil_img= PhotoImage(file="perfil.png")
    perfil_design= Label(perfil, image=perfil_img)
    perfil_design.pack()

    # ler o nome de usuário da sessão
    with open(SESSAO) as sessao:
        user = sessao.read()

    # mostrar uma mensagem de boas-vindas
    label_bem_vindo = Label(perfil, text=f"{user}", font =("Arial", 23), fg="#7E57B1",bg="#F4E038")
    label_bem_vindo.place(x=305, y=193)

    # mostrar um botão para sair da sessão
    botao_sair = Button(perfil, text="Sair", command=sair_sessao)
    botao_sair.place(x=50, y=100)

    perfil.mainloop()

def sair_sessao():
    global login
    # apagar o nome de usuário da sessão
    with open(SESSAO, "w") as sessao:
        sessao.write("")
    
    # fechar a janela principal e abrir a janela de login
    perfil.destroy()
    abrir_janela_login()

# verificar se há algum usuário logado na sessão
with open(SESSAO) as sessao:
    user = sessao.read()

if user:
    # abrir a janela principal diretamente
    abrir_janela_principal()
else:
   # abrir a janela de login normalmente 
   abrir_janela_login()