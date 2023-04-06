from windows.interactiveWindow import InteractiveWindow
from windows.ui_Object import UIObject
from windows.ui_InteractableObject import UIInteractableObject
from dialog.textObject import TextObject
import pygame
import sys
from pygame.locals import QUIT
import Joetilities.utilities


class ShoulderWindow(InteractiveWindow):

    def __init__(self, student) -> None:
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
            TextObject(None, f'{student.name}', self.col_0 + 150, self.row_0, 36),
            UIInteractableObject(self.x + 40, self.row_0, 100, 120, 'assets/npc_top.png'),
        ]
        self.populate_menu_options(self.ui_objects)

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
                if event.type == pygame.MOUSEBUTTONUP:
                    pass

            pygame.display.update()
