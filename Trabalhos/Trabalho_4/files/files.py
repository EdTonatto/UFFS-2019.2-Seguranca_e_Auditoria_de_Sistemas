import globals
import utils

#####========================================ENVIO DE ARQUIVO========================================#####
#Função para chamada criar os diretórios de arquivos enviados e recebidos do usuário logado.
#Formato do caminho do diretório será:
##Considerando o login do usuário como Jack, ficará assim:
###"files/Jack/send_to" para os arquivos enviados.
###"files/Jack/received_from" para os arquivos recebidos.
def createFilesPath():
    utils.createPath("files/" + globals.current_user_nickname + "/send_to")
    utils.createPath("files/" + globals.current_user_nickname + "/received_from")

#Irá criar, caso ainda não exista, um arquivo no formato .txt com o nome que estiver informado na variavel de controle global "text_file".
#O caminho para o arquivo de texto seguirá o padrão comentado na descrição da função files.createFilesPath().
##A diferença será que irá adicionar, ou reutilizar, um diretório com o nome do destinatário da mensagem
##Exemplo: Jack está enviando o arquivo com nome Documento.txt para Bill. O caminho do arquivo será:
###files/Jack/send_to/Bill/Documento.txt
def createSendFile(content):
    utils.createPath(globals.path_text_file)
    if (not utils.validatePathExistance(globals.path_text_file + "/" + globals.text_file)):
        with open(globals.path_text_file + "/" + globals.text_file, 'w') as newfile:
            newfile.write(content)
            newfile.close()
        print("Arquivo com nome '{name}' criado com sucesso na pasta com caminho: '{path}'.\nArquivo criado com sucesso!".format(name=globals.text_file, path=globals.path_text_file))
        return True
    else:
        print("Arquivo com nome '{name}' não foi criado na pasta com caminho: '{path}'.\nArquivo já existente!".format(name=globals.text_file, path=globals.path_text_file))
#####========================================ENVIO DE ARQUIVO========================================#####
