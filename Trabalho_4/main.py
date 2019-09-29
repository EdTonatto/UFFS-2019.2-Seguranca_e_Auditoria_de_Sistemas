#from keys import keys
from users import users
import utils
import globals

def main():
    utils.clearScreen()
    op = utils.showLogin()
    if (op == 1):
        #ValidarUsuario
        while True:
            op = utils.showMainMenu()
            if (op == 1): #USUARIOS
                op = utils.showUserMenu()
                if (op == 1): #CADASTRO DE USUARIOS
                    newuser = {}
                    newuser = utils.showRegisterUser()
                    users.registerUser(
                        newuser[globals.field_nickname],
                        newuser[globals.field_name],
                        newuser[globals.field_email],
                        newuser[globals.field_password])
                    print("Usuario {name} cadastrado com sucesso com o nickname {nickname}".format(name=newuser[globals.field_name], nickname=newuser[globals.field_nickname]))
                    utils.pauseScreen()
                if (op == 2): #LISTAR USUARIOS
                    users.showUsers()
                    utils.pauseScreen()
                if (op == 3): #DELETAR ARQUIVO DE USUARIOS
                    users.deleteUsersFile()
                    utils.pauseScreen()
    if (op == 2):
        newuser = {}
        newuser = utils.showRegisterUser()
        users.registerUser(
            newuser[globals.field_nickname],
            newuser[globals.field_name],
            newuser[globals.field_email],
            newuser[globals.field_password])
        print("Usuario {name} cadastrado com sucesso com o nickname {nickname}".format(name=newuser[globals.field_name], nickname=newuser[globals.field_nickname]))
        utils.pauseScreen()
        main()
    if (op == 3):
        print("Programa finalizado!!!")

main()
