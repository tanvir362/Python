import socket
import time

import pygame
import pygame.camera
from pygame.locals import *
img_size = (320, 240)
clock = pygame.time.Clock()
frame_rate = 10


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.1.105', 5000))
s.listen(5)
print('listening for client..')

pygame.init()
pygame.camera.init()
camlist = pygame.camera.list_cameras()
cam = pygame.camera.Camera(camlist[0], img_size)

# cam.start()
# image = cam.get_image()
# cam.stop()
# imagets = pygame.image.tostring(image, 'RGB')

while True:
    c, addr = s.accept()
    print(f'connected {addr}')
    cam.start()
    while True:
        time.sleep(0.1)
        frame = cam.get_image()
        framets = pygame.image.tostring(frame, 'RGB')
        c.send(framets)
        

    cam.stop()
    c.close()