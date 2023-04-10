from dialog.textObject import TextObject
from windows.interactiveWindow import InteractiveWindow
import pygame
import sys
from pygame.locals import QUIT
import Joetilities.utilities
import time
import asyncio


class ServerWindow(InteractiveWindow):
    """
        Class for creating the interface for the games server object.

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
        ui_elements: list[ui_Object]
            A list of ui objects that will be drawn to the screen using populate_menu_options()

    Methods
    ----------
    display:
    # TODO Add documentation for methods.
    """

    def __init__(self, game_instance):
        super().__init__()
        self.x = 100
        self.w = 1000
        self.h = 600
        self.img = pygame.image.load('assets/dialog_window.png')
        self.img = pygame.transform.scale(self.img, (self.w, self.h))
        self.status = True

        self.col_0 = self.x
        self.col_1 = self.x
        self.col_2 = self.x
        self.col_3 = self.x

        self.row_0 = self.y + self.h - 60
        self.row_1 = self.y
        self.row_2 = self.row_1
        self.row_3 = self.row_2
        self.row_4 = self.row_3

        self.ui_elements = [
        ]
        self.log_text = [
            TextObject(None, f'Starting Terminal Session...', self.col_0 + 150, self.row_0, 12),
        ]

        # Run both window loops.
        asyncio.run(self.log_screen(game_instance))

    async def log_screen(self, game_instance):
        await asyncio.gather(self.move_log_text_up(), self.display(game_instance))

    async def display(self, game_instance) -> None:
        """
        A method of ServerWindow that draws the window to the screen.

        @param game_instance: GameInstance
        @return: None
        """

        # Window Running Loop for the instance.
        # initialize log index at the beginning of the log list.

        while True:
            self.populate_menu_options(self.ui_elements + self.log_text)

            # Display the background dialog window
            game_instance.game_window.blit(self.img, (self.x, self.y))

            # Display all selection menu objects in menu_options list.
            for index, selection in enumerate(self.menu_options):
                if selection.y >= self.y + 40:
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
                        self.status = False
                        return
                if event.type == pygame.MOUSEBUTTONUP:
                    pass

            pygame.display.update()
            await asyncio.sleep(0.2)

    async def move_log_text_up(self):
        h = 15
        log_index = self.log_text[0]
        while self.status:
            await asyncio.sleep(1)
            log_index.y -= h
            self.log_text.append(TextObject(None, 'Hello World Added', log_index.x, log_index.y+h, 12))
