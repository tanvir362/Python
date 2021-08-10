import socket
import pickle

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('192.168.1.105', 5000))

full_img = b''

while True:
    img = c.recv(10)
    if not img:
        break

    full_img += img

print('received!')

f = open('ds/rcv_pic.jpg', 'wb')
f.write(full_img)
f.close()



