import socket
import MCipher

def server_program():
    host = '127.0.0.1'
    port = 5462
    
    key= 'thisisbadkeyokeythisisbadkeyokey'.encode()#전송, 암호화를 위해 byte로
    iv= 'ivisinitialvetor'.encode()
    
    server_socket= socket.socket()
    server_socket.bind((host,port))
    
    server_socket.listen(2)
    conn, address= server_socket.accept()
    conn.send(key)
    print(conn.recv(1024).decode())
    conn.send(iv)
    print(conn.recv(1024).decode())
    
    print("Connection from: "+ str(address))
    
    while True:
        rdata= conn.recv(1024)#byte 형태
        if not rdata:
            break
        data= rdata
        cipher= MCipher.setAES(key, iv)#cipher시 encode 하는 이유: c code이기 때문에 byte로
        data= MCipher.AES_Decrypt(cipher, data)
        print("Recieved from user2 : "+ str(data.decode()))#byte를 프린트하기 위해 str로 디코딩
        data= input(' -> ')
        cipher = MCipher.setAES(key, iv)#연속으로 같이 쓸 수 없기 때문에 새로 cipher set
        data = MCipher.AES_Encrypt(cipher, data)
        conn.send(data)#암호화 과정에서 byte가 됐으므로 그대로 전송
        
    conn.close()
    
if __name__=='__main__':
    server_program()