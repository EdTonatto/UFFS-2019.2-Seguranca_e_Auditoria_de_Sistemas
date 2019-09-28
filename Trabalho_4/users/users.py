import csv

field_name = "USR_name"
field_nickname = "USR_nickname"
field_email = "USR_email"
field_password = "USR_password"

def verifyUserFileExistance():
    try:
        with open('users/registered/users.csv', 'r') as file:
            return True
    except:
        return False

def writeHeader():
    with open('users/registered/users.csv', 'w', newline='') as csvfile:
        fields = [field_nickname, field_name, field_email, field_password]
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        csvfile.close()

def registerUser():
    if not verifyUserFileExistance():
        writeHeader()
    with open('users/registered/users.csv', 'a', newline='') as csvfile:
        fields = [field_nickname, field_name, field_email, field_password]
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writerow({field_nickname: 'Nick', field_name: 'Nome', field_email: 'Email', field_password: 'Senha'})
        csvfile.close()

def showUsers():
    with open('users/registered/users.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row[field_nickname], row[field_name], row[field_email], row[field_password])
