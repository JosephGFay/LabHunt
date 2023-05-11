import sys
import time

import pygame

from source.dialog.textObject import TextObject
from source.windows.interactiveWindow import InteractiveWindow


class EndWindow(InteractiveWindow):

    def __init__(self, game_instance, text):
        super().__init__()
        self.text = text
        self.x = 100
        self.w = 1000
        self.h = 600
        self.img = pygame.image.load('source/assets/dialog_window.png')
        self.img = pygame.transform.scale(self.img, (self.w, self.h))
        self.window_running = True
        self.x_spacing = 200
        self.col_0 = int((self.x + self.w) / 2) - 30
        self.col_1 = self.col_0 + self.x_spacing
        self.col_2 = self.col_1 + self.x_spacing
        self.col_3 = self.col_2 + self.x_spacing

        self.row_0 = int((self.y + self.h)/2)
        self.row_1 = self.row_0 + 80
        self.row_2 = self.row_1 + 80
        self.row_3 = self.row_2 + 80
        self.row_4 = self.row_3 + 80

        self.ui_elements = [
            TextObject(None, f'{self.text}', self.col_0, self.row_0, 36),
        ]

        # Run both window loops.
        self.display(game_instance)

    def display(self, game_instance) -> None:

        while True:
            self.populate_menu_options(self.ui_elements)

            # Display the background dialog window
            game_instance.game_window.blit(self.img, (self.x, self.y))

            # Display all selection menu objects in menu_options list.
            self.draw_ui_objects(game_instance)

            # Event Listener
            for event in pygame.event.get():
                # Listen for KEY events
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_instance.draw_objects()
                        self.window_running = False
                        return

            pygame.display.update()

            if self.text == 'You Lose':
                time.sleep(1)
                pygame.quit()
                sys.exit()

    def draw_ui_objects(self, game_instance):
        for index, selection in enumerate(self.menu_options):
            if index == self.selection:
                self.img_sel = pygame.transform.scale(self.img_sel, (selection.w, selection.h))
                game_instance.game_window.blit(selection.img, (selection.x, selection.y))
                game_instance.game_window.blit(self.img_sel, (selection.x, selection.y))
            else:
                game_instance.game_window.blit(selection.img, (selection.x, selection.y))
