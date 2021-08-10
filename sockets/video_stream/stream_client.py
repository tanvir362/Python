import socket

import pygame
import pygame.camera
from pygame.locals import *
img_size = (320, 240)

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('192.168.1.105', 5000))

pygame.init()
display_surface = pygame.display.set_mode(img_size)


while True:
    full_msg = b''
    while True:
        msg = c.recv(10)
        if not msg:
            break
        full_msg+=msg
    
    frame = pygame.image.fromstring(full_msg, img_size, 'RGB')
    display_surface.blit(frame, (0, 0))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

            quit()



# f = open('ds/rcv_pic.jpg', 'wb')
# f.write(full_img)
# f.close()



