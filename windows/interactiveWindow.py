import pygame
from gameObjects.gameObject import GameObject
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

class InteractiveWindow(GameObject):
  def __init__(self, game_instance, string):
    x = 400
    y = 200
    w = 600
    h = 600
    img = 'assets/dialog_window.png'
    super().__init__(x, y, w, h, img)
    game_instance.dialog_running = True
    game_instance.game_window.blit(self.img, (self.x-10, self.y-28))
    pygame.display.update()
    

  def run_dialog(self, game_instance):
    while game_instance.dialog_running:
        for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
              game_instance.dialog_running = False
    
  
