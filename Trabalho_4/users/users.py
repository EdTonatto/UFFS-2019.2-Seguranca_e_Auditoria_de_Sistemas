import csv
import globals
import utils
import os
import time
import draw

def verifyUserFileExistance():
    try:
        with open(globals.path_user_csv, 'r') as file:
            return True
    except:
        return False

def verifyUserExistance(nickname):
    with open(globals.path_user_csv, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if(row[globals.field_nickname] == nickname):
                return True, row[globals.field_password], row[globals.field_nickname], row[globals.field_name], row[globals.field_email]
        return False, "", "", "", ""

def writeHeader():
    with open(globals.path_user_csv, 'w', newline='') as csvfile:
        fields = [globals.field_nickname, globals.field_name, globals.field_email, globals.field_password]
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        csvfile.close()

def registerUser(nickname, name, email, senha):
    if not verifyUserFileExistance():
        writeHeader()
    with open(globals.path_user_csv, 'a', newline='') as csvfile:
        fields = [globals.field_nickname, globals.field_name, globals.field_email, globals.field_password]
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        flag = verifyUserExistance(nickname)
        if(not flag[0]):
            writer.writerow({globals.field_nickname: nickname, globals.field_name: name, globals.field_email: email, globals.field_password: senha})
        csvfile.close()

def showUsers():
    try:
        draw.showHeaderShowUser()
        with open(globals.path_user_csv, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            i = 1
            for row in reader:
                print("{i:4d}° Usuário - NickName: {nickname}; Nome: {name}; Email: {email};".format(i=i,
                                                                                                    nickname=row[globals.field_nickname],
                                                                                                    name=row[globals.field_name],
                                                                                                    email=row[globals.field_email]))
                i = i + 1
    except:
        print("Nao foi possivel visualizar o arquivo {path}.".format(path=globals.path_user_csv))

def deleteUsersFile():
    try:
        os.remove(globals.path_user_csv)
        print("Arquivo {path} excluido com sucesso".format(path=globals.path_user_csv))
    except:
        print("Nao foi possivel excluir o arquivo {path}.\nArquivo Inexistente. Cadastre usuarios primeiro".format(path=globals.path_user_csv))

def valideLogin(nickname, password):
    def invalidLogin():
        print("Informacoes incorretas. Tente novamente")
        time.sleep(3)
    def validLogin(nickname, name, email):
        print("Informacoes corretas. Aguarde para ser direcionado ao menu principal")
        globals.current_user_nickname = nickname
        globals.current_user_name = name
        globals.current_user_email = email
        globals.my_public_key = globals.current_user_nickname + "_public.key"
        globals.my_private_key = globals.current_user_nickname + "_private.key"
        time.sleep(3)
    login = verifyUserExistance(nickname)
    if (login[0] == True):
        if(password == login[1]):
            validLogin(login[2], login[3], login[4])
            return True
        else:
            invalidLogin()
            return False
    invalidLogin()
    return False
