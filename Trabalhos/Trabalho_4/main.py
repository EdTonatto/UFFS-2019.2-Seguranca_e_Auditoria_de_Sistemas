from keys import keys
from users import users
from files import files
import draw
import utils
import globals

def login():
    utils.clearScreen()
    logininfo = {}
    logininfo = draw.showLoginUsrPsswdMenu()
    if (users.validateLogin(logininfo[globals.field_nickname], logininfo[globals.field_password]) == False):
        login()
    else:
        files.createFilesPath()
        return

def callRegisterUser():
    newuser = {}
    newuser = draw.showRegisterUser()
    users.registerUser(
        newuser[globals.field_nickname],
        newuser[globals.field_name],
        newuser[globals.field_email],
        newuser[globals.field_password])
    print("Usuario {name} cadastrado com sucesso com o nickname {nickname}".format(name=newuser[globals.field_name], nickname=newuser[globals.field_nickname]))
    files.createFilesPath()
    utils.pauseScreen()

def main():
    utils.clearScreen()
    op = draw.showLoginMenu()
    if (op == 1):
        login() #REALIZA LOGIN
        while True:
            op = draw.showMainMenu()
            if (op == 1): #USUARIOS
                op = draw.showUserMenu()
                if (op == 1): #CADASTRO DE USUARIOS
                    callRegisterUser()
                    continue
                if (op == 2): #LISTAR USUARIOS
                    users.showUsers()
                    utils.pauseScreen()
                    continue
                if (op == 3): #DELETAR ARQUIVO DE USUARIOS
                    users.deleteUsersFile()
                    utils.pauseScreen()
                    continue
            if (op == 2): #CHAVES
                op = draw.showKeyMenu()
                if (op == 1): #GERAR CHAVES
                    if (keys.generateKeys() == True):
                        print("Chaves geradas com sucesso!")
                    else:
                        print("Chaves ja existentes!")
                    utils.pauseScreen()
                    continue
                if (op == 2): #SETAR BITSIZE RSA
                    keys.setBitsizeRSA()
                    utils.pauseScreen()
                    continue
                if (op == 3): #LISTAR CHAVES RSA DO USUARIO
                    keys.showKeys()
                    utils.pauseScreen()
                    continue
                if (op == 4): #DELETAR ARQUIVOS DAS CHAVES DO USUARIO
                    keys.deleteKeysFile()
                    utils.pauseScreen()
                    continue
                if (op == 5):
                    draw.showSelectUser()
                    keys.showOtherPublicKey()
                    utils.pauseScreen()
                    continue
            if (op == 3): #ARQUIVOS
                op = draw.showFileMenu()
                if (op == 1):
                    newfile = {}
                    newfile = draw.showSendFileMenu()
                    utils.updateSettingsToSendFile(newfile[globals.field_file_name],
                                                    newfile[globals.field_file_receiver])
                    files.createSendFile(newfile[globals.field_file_content])
                    utils.pauseScreen()
                    continue
            if (op == 0):
                break
    if (op == 2): #CADASTRAR USUARIO NO MOMENTO DE LOGIN LOGAR
        callRegisterUser()
        main()
    if (op == 3): #SAIR NA TELA DE LOGIN
        print("Programa finalizado!!!")

main()
