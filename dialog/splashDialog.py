import pygame
from dialog.dialog import Dialog
from dialog.textObject import TextObject

class SplashDialog(Dialog):

  def __init__(self, game_instance, string):
    super().__init__(game_instance, string)
    TextObject(game_instance, 'A threat actor posing as a student has infilitrated the lab.', self.x+10, self.y+30+30)
    TextObject(game_instance, 'Investigate and monitor the network for traces of suspicious ', self.x+10, self.y+50+30)
    TextObject(game_instance, 'activity in order to expose the threat actor within the room.', self.x+10, self.y+70+30)
    pygame.display.update()
    self.run_dialog(game_instance)
    