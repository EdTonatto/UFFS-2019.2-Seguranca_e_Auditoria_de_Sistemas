import os
import globals

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pauseScreen():
    input("\nPressione <enter> para continuar")

def showHeaderShowUser():
    print("------------------------------ LISTANDO USUARIOS -----------------------------")

def showLogin():
    op = -1
    print("------------------------------------ LOGIN -----------------------------------")
    print("    Opções:")
    print("        1 - Logar")
    print("        2 - Cadastrar")
    print("        3 - Sair")
    op = input("Opção selecionada: ")
    return int(op)

def showMainMenu():
    op = -1
    clearScreen()
    print("------------------------------------ MENU ------------------------------------")
    print("    Opções:")
    print("        1 - Usuários")
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
