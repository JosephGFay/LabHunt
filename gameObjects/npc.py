from gameObjects.gameObject import GameObject
import pygame

SPRITES = [
  'assets/hacker_top.png',
  'assets/hacker_right.png',
  'assets/hacker_left.png',
  'assets/hacker_bottom.png',
]
class NPC(GameObject):
  
  def __init__(self, x, y, w, h, img):
    super().__init__(x, y, w, h, img)
    self.infected = False
    self.infected_seat = None
    self.check_infected()

  def check_infected(self):
    # Check to see if an NPC is infected.
    if self.infected:
      self.set_hacker_visible()
      
  def set_hacker_visible(self):
    # Change sprites if infected to hacker sprite
      for i in range(4):
        if self.infected_seat == i:
          img = pygame.image.load(SPRITES[i]).convert_alpha()
          self.img = pygame.transform.scale(img, (self.w, self.h))