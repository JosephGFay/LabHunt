import pygame
from gameObjects.gameObject import GameObject

white = (255, 255, 255)
green = (0, 255, 0)
blue = (32, 32, 49)


class ToolBar(GameObject):

    def __init__(self, x, y, w, h, img):
        super().__init__(x, y, w, h, img)
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = self.font.render('Tools', True, white, blue)
        self.textRect = self.text.get_rect()
