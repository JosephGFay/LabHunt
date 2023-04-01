from gameObject import GameObject
from npc import NPC
import pygame
import random
green = (0, 255, 0)

class Table(GameObject):

  def __init__(self, x, y, w, h, img, name):
    super().__init__(x, y, w, h, img, name)
    self.infected = False
    self.render()
    self.top_seat = (
      # X
      (self.x) + 46,
      # y
      self.y - 64
    )
    self.right_seat = (
      # X
      (self.x + self.w),
      # Y
      ((self.y) + 46)
    )
    self.left_seat = (
      # X
      (self.x - 64),
      # Y
      ((self.y) + 46)
    )
    self.bottom_seat = (
      # X
      (self.x) + 46,
      # y
      (self.y + self.h)
    )
    

    self.npc_top = NPC(self.top_seat[0], self.top_seat[1], 60 , 100, 'assets/nuetral.png')
    self.npc_right = NPC(self.right_seat[0], self.right_seat[1], 60 , 100, 'assets/npc_right.png')
    self.npc_left = NPC(self.left_seat[0], self.left_seat[1], 60 , 100, 'assets/npc_left.png')
    self.npc_bottom = NPC(self.bottom_seat[0], self.bottom_seat[1], 60 , 100, 'assets/nuetral.png')

    
    self.npcs = [self.npc_top, self.npc_right, self.npc_left, self.npc_bottom]
    
    
  def render(self):
      self.font = pygame.font.Font('freesansbold.ttf', 16)
      self.text = self.font.render('Infected' if self.infected else self.name, True, green)
      self.textRect = self.text.get_rect()
      self.textRect.center = (self.x+80, self.y + 70)
      if self.infected:
        self.get_hacker(self.npcs)

  def get_hacker(self, npc_list):
    infected_seat = random.randint(0, 3)
    npc_list[infected_seat].infected = True
    

  