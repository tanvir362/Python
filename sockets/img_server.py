import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.1.105', 5000))

s.listen(5)
print('listening for client..')

f = open('sr/music.mp3', 'rb')
img = f.read()
f.close()
print('file reading completed!')

while True:
    c, addr = s.accept()
    print(f'connected {addr}')

    c.send(img)
    c.close()
    print('sent!')