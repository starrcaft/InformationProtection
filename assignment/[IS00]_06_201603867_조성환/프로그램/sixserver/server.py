import socket
import MCipher


def server_program():
    host = '127.0.0.1'
    port = 5462

    f = open("mypriKey.pem", "r")
    pubkey = MCipher.readPubKey()
    prikey = MCipher.readPriKey()

    key = 'thisisbadkeyokeythisisbadkeyokey'
    encryptKey = MCipher.RSA_Encrypt(pubkey, key)
    iv = 'ivisinitialvetor'.encode()

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()
    conn.send(encryptKey)
    print(conn.recv(1024).decode())

    print("Connection from: " + str(address))

    conn.close()


if __name__ == '__main__':
    server_program()