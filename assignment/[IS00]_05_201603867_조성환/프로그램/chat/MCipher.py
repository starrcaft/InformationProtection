from Crypto.Cipher import AES

BS= 16
pad= lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

def setAES(key, iv):
    #TODO SET AES

    return AES.new(key,AES.MODE_CBC, iv)

def AES_Encrypt(cipher, data):
    #TODO DATA ENCRYPT
    

    return cipher.encrypt(pad(data).encode())#암호화를 위해 byte로

def AES_Decrypt(cipher, data):
    #TODO DATA DECRYPT

    return unpad(cipher.decrypt(data))#byte상태에서 unpad