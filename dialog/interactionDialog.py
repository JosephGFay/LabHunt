from dialog.dialog import Dialog
import pygame

class InteractionDialog(Dialog):

  def __init__(self, game_instance, string):
    super().__init__(game_instance, string)
    pygame.display.update()
    self.run_dialog(game_instance)