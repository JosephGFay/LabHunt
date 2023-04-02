import pygame
from dialog.dialogWindow import DialogWindow
from dialog.textObject import TextObject

class SplashWindow(DialogWindow):

  def __init__(self, game_instance, string):
    super().__init__(game_instance, string)
    TextObject(game_instance, 'Hello World', self.x+10, self.y+30)
    TextObject(game_instance, 'Hello World', self.x+10, self.y+50)
    TextObject(game_instance, 'Hello World', self.x+10, self.y+70)
    pygame.display.update()
    self.run_dialog(game_instance)
    