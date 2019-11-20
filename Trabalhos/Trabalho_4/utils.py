import os
import globals

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pauseScreen():
    input("\nPressione <enter> para continuar")

def validatePathExistance(path):
    if (os.path.exists(path)):
        return True
    else:
        return False

def createPath(newpath):
    if (not validatePathExistance(newpath) == True):
        os.makedirs(newpath)
        return True
    return False

def updateTextFilePath(send_or_receive, file_name):
    path = ""
    globals.path_text_file = "files/"
    path = (globals.path_text_file +
            globals.current_user_nickname + "/" +
            send_or_receive + "/" +
            globals.current_other_user_nickname)
    globals.path_text_file = path

def updateTextFileName(newname):
    globals.text_file = newname + ".txt"

def updateOtherUserNickname(newnickname):
    globals.current_other_user_nickname = newnickname

def updateSettingsToSendFile(newname, newnickname):
    updateTextFileName(newname)
    updateOtherUserNickname(newnickname)
    updateTextFilePath("send_to", globals.text_file)

def updateCurrentUserData(nickname, name, email):
    globals.current_user_nickname = nickname
    globals.current_user_name = name
    globals.current_user_email = email
    globals.my_public_key = globals.current_user_nickname + "_public.key"
    globals.my_private_key = globals.current_user_nickname + "_private.key"
