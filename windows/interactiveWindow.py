import pygame
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

    def __init__(self: object) -> None:
        """
        Constructor method for the Interactive Window
        @rtype: None
        """
        # Attributes
        self.x = 300
        self.y = 150
        self.w = 600
        self.h = 600
        self.img = pygame.image.load('assets/dialog_window.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (self.w, self.h))

        self.img_idle = pygame.image.load('assets/red.png').convert_alpha()
        self.img_idle = pygame.transform.scale(self.img_idle, (100, 120))

        self.img_sel = pygame.image.load('assets/green.png').convert_alpha()
        self.img_sel = pygame.transform.scale(self.img_sel, (100, 120))

        self.selection = 0

        self.selection_0 = GameObject(self.x + 45, self.y + 40, 100, 120, 'assets/red.png')
        self.selection_1 = GameObject(self.x + 45 * 4, self.y + 40, 100, 120, 'assets/red.png')
        self.selection_2 = GameObject(self.x + 45 * 7, self.y + 40, 100, 120, 'assets/red.png')
        self.selection_3 = GameObject(self.x + 45 * 10, self.y + 40, 100, 120, 'assets/red.png')
        # Call to GameObject Constructor using default class attributes
        super().__init__(self.x, self.y, self.w, self.h)

        self.menu_options = [
            self.selection_0,
            self.selection_1,
            self.selection_2,
            self.selection_3,
        ]

    def display(self, game_instance):

        # Display the background dialog window
        game_instance.game_window.blit(self.img, (self.x, self.y))

        # Window Running Loop for the instance.
        while True:

            # Display all selection menu objects in menu_options list.
            for index, selection in enumerate(self.menu_options):

                if index == self.selection:
                    selection.img = self.img_sel
                else:
                    selection.img = self.img_idle

                game_instance.game_window.blit(selection.img, (selection.x, selection.y))

            # Get Mouse Position
            mouse_pos = pygame.mouse.get_pos()
            for index, selection in enumerate(self.menu_options):
                if Joetilities.utilities.get_mouse_collision(mouse_pos, selection):
                    self.selection = index

            # Event Listener
            for event in pygame.event.get():
                # Listen for KEY events
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
            pygame.display.update()
