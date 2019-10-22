import socket
import MCipher

def client_program():
    host = '127.0.0.1'
    port = 5462
    
    keyRecive = False
    client_socket= socket.socket()
    client_socket.connect((host,port))
    
    if(keyRecive== False):
        key = client_socket.recv(1024)#key, iv를 byte로 받았으므로 디코딩
        prikey=MCipher.readPriKey()
        decryptedKey=MCipher.RSA_Decrypt(prikey, key)
        print('key : '+decryptedKey.decode())
        client_socket.send("key echange Success".encode())
        
        keyRecive = True
        
    client_socket.close()
    
if __name__ == '__main__':
    client_program()