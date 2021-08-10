from socket import socket
import time

c = socket()

c.connect(('192.168.1.105', 5000))

name = input('Enter your name: ')
c.send(bytes(name, 'utf-8'))

counter = 0
while True:

    try:
        msg = c.recv(1024).decode()
        if msg == '':
            break
    
        print('received: {} {}'.format(msg, type(msg)))
        
        print(counter)
        counter = counter + 1
        
    except Exception as e:
        print(str(e))
        break


    

