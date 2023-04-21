import random

from dialog.textObject import TextObject
from windows.interactiveWindow import InteractiveWindow
from windows.ui_ButtonObject import ButtonObject
import pygame
import sys
from pygame.locals import QUIT
import Joetilities.utilities
from windows.logWindow import LogWindow
from dataclasses import dataclass


@dataclass
class MapWindow(InteractiveWindow):

    def __init__(self, game_instance):
        super().__init__()
        self.x = 100
        self.w = 1000
        self.h = 600
        self.img = pygame.image.load('assets/dialog_window.png')
        self.img = pygame.transform.scale(self.img, (self.w, self.h))
        self.feed_status = True
        self.window_running = True

        self.x_spacing = 200
        self.col_0 = self.x + self.x_spacing - 100
        self.col_1 = self.col_0 + self.x_spacing
        self.col_2 = self.col_1 + self.x_spacing
        self.col_3 = self.col_2 + self.x_spacing

        self.row_0 = self.y + 140
        self.row_1 = self.row_0 + 80
        self.row_2 = self.row_1 + 80
        self.row_3 = self.row_2 + 80
        self.row_4 = self.row_3 + 80
        self.ui_elements = [

            TextObject(None, 'Network Map', self.col_0, self.y + 80, 36),

            ButtonObject(self.col_0, self.row_0, 80, 80, 'assets/red.png', object_id='top_left'),

            ButtonObject(self.col_0, self.row_4, 80, 80, 'assets/red.png', object_id='bottom_left'),

            ButtonObject(self.col_1, self.row_2, 80, 80, 'assets/red.png', object_id='bottom_middle'),

            ButtonObject(self.col_2, self.row_0, 80, 80, 'assets/red.png', object_id='top_right'),

            ButtonObject(self.col_2, self.row_4, 80, 80, 'assets/red.png', object_id='bottom_right'),

        ]
        # Run post initialization processes.
        self.__post__init__(game_instance)

    def __post__init__(self, game_instance) -> None:
        self.display(game_instance)

    def display(self, game_instance) -> None:

        while True:
            self.populate_menu_options(self.ui_elements)

            # Display the background dialog window
            game_instance.game_window.blit(self.img, (self.x, self.y))

            # Display all selection menu objects in menu_options list.
            self.draw_ui_objects(game_instance)

            # Get Mouse Position
            mouse_pos = pygame.mouse.get_pos()

            # get_mouse_selections
            for index, selection in enumerate(self.menu_options):
                if Joetilities.utilities.get_mouse_collision(mouse_pos, selection):
                    # Check if menu option is interactable
                    if selection.interactable:
                        self.selection = index
                    else:
                        self.selection = None

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
                        self.window_running = False
                        return

                if event.type == pygame.MOUSEBUTTONUP:
                    for index, selection in enumerate(self.menu_options):
                        if Joetilities.utilities.get_mouse_collision(mouse_pos, selection):
                            if selection.object_id == 'logs':
                                LogWindow(game_instance)

            pygame.display.update()

    def draw_ui_objects(self, game_instance):
        for index, selection in enumerate(self.menu_options):
            if index == self.selection:
                self.img_sel = pygame.transform.scale(self.img_sel, (selection.w, selection.h))
                game_instance.game_window.blit(selection.img, (selection.x, selection.y))
                game_instance.game_window.blit(self.img_sel, (selection.x, selection.y))
            else:
                game_instance.game_window.blit(selection.img, (selection.x, selection.y))
