import pickle

f = open('sr/img.jpg', 'rb')

content = f.read()

f.close()

f = open('ds/my_pic.jpg', 'wb')
f.write(content)
f.close()

print(len(content))

