from gameObject import GameObject
import pygame

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

class Player(GameObject):

  def __init__(self, x, y, w, h, img):
    super().__init__(x, y, w, h, img)
    self.render()
    
  def move_y(self, direction, max_height, object):
    if (self.y >= max_height - self.h and direction > 0) or (self.y <= 0 and direction < 0):
      return 

    # Top collision
    if (self.y <= object.y + object.h and direction < 0) and ((self.x > object.x and self.x < object.x+object.w) or (self.x + self.w > object.x and self.x + self.w < object.x+object.w)):
      return 
    self.y += (direction * 3)
    self.render()
    

  def move_x(self, direction, max_width):
    if (self.x >= max_width - self.w and direction > 0) or (self.x <= 0 and direction < 0):
      return
    self.x += (direction * 3)
    self.render()
    
  def render(self):
    
    self.font = pygame.font.Font('freesansbold.ttf', 32)
    self.text = self.font.render(f'{self.x},{self.y}', True, green)
    self.textRect = self.text.get_rect()
    self.textRect.center = (self.x+30, self.y -30)
    self.imgs = [(self.img, (self.x, self.y)), (self.text, self.textRect)]