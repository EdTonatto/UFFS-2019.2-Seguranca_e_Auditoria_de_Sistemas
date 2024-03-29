import rsa
import globals
import os

def getPrivateKey(): ##DA PRA UNIFICAR EM UMA getKey(usuario, tipochave)
    with open(globals.path_private_key + globals.my_private_key, mode='r') as privatefile:
        keydata = privatefile.read()
        return keydata

def getPublicKey(): ##DA PRA UNIFICAR EM UMA getKey(usuario, tipochave)
    with open(globals.path_public_key + globals.my_public_key, mode='r') as publicfile:
        keydata = publicfile.read()
        return keydata

def getOtherPublicKey(): ##DA PRA UNIFICAR EM UMA getKey(usuario, tipochave)
    if (validateKeysFileExistance(globals.other_private_key, globals.other_public_key) == True):
        with open(globals.path_public_key + globals.other_public_key, mode='r') as publicfile:
            keydata = publicfile.read()
            return keydata

def getKey(keypath, userkey):
    if (utils.validatePathExistance(keypath + userkey) == True):
        with open(keypath + userkey) as key:
            keydata = key.read()
            return keydata

def validateKeysFileExistance(pvkeyfile, pbkeyfile): #da pra tentar utilizar o utils.validatePathExistance
    ret = False
    try:
        with open(globals.path_private_key + pvkeyfile, mode='r') as privatefile:
            with open(globals.path_public_key + pbkeyfile, mode='r') as publicfile:
                ret = True
        return ret
    except:
        return ret

def setBitsizeRSA(): ##
    print("Bitsize atual RSA: {bitsize} bits.".format(bitsize=globals.rsa_key_size))
    newbitsize = input("Informe o novo bitsize: ")
    globals.rsa_key_size = int(newbitsize)
    print("Bitsize atualizado para {bitsize} bits.".format(bitsize=globals.rsa_key_size))

def showKeys(): ##
    if (validateKeysFileExistance(globals.my_private_key, globals.my_public_key)  ==  True):
        print(getPrivateKey())
        print(getPublicKey())
        return True
    return False

def showOtherPublicKey(): ##
    print(getOtherPublicKey())

def deleteKeysFile(): ##
    def printNotFound():
        print("Arquivos '{pathpvk}' e '{pathpbk}' nao foram encontrados.".format(
                                                                            pathpvk=globals.path_private_key + globals.my_private_key,
                                                                            pathpbk=globals.path_public_key + globals.my_public_key))
    def printSuccess():
        print("Arquivos '{pathpvk}' e '{pathpbk}' excluidos com sucesso.".format(
                                                                            pathpvk=globals.path_private_key + globals.my_private_key,
                                                                            pathpbk=globals.path_public_key + globals.my_public_key))
    try:
        if (validateKeysFileExistance(globals.my_private_key, globals.my_public_key)  == True):
            os.remove(globals.path_private_key + globals.my_private_key)
            os.remove(globals.path_public_key + globals.my_public_key)
            printSuccess()
        else:
            printNotFound()
    except:
        printNotFound()

def generateKeys(): ##
    if (validateKeysFileExistance(globals.my_private_key, globals.my_public_key)  == False):
        (publickey, privatekey) = rsa.newkeys(globals.rsa_key_size)
        with open(globals.path_private_key + globals.my_private_key, 'w') as privatekeyfile:
            privatekeyfile.write(str(privatekey))
            privatekeyfile.close()
        with open(globals.path_public_key + globals.my_public_key, 'w') as publickeyfile:
            publickeyfile.write(str(publickey))
            publickeyfile.close()
        return True
    return False
