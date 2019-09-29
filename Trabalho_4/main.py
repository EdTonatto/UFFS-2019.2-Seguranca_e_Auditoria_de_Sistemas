#from keys import keys
from users import users
import utils
import globals
#keys.gerarchaves()
#keys.printchaves()
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
