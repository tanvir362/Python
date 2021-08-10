from socket import socket
import time

s = socket()
print('socket created')

s.bind(('192.168.1.105', 5000))

s.listen(3)
print('listening for client')

while True:
    c, addr = s.accept()

    name = c.recv(1024).decode()
    print('{} connected'.format(name),addr)
    
    c.send(bytes('Tanvir greets you, {}'.format(name), 'utf-8'))

    counter = 0
    while counter < 5:

        msg = input('what you want to sent: ')

        time.sleep(1)
        c.send(bytes(msg, 'utf-8'))
        print('sent: {}'.format(msg))
        counter = counter+1
    
    c.close()

