#from keys import keys
from users import users
import utils
import globals

def login():
    utils.clearScreen()
    logininfo = {}
    logininfo = utils.showLoginUsrPsswdMenu()
    if (users.valideLogin(logininfo[globals.field_nickname], logininfo[globals.field_password]) == False):
        login()
    else:
        return

def callRegisterUser():
    newuser = {}
    newuser = utils.showRegisterUser()
    users.registerUser(
        newuser[globals.field_nickname],
        newuser[globals.field_name],
        newuser[globals.field_email],
        newuser[globals.field_password])
    print("Usuario {name} cadastrado com sucesso com o nickname {nickname}".format(name=newuser[globals.field_name], nickname=newuser[globals.field_nickname]))
    utils.pauseScreen()

def main():
    utils.clearScreen()
    op = utils.showLoginMenu()
    if (op == 1):
        login() #REALIZA LOGIN
        while True:
            op = utils.showMainMenu()
            if (op == 1): #USUARIOS
                op = utils.showUserMenu()
                if (op == 1): #CADASTRO DE USUARIOS
                    callRegisterUser()
                if (op == 2): #LISTAR USUARIOS
                    users.showUsers()
                    utils.pauseScreen()
                if (op == 3): #DELETAR ARQUIVO DE USUARIOS
                    users.deleteUsersFile()
                    utils.pauseScreen()
    if (op == 2): #CADASTRAR USUARIO NO MOMENTO DE LOGIN LOGAR
        callRegisterUser()
        main()
    if (op == 3): #SAIR NA TELA DE LOGIN
        print("Programa finalizado!!!")

main()

#users.valideLogin("EdTonatto", "senha123")
