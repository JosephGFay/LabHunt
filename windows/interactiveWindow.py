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
    x = 300
    y = 150
    w = 600
    h = 600

    col_0 = None
    col_1 = None
    col_2 = None
    col_3 = None

    row_0 = None
    row_1 = None

    img = pygame.image.load('assets/dialog_window.png')
    img = pygame.transform.scale(img, (w, h))
    img_sel = pygame.image.load('assets/cyan.png')
    selection = None
    menu_options = []

    def __init__(self) -> None:
        """
        Constructor method for the Interactive Window
        @rtype: None
        """
        # Attributes
        self.img.convert_alpha()
        self.img_sel.convert_alpha()
        # Call to GameObject Constructor using default class attributes
        super().__init__(self.x, self.y, self.w, self.h)

    def populate_menu_options(self, option_list: list) -> None:
        for option in option_list:
            self.menu_options.append(option)

    def display(self, game_instance):

        # Window Running Loop for the instance.
        while True:

            # Display the background dialog window
            game_instance.game_window.blit(self.img, (self.x, self.y))

            # Display all selection menu objects in menu_options list.
            for index, selection in enumerate(self.menu_options):

                if index == self.selection:
                    self.img_sel = pygame.transform.scale(self.img_sel, (selection.w, selection.h))
                    game_instance.game_window.blit(selection.img, (selection.x, selection.y))
                    game_instance.game_window.blit(self.img_sel, (selection.x, selection.y))
                else:
                    game_instance.game_window.blit(selection.img, (selection.x, selection.y))

            # Get Mouse Position
            mouse_pos = pygame.mouse.get_pos()
            for index, selection in enumerate(self.menu_options):
                if Joetilities.utilities.get_mouse_collision(mouse_pos, selection):
                    # Check if menu option is interactable
                    if selection.interactable:
                        self.selection = index

            # Event Listener
            for event in pygame.event.get():
                if event.type == QUIT:
                    # Quit the game if event fired.
                    pygame.quit()
                    sys.exit()
                # Listen for KEY events
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_instance.draw_objects()
                        return
            pygame.display.update()
