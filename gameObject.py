import pygame

class GameObject:

  def __init__(self, x, y, w, h, img):
    img = pygame.image.load(img).convert_alpha()
    self.img = pygame.transform.scale(img, (w, h))
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    

