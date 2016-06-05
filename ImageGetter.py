import pygame.image

class ImageGetter:
    def get_image(self, cam):
        img = cam.get_image()
        #pygame.image.save(img, "photo.bmp")
        return img
