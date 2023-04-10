from windows.ShoulderWindow import ShoulderWindow
from windows.interactiveWindow import InteractiveWindow
from windows.ui_Object import UIObject
from windows.ui_InteractableObject import UIInteractableObject
from dialog.textObject import TextObject
import pygame
import sys
from pygame.locals import QUIT
import Joetilities.utilities
import random


class TableWindow(InteractiveWindow):

    def __init__(self, table) -> None:
        super().__init__()
        self.col_0 = self.x + 45
        self.col_1 = self.x + 45 * 4
        self.col_2 = self.x + 45 * 7
        self.col_3 = self.x + 45 * 10

        self.row_0 = self.y + 80
        self.row_1 = self.y + 40 * 5
        self.row_2 = self.row_1 + 40 * 4
        self.row_3 = self.row_2 + 40
        self.row_4 = self.row_3 + 40

        self.ui_objects = [
            # Title
            TextObject(None, 'Select A Student', self.col_0 + 100, self.row_0, 36),
            # Player cards
            UIInteractableObject(self.col_0, self.row_1, 100, 120, 'assets/npc_top.png'),
            UIInteractableObject(self.col_1, self.row_1, 100, 120, 'assets/npc_top.png'),
            UIInteractableObject(self.col_2, self.row_1, 100, 120, 'assets/npc_top.png'),
            UIInteractableObject(self.col_3, self.row_1, 100, 120, 'assets/npc_top.png'),
            # Names
            TextObject(None, f'Name: {table.npc_top.name}', self.col_0, self.row_2),
            TextObject(None, f'Name: {table.npc_right.name}', self.col_1, self.row_2),
            TextObject(None, f'Name: {table.npc_bottom.name}', self.col_2, self.row_2),
            TextObject(None, f'Name: {table.npc_left.name}', self.col_3, self.row_2),
            #  IP
            TextObject(None, f'IP: {table.npc_top.ip}', self.col_0, self.row_3),
            TextObject(None, f'IP: {table.npc_right.ip}', self.col_1, self.row_3),
            TextObject(None, f'IP: {table.npc_bottom.ip}', self.col_2, self.row_3),
            TextObject(None, f'IP: {table.npc_left.ip}', self.col_3, self.row_3),
            # MAC
            TextObject(None, f'MAC: {table.npc_top.mac}', self.col_0, self.row_4, 10),
            TextObject(None, f'MAC: {table.npc_right.mac}', self.col_1, self.row_4, 10),
            TextObject(None, f'MAC: {table.npc_bottom.mac}', self.col_2, self.row_4, 10),
            TextObject(None, f'MAC: {table.npc_left.mac}', self.col_3, self.row_4, 10),
        ]
        self.populate_menu_options(self.ui_objects)

    def display(self, game_instance, table):
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
                        return
                if event.type == pygame.MOUSEBUTTONUP:
                    for index, selection in enumerate(self.menu_options):
                        if Joetilities.utilities.get_mouse_collision(mouse_pos, selection):
                            detected = random.randint(0, 1)
                            ShoulderWindow(table.npcs[index - 1], detected).display(game_instance,
                                                                                    table.npcs[index - 1])

            pygame.display.update()
