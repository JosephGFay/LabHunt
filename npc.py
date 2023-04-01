from gameObject import GameObject
import pygame
class NPC(GameObject):

  def __init__(self, x, y, w, h, img):
    super().__init__(x, y, w, h, img)
    self.infected = False
    self.check_infected()

  def check_infected(self):
    if self.infected:
      img = pygame.image.load('assets/hacker.png').convert_alpha()
      self.img = pygame.transform.scale(img, (self.w, self.h))
    