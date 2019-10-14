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
        print('Enter the key ' )
        key = input()
        return key

def encrypt(mode, fileName, key):
    outputFileName = 'encrypt.txt'
    if mode[0]== 'd':
        outputFileName = 'decrypt.txt'
    translated = ''
    outputFile = open(outputFileName, 'wb')
    inputFile = open(fileName, 'rb')
    message = inputFile.read().decode()

    count=0
    for symbol in message:
        translated += shift(symbol, key[count])
        print(ord(symbol))
        (count+1)%len(key)

    print(ord(chr(13)))
    outputFile.write(translated.encode())
    outputFile.close()
    inputFile.close()
    print('En(De)cryption complete')
    print(translated)

def shift(symbol, key):
        return chr(ord(symbol)^ord(key))

encrypt(getMode(),getFileName(), getKey())

