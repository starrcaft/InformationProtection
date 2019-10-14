MAX_KEY_SIZE = 26

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

def getKey():
    key = 0
    inputKey = open('key.txt', 'rb').read().decode()
    return inputKey.split(',')


def encrypt(mode, fileName, key):
    outputFileName = 'encrypt.txt'
    if mode[0]== 'd':
        outputFileName = 'decrypt.txt'
    translated = ''
    outputFile = open(outputFileName, 'wb')
    inputFile = open(fileName, 'rb')
    message = inputFile.read().decode()
    count=0

    for keyInput in key :

        for symbol in message:
            translated += shift(symbol, keyInput[count])
            count=(count+1)%len(keyInput)

        outputFile.write((translated+'\n').encode())
        translated=""
    outputFile.close()
    inputFile.close()
    print('En(De)cryption complete')


def shift(symbol, key):
    return chr(ord(symbol)^ord(key))

encrypt(getMode(),getFileName(), getKey())