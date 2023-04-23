import random

from dialog.textObject import TextObject
from windows.interactiveWindow import InteractiveWindow
from windows.ui_ButtonObject import ButtonObject
from windows.ui_Object import UIObject
import pygame
import sys
from pygame.locals import QUIT
import Joetilities.utilities
from dataclasses import dataclass

black = (0, 0, 0)
@dataclass
class MapWindow(InteractiveWindow):

    def __init__(self, game_instance):
        super().__init__()
        self.x = 100
        self.w = 1000
        self.h = 600
        self.img = pygame.image.load('assets/map_window.png')
        self.img = pygame.transform.scale(self.img, (self.w, self.h))
        self.feed_status = True
        self.window_running = True
        self.game_instance = game_instance

        self.x_spacing = 200
        self.col_0 = self.x + self.x_spacing - 100
        self.col_1 = self.col_0 + self.x_spacing
        self.col_2 = self.col_1 + self.x_spacing
        self.col_3 = self.col_2 + self.x_spacing
        self.col_4 = self.col_3 + 70

        self.y_spacing = 60
        self.row_0 = self.y + 140
        self.row_1 = self.row_0 + self.y_spacing
        self.row_2 = self.row_1 + self.y_spacing
        self.row_3 = self.row_2 + self.y_spacing
        self.row_4 = self.row_3 + self.y_spacing

        self.info_ui = [
            TextObject(None, f'Select a table to view info', self.col_4-20, self.row_2, 12, black),
            TextObject(None, 'Info', self.col_3, self.y + 120, 36, black)
        ]
        self.ui_elements = [

            TextObject(None, 'Network Map', self.col_0, self.y + 80, 24, black),

            ButtonObject(self.col_0, self.row_0, 80, 80, 'assets/table_blue.png', object_id='top_left'),

            ButtonObject(self.col_0, self.row_3, 80, 80, 'assets/table_red.png', object_id='bottom_left'),

            ButtonObject(self.col_1, self.row_2, 80, 80, 'assets/table_red.png', object_id='middle'),

            ButtonObject(self.col_1, self.row_4, 80, 80, 'assets/table_red.png', object_id='bottom_middle'),

            UIObject(self.col_2, self.row_2, 80, 80, 'assets/server.png'),

            ButtonObject(self.col_2, self.row_0, 80, 80, 'assets/table_red.png', object_id='top_right'),

            ButtonObject(self.col_2, self.row_4, 80, 80, 'assets/table_blue.png', object_id='bottom_right'),
        ]

        # Run post initialization processes.
        self.__post__init__()

    def __post__init__(self) -> None:
        self.display()

    def populate_info(self, table_button) -> None:
        table = None

        match table_button.object_id:
            case 'top_left':
                table = self.game_instance.tables[1]
            case 'bottom_left':
                table = self.game_instance.tables[0]
            case 'middle':
                table = self.game_instance.tables[4]
            case 'bottom_middle':
                table = self.game_instance.tables[3]
            case 'top_right':
                table = self.game_instance.tables[5]
            case 'bottom_right':
                table = self.game_instance.tables[2]
            case 'server':
                pass

        for npc in table.npcs:
            print(npc.name)
        self.display_info(table)

    def display_info(self, table):
        y_spacing = 80
        row_0 = self.row_0
        row_1 = row_0 + y_spacing
        row_2 = row_1 + y_spacing
        row_3 = row_2 + y_spacing
        self.info_ui = [
            # Monitor Images
            UIObject(self.col_3, row_0, 64, 64, 'assets/monitor.png'),
            UIObject(self.col_3, row_1, 64, 64, 'assets/monitor.png'),
            UIObject(self.col_3, row_2, 64, 64, 'assets/monitor.png'),
            UIObject(self.col_3, row_3, 64, 64, 'assets/monitor.png'),

            # IP Addresses
            TextObject(None, f'{table.npcs[0].ip}', self.col_4, row_0, 12, black),
            TextObject(None, f'{table.npcs[1].ip}', self.col_4, row_1, 12, black),
            TextObject(None, f'{table.npcs[2].ip}', self.col_4, row_2, 12, black),
            TextObject(None, f'{table.npcs[3].ip}', self.col_4, row_3, 12, black),

            # Mac Addresses
            TextObject(None, f'{table.npcs[0].mac}', self.col_4, row_0+20, 12, black),
            TextObject(None, f'{table.npcs[1].mac}', self.col_4, row_1+20, 12, black),
            TextObject(None, f'{table.npcs[2].mac}', self.col_4, row_2+20, 12, black),
            TextObject(None, f'{table.npcs[3].mac}', self.col_4, row_3+20, 12, black),
        ]

    def display(self) -> None:

        while True:
            self.populate_menu_options(self.ui_elements + self.info_ui)

            # Display the background dialog window
            self.game_instance.game_window.blit(self.img, (self.x, self.y))

            # Display all selection menu objects in menu_options list.
            self.draw_ui_objects()

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
                        self.game_instance.draw_objects()
                        self.window_running = False
                        return

                if event.type == pygame.MOUSEBUTTONUP:
                    for index, selection in enumerate(self.menu_options):
                        if Joetilities.utilities.get_mouse_collision(mouse_pos, selection):
                            if selection.__class__.__name__ == 'ButtonObject':
                                print(selection.object_id)
                                self.populate_info(selection)

            pygame.display.update()

    def draw_ui_objects(self):
        for index, selection in enumerate(self.menu_options):
            if index == self.selection:
                self.img_sel = pygame.transform.scale(self.img_sel, (selection.w, selection.h))
                self.game_instance.game_window.blit(selection.img, (selection.x, selection.y))
                self.game_instance.game_window.blit(self.img_sel, (selection.x, selection.y))
            else:
                self.game_instance.game_window.blit(selection.img, (selection.x, selection.y))
