import time
import pygame
import pygame.camera
from pygame.locals import *

img_size = (320, 240)

pygame.init()
pygame.camera.init()
camlist = pygame.camera.list_cameras()
display_surface = pygame.display.set_mode(img_size)

cam = pygame.camera.Camera(camlist[0], img_size)
cam.start()
# clock = pygame.time.Clock()

while True:
    # clock.tick(10)
    time.sleep(0.1)
    image = cam.get_image()

    display_surface.blit(image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

            quit()
    
    pygame.display.update()
    