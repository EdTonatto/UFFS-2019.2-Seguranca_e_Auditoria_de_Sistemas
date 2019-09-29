import os
import globals

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pauseScreen():
    input("\nPressione <enter> para continuar")

def showHeaderShowUser():
    print("------------------------------ LISTANDO USUARIOS -----------------------------")

def showKeyMenu():
    op = -1
    clearScreen()
    print("--------------------------------- MENU CHAVES --------------------------------")
    print("    Opções:")
    print("        1 - Gerar chaves publica/privada")
    print("        2 - Setar tamanho de bits da chave RSA")
    print("        3 - Listar minhas chaves")
    print("        4 - Remover minhas chaves")
    op = input("Opção selecionada: ")
    return int(op)

def showLoginMenu():
    op = -1
    print("------------------------------------ LOGIN -----------------------------------")
    print("    Opções:")
    print("        1 - Logar")
    print("        2 - Cadastrar")
    print("        3 - Sair")
    op = input("Opção selecionada: ")
    return int(op)

def showLoginUsrPsswdMenu():
    logininfo = {}
    print("------------------------------- REALIZAR LOGIN -------------------------------")
    print("    Informe:")
    print("        1 - NickName (Login)")
    print("        2 - Senha")
    logininfo[globals.field_nickname] = str(input("1: "))
    logininfo[globals.field_password] = str(input("2: "))
    return logininfo

def showMainMenu():
    op = -1
    clearScreen()
    #print(globals.current_user_nickname)
    #print(globals.current_user_name)
    #print(globals.current_user_email)
    #print(globals.public_key)
    #print(globals.private_key)
    #print(globals.path_public_key + globals.public_key)
    #print(globals.path_private_key + globals.private_key)
    print("------------------------------------ MENU ------------------------------------")
    print("    Opções:")
    print("        1 - Usuários")
    print("        2 - Chaves")
    print("        0 - Sair")
    op = input("Opção selecionada: ")
    return int(op)

def showRegisterUser():
    newuser = {}
    print("------------------------------ CADASTRAR USUARIO -----------------------------")
    print("    Informe:")
    print("        1 - Nick")
    print("        2 - Nome")
    print("        3 - Email")
    print("        4 - Senha")
    newuser[globals.field_nickname] = str(input("1: "))
    newuser[globals.field_name] = str(input("2: "))
    newuser[globals.field_email] = str(input("3: "))
    newuser[globals.field_password] = str(input("4: "))
    return newuser

def showUserMenu():
    op = -1
    clearScreen()
    print("-------------------------------- MENU USUARIOS -------------------------------")
    print("    Opções:")
    print("        1 - Cadastrar usuário")
    print("        2 - Listar usuários")
    print("        3 - Remover arquivo de usuários")
    op = input("Opção selecionada: ")
    return int(op)
