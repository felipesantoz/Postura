import pygame.camera
import time
from ImageGetter import *
from AzureRequest import *
from DataParser import *
from DataAnalyzer import *

stop = False

pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
cam.start()
ar = AzureRequest()
data_parser = DataParser()

while not stop:
    img_getter = ImageGetter()
    capture = img_getter.get_image(cam)
    data_parser.set_data(ar.request('{url: \'http://newsrescue.com/wp-content/uploads/2015/04/happy-person.jpg\'}'))
    print data_parser.parse()
    time.sleep(3)

pygame.camera.quit()
