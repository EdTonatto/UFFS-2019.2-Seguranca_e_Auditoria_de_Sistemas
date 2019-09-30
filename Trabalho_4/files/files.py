import globals
import utils

def createFilesPath():
    utils.createPath("files/" + globals.current_user_nickname + "/send_to")
    utils.createPath("files/" + globals.current_user_nickname + "/received_from")

def createSendFile(content):
    utils.createPath(globals.path_text_file)
    if (not utils.validatePathExistance(globals.path_text_file + "/" + globals.text_file)):
        with open(globals.path_text_file + "/" + globals.text_file, 'w') as newfile:
            newfile.write(content)
            newfile.close()
