import pygame
import pygame.camera
from pygame.locals import *
import pickle

pygame.init()
pygame.camera.init()

# img_size = (1280, 960)
img_size = (320, 240)
# img_size = (160, 120)

camlist = pygame.camera.list_cameras()
display_surface = pygame.display.set_mode(img_size)

cam = pygame.camera.Camera(camlist[0], img_size)
cam.start()
clock = pygame.time.Clock()

# counter = 0
while True:
    clock.tick(10)
    image = cam.get_image()

    # img = pickle.dumps(image)
    # imagen = pickle.loads(img)

    #converting image to string buffer and load (optional)
    imgs = pygame.image.tostring(image, "RGB")
    imagefs = pygame.image.fromstring(imgs, img_size, 'RGB')
    # print(type(imagefs))

    # print(f"dumps: {type(img)},    loads: {type(imagen)}")

    display_surface.blit(imagefs, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

            quit()
    
    pygame.display.update()
    # pygame.image.save(image, f"images/image_{counter}.jpg")
    # counter = counter + 1