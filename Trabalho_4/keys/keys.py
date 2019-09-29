import rsa
import globals
import os

def setBitsizeRSA():
    print("Bitsize atual RSA: {bitsize} bits.".format(bitsize=globals.rsa_key_size))
    newbitsize = input("Informe o novo bitsize: ")
    globals.rsa_key_size = int(newbitsize)
    print("Bitsize atualizado para {bitsize} bits.".format(bitsize=globals.rsa_key_size))

def getPrivateKey():
    with open(globals.path_private_key + globals.private_key, mode='r') as privatefile:
        keydata = privatefile.read()
        return keydata

def getPublicKey():
    with open(globals.path_public_key + globals.public_key, mode='r') as publicfile:
        keydata = publicfile.read()
        return keydata

def showKeys():
    if (validateKeysFileExistance() ==  True):
        print(getPrivateKey())
        print(getPublicKey())
        return True
    return False

def deleteKeysFile():
    try:
        if (validateKeysFileExistance() == True):
            os.remove(globals.path_private_key + globals.private_key)
            os.remove(globals.path_public_key + globals.public_key)
            print("Arquivos '{pathpvk}' e '{pathpbk}' excluidos com sucesso.".format(
                                                                                pathpvk=globals.path_private_key + globals.private_key,
                                                                                pathpbk=globals.path_public_key + globals.public_key))
        else:
            print("Arquivos '{pathpvk}' e '{pathpbk}' nao foram encontrados.".format(
                                                                                pathpvk=globals.path_private_key + globals.private_key,
                                                                                pathpbk=globals.path_public_key + globals.public_key))
    except:
        print("Arquivos '{pathpvk}' e '{pathpbk}' nao foram encontrados.".format(
                                                                            pathpvk=globals.path_private_key + globals.private_key,
                                                                            pathpbk=globals.path_public_key + globals.public_key))

def generateKeys():
    if (validateKeysFileExistance() == False):
        (publickey, privatekey) = rsa.newkeys(globals.rsa_key_size)
        with open(globals.path_private_key + globals.private_key, 'w') as privatekeyfile:
            privatekeyfile.write(str(privatekey))
            privatekeyfile.close()
        with open(globals.path_public_key + globals.public_key, 'w') as publickeyfile:
            publickeyfile.write(str(publickey))
            publickeyfile.close()
        return True
    return False

def validateKeysFileExistance():
    ret = False
    try:
        with open(globals.path_private_key + globals.private_key, mode='r') as privatefile:
            with open(globals.path_public_key + globals.public_key, mode='r') as publicfile:
                ret = True
        return ret
    except:
        return ret
