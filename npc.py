from gameObject import GameObject
import pygame
class NPC(GameObject):

  def __init__(self, x, y, w, h, img):
    super().__init__(x, y, w, h, img)
    self.infected = False
    self.infected_seat = None
    self.check_infected()

  def check_infected(self):
    if self.infected:
      if self.infected_seat == 0:
        img = pygame.image.load('assets/hacker_top.png').convert_alpha()
        self.img = pygame.transform.scale(img, (self.w, self.h))
      elif self.infected_seat == 1:
        img = pygame.image.load('assets/hacker_right.png').convert_alpha()
        self.img = pygame.transform.scale(img, (self.w, self.h))
      elif self.infected_seat == 2:
        img = pygame.image.load('assets/hacker_left.png').convert_alpha()
        self.img = pygame.transform.scale(img, (self.w, self.h))
      elif self.infected_seat == 3:
        img = pygame.image.load('assets/hacker_bottom.png').convert_alpha()
        self.img = pygame.transform.scale(img, (self.w, self.h))
      
    