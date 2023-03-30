from gameObject import GameObject
import pygame

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

class Player(GameObject):

  def __init__(self, x, y, w, h, img):
    super().__init__(x, y, w, h, img)
    self.render()
    
  def move_y(self, direction, max_height, objects):
    for object in objects:
      # Check window boundaries
      if (self.y >= max_height - self.h and direction > 0) or (self.y <= 0 and direction < 0):
        return 
  
      # Top collision
      # Check if top of player intersects with the bottom of an object.
      if self.y == object.y + object.h: 
        # Check if player is within the the bounds of object x and x + w on coordinate plane
        if (self.x >= object.x and self.x <= object.x + object.w) or (self.x + self.w > object.x and self.x + self.w < object.x+ object.w):
          if direction < 0:
            return

      # Bottom collision
      # check if bottom of player intersects with the top of an object
      if self.y + self.h == object.y:
        # Check if player is within the the bounds of object x and x + w on coordinate plane
        if (self.x >= object.x and self.x <= object.x + object.w) or (self.x + self.w > object.x and self.x + self.w < object.x+ object.w):
          if direction > 0:
            return
  
      # Move
    self.y += (direction * 2)
    self.render()
    

  def move_x(self, direction, max_width, objects):
    # Check window boundaries
    for object in objects:
      # Check window boundaries
      if (self.x >= max_width - self.w and direction > 0) or (self.x <= 0 and direction < 0):
        return
        
      # Left collision
      # Check if left of player intersects with the right of an object.
      if self.x == object.x + object.w: 
        # Check if player is within the the bounds of object y and y + h on coordinate plane
        if (self.y >= object.y and self.y <= object.y + object.h) or (self.y + self.h > object.y and self.y + self.h < object.y+ object.h):
          if direction < 0:
            return

      # Right collision
      # Check if right of player intersects with the left of an object.
      if self.x + self.w == object.x:
        # Check if player is within the the bounds of object y and y + h on coordinate plane
        if (self.y >= object.y and self.y <= object.y + object.h) or (self.y + self.h > object.y and self.y + self.h < object.y+ object.h):
          if direction > 0:
            return
      

      
    self.x += (direction * 2)
    self.render()
    
  def render(self):
    
    self.font = pygame.font.Font('freesansbold.ttf', 32)
    self.text = self.font.render(f'{self.x},{self.y}', True, green)
    self.textRect = self.text.get_rect()
    self.textRect.center = (self.x+30, self.y -30)
    self.imgs = [(self.img, (self.x, self.y)), (self.text, self.textRect)]