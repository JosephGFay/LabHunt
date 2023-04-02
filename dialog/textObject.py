import pygame

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

class TextObject:
  def __init__(self, game_instance, string, x, y):
    self.font = pygame.font.Font('freesansbold.ttf', 12)
    self.text = self.font.render(string, True, white)
    self.textRect = self.text.get_rect(x=x, y=y)
    game_instance.game_window.blit(self.text, self.textRect)
