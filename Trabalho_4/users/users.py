import csv
import globals

def verifyUserFileExistance():
    try:
        with open('users/registered/users.csv', 'r') as file:
            return True
    except:
        return False

def verifyUserExistance(nickname):
    with open('users/registered/users.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if(row[globals.field_nickname] == nickname):
                return True
        return False

def writeHeader():
    with open('users/registered/users.csv', 'w', newline='') as csvfile:
        fields = [globals.field_nickname, globals.field_name, globals.field_email, globals.field_password]
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        csvfile.close()

def registerUser(nickname, name, email, senha):
    if not verifyUserFileExistance():
        writeHeader()
    with open('users/registered/users.csv', 'a', newline='') as csvfile:
        fields = [globals.field_nickname, globals.field_name, globals.field_email, globals.field_password]
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        if(not verifyUserExistance(nickname)):
            writer.writerow({globals.field_nickname: nickname, globals.field_name: name, globals.field_email: email, globals.field_password: senha})
        csvfile.close()

def showUsers():
    with open('users/registered/users.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row[globals.field_nickname], row[globals.field_name], row[globals.field_email], row[globals.field_password])
