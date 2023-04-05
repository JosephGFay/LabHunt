import pygame
from gameObjects.gameObject import GameObject
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

class InteractiveWindow(GameObject):
  def __init__(self):
    x = 400
    y = 200
    w = 600
    h = 600
    img = 'assets/dialog_window.png'
    self.img_sel = pygame.image.load('assets/green.png').convert_alpha()
    super().__init__(x, y, w, h, img)
    self.selection = 0
    
    self.selection_0 = GameObject(self.x+45, self.y+40, 100, 120, 'assets/red.png')
    self.selection_1 = GameObject(self.x+45*4, self.y+40, 100, 120, 'assets/red.png')
    self.selection_2 = GameObject(self.x+45*7, self.y+40, 100, 120, 'assets/red.png')
    self.selection_3 = GameObject(self.x+45*10, self.y+40, 100, 120, 'assets/red.png')

    self.menu_options = [
      self.selection_0, 
      self.selection_1,
      self.selection_2,
      self.selection_3,
    ]

    
    
  def display(self, game_instance):
    game_instance.game_window.blit(self.img, (self.x-10, self.y-28))
    for option in self.menu_options:
      game_instance.game_window.blit(option.img, (option.x, option.y))
    pygame.display.update()

    while True:
      self.menu_options[self.selection].img = self.img_sel
      self.display(game_instance)
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            game_instance.draw_objects()
            return
          if event.key == pygame.K_LEFT:
            if self.selection != 0:
              self.selection -= 1
          if event.key == pygame.K_RIGHT:
            if self.selection != 3:
              self.selection += 1 
    
