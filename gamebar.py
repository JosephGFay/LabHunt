import pygame
from gameObject import GameObject

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)


class GameBar(GameObject):

    def __init__(self, x, y, w, h, img):
        super().__init__(x, y, w, h, img)
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = self.font.render('LAB HUNT', True, green, blue)
        self.textRect = self.text.get_rect()
