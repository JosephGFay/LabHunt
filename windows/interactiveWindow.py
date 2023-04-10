import pygame
from pygame.locals import QUIT
import sys
from gameObjects.gameObject import GameObject
import Joetilities.utilities


class InteractiveWindow(GameObject):
    """
        A class to represent an Interactive Menu Window prototype.

    Attributes
    ----------
    x : int
      A coordinate value to be used for horizontal positioning.
    y : int
      A coordinate value to be used for vertical positioning
    w : int
      Determines the width of the object.
    h : int
      Determines the height of the object.
    img : str
      String path to image file.
    """

    def __init__(self) -> None:
        """
            Constructor method for the Interactive Window
            @rtype: None
        """

        # Attributes
        self.x = 300
        self.y = 150
        self.w = 600
        self.h = 600

        self.col_0 = None
        self.col_1 = None
        self.col_2 = None
        self.col_3 = None

        self.row_0 = None
        self.row_1 = None

        self.img = pygame.image.load('assets/dialog_window.png')
        self.img = pygame.transform.scale(self.img, (self.w, self.h))
        self.img_sel = pygame.image.load('assets/cyan.png')
        self.selection = None
        self.menu_options = []

        self.img.convert_alpha()
        self.img_sel.convert_alpha()
        # Call to GameObject Constructor using default class attributes
        super().__init__(self.x, self.y, self.w, self.h)

    def populate_menu_options(self, option_list: list) -> None:

        self.menu_options = option_list
