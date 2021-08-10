import socket
import pickle

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('192.168.1.105', 5000))

full_msg = b''

while True:
    msg = c.recv(10)
    if not msg:
        break

    full_msg += msg

message = pickle.loads(full_msg)
print(f'{message} {type(message)}')

