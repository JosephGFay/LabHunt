import random

from dialog.textObject import TextObject
from windows.interactiveWindow import InteractiveWindow
import pygame
import sys
from pygame.locals import QUIT
import Joetilities.utilities
import asyncio
from data.server_data import ip_addresses

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

        self.x_spacing = 200
        self.col_0 = self.x + self.x_spacing - 100
        self.col_1 = self.col_0 + self.x_spacing
        self.col_2 = self.col_1 + self.x_spacing
        self.col_3 = self.col_2 + self.x_spacing

        self.row_0 = self.y + self.h - 50
        self.row_1 = self.y
        self.row_2 = self.row_1
        self.row_3 = self.row_2
        self.row_4 = self.row_3

        self.ui_elements = [
            TextObject(None, f'Source', self.col_0, self.y + 80, 12),
            TextObject(None, f'Destination', self.col_1, self.y + 80, 12),
            TextObject(None, f'URL', self.col_2, self.y + 80, 12),
        ]
        self.log_text = [
            TextObject(None, f'Starting Terminal Session...', self.col_0, self.row_0, 24),
        ]

        # Run both window loops.
        asyncio.run(self.log_screen(game_instance))

    async def log_screen(self, game_instance):
        await asyncio.gather(self.start_traffic(game_instance), self.display(game_instance))

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
                if selection.y >= self.y + 80:
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

    async def start_traffic(self, game_instance) -> None:
        """
        Populates the log_text with random traffic and moves the text up.
        @param game_instance:
        @return: None
        """
        i = 0
        h = 25
        while self.status:
            log_index = self.log_text[i]
            for text in self.log_text:
                text.y -= h
            await asyncio.sleep(0.3)
            random_table = random.randint(0, len(game_instance.tables)-1)
            random_npc = random.randint(0, 3)
            random_source_ip = game_instance.tables[random_table].npcs[random_npc].ip
            random_website, random_destination_ip = random.choice(list(ip_addresses.items()))
            random_mac = game_instance.tables[random_table].npcs[random_npc].mac

            # Append the source IP
            self.log_text.append(TextObject(
                game_instance=None,
                string=f'{random_source_ip}',
                x=self.col_0,
                y=self.row_0,
                size=18))

            # Append the destination IP
            self.log_text.append(TextObject(
                game_instance=None,
                string=f'{random_destination_ip}',
                x=self.col_1,
                y=self.row_0,
                size=18))

            # Append the website url
            self.log_text.append(TextObject(
                game_instance=None,
                string=f'{random_website}',
                x=self.col_2,
                y=self.row_0,
                size=18))

            i += 1
