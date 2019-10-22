from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def RSA_Encrypt(pubkey, data):
    # TODO DATA ENCRYPT

    encryptor = PKCS1_OAEP.new(pubkey)

    return encryptor.encrypt(data.encode())

def RSA_Decrypt(prikey, data):
    # TODO DATA DECRYPT

    return prikey.decrypt(data)


def readPriKey():
    f = open("mypriKey.pem", "r")
    prikey = RSA.importKey(f.read())
    f.close()

    return prikey

def readPubKey():
    f = open(".mypubKey.pem", "r")
    pubkey = RSA.importKey(f.read())
    f.close()

    return pubkey
