from Crypto.Cipher import AES
import base64
from Crypto.Util import Counter

def getMode():
    while True:
        print('Enter either "encrypt" or "e" or "decrypt" or "d". ')
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('The value you entered its invalid')

def getFileName():
    print('Enter your file name:')
    return input()

def crypto(mode, fileName):
    iv= 'asefasdfefsdsdfe'.encode('utf-8')
    key= 'thisisbadkeyokey'.encode('utf-8')

    counter = Counter.new(128)
    cipher = AES.new(bytearray(key), AES.MODE_CTR, counter=counter)
    outputFileName = 'encrypt.txt'
    if mode[0] == 'd':
        outputFileName = 'decrypt.txt'
        inputFile = open(fileName, 'rb')
    else:
        inputFile = open(fileName, 'r')
    message = inputFile.read()
    translated = ''
    outputFile = open(outputFileName, 'wb')

    if mode[0]=='d':
        translated=unpad(cipher.decrypt(base64.b64decode(message)))
    else:
        translated = base64.b64encode(cipher.encrypt(pad(message).encode('ascii')))

    outputFile.write(translated)
    outputFile.close()
    inputFile.close()
    print('En(De)cryption complete')

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
crypto(getMode(), getFileName())



