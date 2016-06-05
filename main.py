import pygame.camera
import time
from ImageGetter import *
from AzureRequest import *

stop = False

pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
cam.start()

"""while not stop:
    img_getter = ImageGetter()
    capture = img_getter.get_image(cam)"""
ar = AzureRequest()
ar.request('{url: \'http://newsrescue.com/wp-content/uploads/2015/04/happy-person.jpg\'}')
    #time.sleep(3)

pygame.camera.quit()
