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
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if(key >= 1 and key <= MAX_KEY_SIZE):
            return key


def encrypt(mode, fileName, key):
    outputFileName = 'encrypt.txt'
    if mode[0]== 'd':
        key = -key
        outputFileName = 'decrypt.txt'
    translated = ''
    outputFile = open(outputFileName, 'w')
    inputFile = open(fileName, 'r')
    message = inputFile.read()

    for symbol in message:
        translated += shift(symbol, key)

    outputFile.write(translated)
    outputFile.close()
    inputFile.close()
    print('En(De)cryption complete')

def shift(symbol, key):
    if(key > 0) :
        if (ord(symbol) <= 122) and (ord(symbol) >= 97):
            if ord(symbol)+key > 122:
                symbol= chr(ord(symbol)-26)

        elif ord(symbol) >= 65 and ord(symbol) <= 90:
            if ord(symbol)+key > 90:
                symbol= chr(ord(symbol)-26)

    else :
        if (ord(symbol) <= 122) and (ord(symbol) >= 97):
            if ord(symbol)+key < 97:
                symbol= chr(ord(symbol)+26)

        elif ord(symbol) >= 65 and ord(symbol) <= 90:
            if ord(symbol)+key < 65:
                symbol= chr(ord(symbol)+26)
    symbol = chr(ord(symbol) + key)


    return symbol

encrypt(getMode(),getFileName(), getKey())
