import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.1.105', 5000))

s.listen(5)
print('listening for client..')

message = {
    'name': 'Tanvir Ahmed',
    'Id': '15162103110',
    'intake': 32,
    'email': 'tanvir@getd2.com'
}

msg = pickle.dumps(message)

while True:
    c, addr = s.accept()
    print(f'connected {addr}')

    c.send(msg)
    c.close()