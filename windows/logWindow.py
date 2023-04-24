import random
from dialog.textObject import TextObject
from windows.interactiveWindow import InteractiveWindow
from windows.ui_ButtonObject import ButtonObject
import pygame
import sys
from pygame.locals import QUIT
import Joetilities.utilities
import asyncio
from data.server_data import ip_addresses

"""
This module provides functionality for a game that involves interacting with text-based dialog windows and buttons.

This module imports the following packages and modules:
    - random: Provides functions for generating random numbers and other random operations.
    - TextObject: A class for creating text objects in Pygame.
    - InteractiveWindow: A class for creating interactive windows that can display text and buttons.
    - ButtonObject: A class for creating interactive buttons in Pygame.
    - pygame: Provides functionality for creating games and interactive applications in Python.
    - sys: Provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
    - QUIT: A Pygame event constant for the "quit" event.
    - Joetilities.utilities: A custom module with various utility functions.
    - asyncio: Provides infrastructure for writing single-threaded concurrent code using coroutines, multiplexing I/O access over sockets and other resources, running network clients and servers, and other related primitives.
    - ip_addresses: A list of IP addresses used for the game's server functionality.
"""

black = (50, 50, 50)


class LogWindow(InteractiveWindow):
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
        self.game_instance = game_instance
        self.x = 100
        self.w = 1000
        self.h = 600
        self.img = pygame.image.load('assets/map_window.png')
        self.img = pygame.transform.scale(self.img, (self.w, self.h))

        self.feed_status = True
        self.window_running = True
        self.router_ip = '99.106.62.1'
        self.router_mac = '04:09:58:7d:7b:27'
        self.hacker_ip = self.game_instance.hacker.ip

        self.x_spacing = 200
        self.col_0 = self.x + self.x_spacing - 120
        self.col_1 = self.col_0 + self.x_spacing - 50
        self.col_2 = self.col_1 + self.x_spacing - 50
        self.col_3 = self.col_2 + self.x_spacing - 130

        self.row_0 = self.y + self.h - 50
        self.row_1 = self.y
        self.row_2 = self.row_1
        self.row_3 = self.row_2
        self.row_4 = self.row_3

        self.ui_elements = [
            TextObject(None, f'Source', self.col_0, self.y + 80, 12),
            TextObject(None, f'Destination', self.col_1, self.y + 80, 12),
            TextObject(None, f'Protocol', self.col_2, self.y + 80, 12),
            TextObject(None, f'Info', self.col_3, self.y + 80, 12),
            ButtonObject(self.x + self.w - 190, self.y + 120, 40, 40, 'assets/green.png', object_id='serv_button_START'),
            ButtonObject(self.x + self.w - 140, self.y + 120, 40, 40, 'assets/red.png', object_id='serv_button_STOP'),
        ]
        self.log_text = [
            TextObject(None, f'', self.col_0, self.row_0, 24),
        ]

        # Run both window loops.
        asyncio.run(self.log_screen())

    async def log_screen(self):
        await asyncio.gather(self.start_traffic(), self.display())

    async def display(self) -> None:
        """
        A method of LogWindow that draws the window to the screen.

        @return: None
        """

        # Window Running Loop for the instance.
        # initialize log index at the beginning of the log list.

        while True:
            self.populate_menu_options(self.ui_elements + self.log_text)

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
                        self.feed_status = False
                        return
                if event.type == pygame.MOUSEBUTTONUP:
                    for index, selection in enumerate(self.menu_options):
                        if Joetilities.utilities.get_mouse_collision(mouse_pos, selection):
                            if selection.object_id == 'serv_button_START':
                                if not self.feed_status:
                                    print('pressed start')
                                    while not self.log_text[len(self.log_text) - 1].y == self.row_0:
                                        for text in self.log_text:
                                            text.y -= 25
                                        await asyncio.sleep(0.001)
                                    self.feed_status = True

                            if selection.object_id == 'serv_button_STOP':
                                print('pressed stop')
                                self.feed_status = False

                if event.type == pygame.MOUSEWHEEL:
                    if not self.feed_status:
                        # Mouse Wheel Up
                        if event.y == 1:
                            self.scroll_down()
                        # Mouse Wheel Down
                        if event.y == -1:
                            self.scroll_up()

            pygame.display.update()
            await asyncio.sleep(0.001)

    async def start_traffic(self) -> None:
        """
        Populates the log_text with random traffic and moves the text up.
        @return: None
        """
        h = 25
        # Main loop
        while self.window_running:
            # Inner loop to run the text.
            while self.feed_status:
                traffic_type = self.get_traffic_type()
                for text in self.log_text:
                    text.y -= h
                await asyncio.sleep(0.3)

                match traffic_type:
                    case 'HTTP':
                        await self.get_http_traffic()
                    case 'ARP':
                        self.get_arp_traffic()
                    case 'HACKER':
                        self.get_hacker_arp_traffic()

            await asyncio.sleep(0.3)

    @staticmethod
    def get_traffic_type():
        traffic_types = ['HTTP', 'ARP', 'HACKER']
        random_number = random.randint(0, 6)
        print(random_number)
        match random_number:
            case 1 | 3:
                return traffic_types[1]
            case 2:
                return traffic_types[2]
            case _:
                return traffic_types[0]

    def get_random_ip(self):
        random_table = random.randint(0, len(self.game_instance.tables) - 1)
        random_npc = random.randint(0, 3)
        return self.game_instance.tables[random_table].npcs[random_npc].ip

    def get_random_mac(self):
        random_table = random.randint(0, len(self.game_instance.tables) - 1)
        random_npc = random.randint(0, 3)
        return self.game_instance.tables[random_table].npcs[random_npc].mac

    @staticmethod
    def get_random_destination():
        random_website, random_destination_ip = random.choice(list(ip_addresses.items()))
        return random_destination_ip

    @staticmethod
    def get_random_website():
        random_website, random_destination_ip = random.choice(list(ip_addresses.items()))
        return random_website

    def set_traffic_text(self, source, destination, protocol, website, text_size, background_color):
        self.log_text.append(TextObject(
            game_instance=None,
            string=f'{" "*230}',
            x=self.col_0,
            y=self.row_0,
            size=text_size,
            back_ground_color=background_color,
            color=black

        ))

        self.log_text.append(TextObject(
            game_instance=None,
            string=f'{source}',
            x=self.col_0,
            y=self.row_0,
            size=text_size,
            back_ground_color=background_color,
            color=black

        ))
        # Append the destination IP
        self.log_text.append(TextObject(
            game_instance=None,
            string=f'{destination}',
            x=self.col_1-20,
            y=self.row_0,
            size=text_size,
            back_ground_color=background_color,
            color=black

        ))
        # Append the website url
        self.log_text.append(TextObject(
            game_instance=None,
            string=f'{protocol}',
            x=self.col_2-40,
            y=self.row_0,
            size=text_size,
            back_ground_color=background_color,
            color=black

        ))
        # Append the website url
        self.log_text.append(TextObject(
            game_instance=None,
            string=f'{website}',
            x=self.col_3-60,
            y=self.row_0,
            size=text_size,
            back_ground_color=background_color,
            color=black
        ))

    async def get_http_traffic(self):
        background_color = (51, 214, 103)
        random_source_ip = self.get_random_ip()
        random_destination_ip = self.get_random_destination()
        random_website = self.get_random_website()
        await self.get_dns_query(random_source_ip, random_website)
        await self.get_tcp(random_source_ip, random_destination_ip)
        self.set_traffic_text(random_source_ip, random_destination_ip, 'HTTP', random_website, 12, background_color)

    def get_arp_traffic(self):
        text_size = 12
        background_color = (227, 227, 109)
        random_destination_ip = self.get_random_ip()
        random_destination_mac = self.get_random_mac()
        self.set_traffic_text(self.router_mac, random_destination_mac, 'ARP', f'who has {random_destination_ip}? Tell {self.router_ip}', 12, background_color)

    def get_hacker_arp_traffic(self):
        text_size = 12
        background_color = (227, 227, 109)
        random_destination_ip = self.get_random_ip()
        random_destination_mac = self.get_random_mac()
        self.set_traffic_text(self.router_mac, random_destination_mac, 'ARP', f'who has {random_destination_ip}? Tell {self.hacker_ip}', 12, background_color)

    async def get_dns_query(self, source_ip, website):
        text_size = 12
        background_color = (29, 209, 191)
        hex_code = self.random_hex()
        self.set_traffic_text(source_ip, self.router_ip, 'DNS', f'Standard query 0x{hex_code} {website}', 12, background_color)
        await asyncio.sleep(0.6)
        self.move_text_up()
        await self.get_dns_response(source_ip, website, hex_code)

    async def get_dns_response(self, source_ip, website, hex_code):
        text_size = 12
        background_color = (29, 209, 191)
        self.set_traffic_text(self.router_ip, source_ip, 'DNS', f'Standard query response 0x{hex_code} {website}', 12, background_color)
        self.move_text_up()
        await asyncio.sleep(0.6)

    async def get_tcp(self, source_ip, website_ip):
        text_size = 12
        background_color = (29, 209, 191)
        port = random.randint(40000, 59000)
        self.set_traffic_text(source_ip, website_ip, 'TCP', f'{port} -> {80} [SYN] Seq=0 Win=64240 Len=0', 12, background_color)

        await asyncio.sleep(0.6)
        self.move_text_up()
        await self.get_tcp_ack(source_ip, website_ip, port)

    async def get_tcp_ack(self, source_ip, website_ip, port):
        text_size = 12
        background_color = (29, 209, 191)
        self.set_traffic_text(website_ip, source_ip, 'TCP', f'{80} -> {port} [SYN, ACK] Seq=0 Ack=1 Win=26847 Len=0', 12, background_color)
        self.move_text_up()
        await asyncio.sleep(0.6)

    @staticmethod
    def random_hex():
        # Generate a random integer between 0 and 16^4-1 (which is the maximum 4-digit hexadecimal number)
        random_int = random.randint(0, 16 ** 4 - 1)

        # Convert the integer to a hexadecimal string with 4 characters
        return hex(random_int)[2:].zfill(4)

    def scroll_up(self):
        """
        Scrolls the menu text up by 25 pixels, if possible.

        If the bottom of the last text item in the menu is at the same y-coordinate
        as the top row of the menu (self.row_0), the text items are shifted up by 25 pixels.
        """
        if not self.log_text[len(self.log_text) - 1].y == self.row_0:
            for text in self.log_text:
                text.y -= 25

    def scroll_down(self):
        """
        Scrolls the menu text down by 25 pixels, if possible.

        If the top of the first text item in the menu is at the same y-coordinate
        as the bottom row of the menu plus 65 pixels (self.y + 65), the text items
        are shifted down by 25 pixels.
        """
        if not self.log_text[0].y >= self.y + 65:
            for text in self.log_text:
                text.y += 25

    def draw_ui_objects(self):
        """
        Draws the menu options and selection indicator on the game window.

        The menu options are drawn using their x and y coordinates, and their images.
        If a menu option is currently selected, a selection indicator image is drawn
        on top of the option's image. The menu options that are visible within the
        menu's boundaries (between self.row_0 and self.y + 80) are drawn.

        Args:
        - game_instance: An instance of the game, used to access the game window.
        """
        for index, selection in enumerate(self.menu_options):
            if self.y + 120 <= selection.y <= self.row_0 - 70:
                if index == self.selection:
                    self.img_sel = pygame.transform.scale(self.img_sel, (selection.w, selection.h))
                    self.game_instance.game_window.blit(selection.img, (selection.x, selection.y))
                    self.game_instance.game_window.blit(self.img_sel, (selection.x, selection.y))
                else:
                    self.game_instance.game_window.blit(selection.img, (selection.x, selection.y))

    def move_text_up(self) -> None:
        """
            Moves the text objects in the self.log_text list vertically upward by a fixed amount.
        """
        # Set a fixed amount of distance to move each text object vertically
        h = 25

        # Iterate through each text object in the list
        for text in self.log_text:
            # Move the text object upward by subtracting the fixed amount from its 'y' attribute
            text.y -= h