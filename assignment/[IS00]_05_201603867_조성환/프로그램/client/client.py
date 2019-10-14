import socket
import MCipher

def client_program():
    host = '127.0.0.1'
    port = 5462
    
    keyRecive = False
    client_socket= socket.socket()
    client_socket.connect((host,port))
    
    if(keyRecive== False):
        key = client_socket.recv(1024).decode()#key, iv를 byte로 받았으므로 디코딩
        print('key : '+key)
        client_socket.send("key echange Success".encode())
        iv = client_socket.recv(1024).decode()
        #iv= client_socket.recv(1024).decode()
        print('iv : '+iv)
        client_socket.send('iv exchange Success'.encode())
        keyRecive = True
        
    if (keyRecive):
        message = input(" -> ")
        while message.lower().strip() != 'bye':
            cipher= MCipher.setAES(key, iv)#byte로 key, iv를 받음.
            dataTosend= MCipher.AES_Encrypt(cipher,message)
            client_socket.send(dataTosend)
            
            data= client_socket.recv(1024) #수신 시 byte로 받음.
            cipher = MCipher.setAES(key, iv)# 연속으로 같이 쓸 수 없기 때문에 새로 set
            data = MCipher.AES_Decrypt(cipher, data)
            print('Received from user1 : '+ data.decode())#str로 프린트 하기 위해 디코딩
            message= input(" -> ")
    client_socket.close()
    
if __name__ == '__main__':
    client_program()