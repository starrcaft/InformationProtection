from Crypto.Cipher import AES
import base64

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


def setAES(key, iv):
    # TODO SET AES

    return AES.new(key.encode(), AES.MODE_CBC, iv.encode())


def AES_Encrypt(cipher, data):
    # TODO DATA ENCRYPT
    
    return cipher.encrypt(pad(data).encode())


def AES_Decrypt(cipher, data):
    # TODO DATA DECRYPT

    return unpad(cipher.decrypt(data))