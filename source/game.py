# Import Pygame and System Utilities
import pygame
import sys
from pygame.locals import QUIT
import os
# Import NPC Data
from source.data.npc_data import npc_data
from source.dialog.textObject import TextObject

# Import Game Objects
from source.gameObjects.gameObject import GameObject
from source.gameObjects.player import Player
from source.gameObjects.table import Table
from source.gameObjects.server import Server

# Import Dialog Window and related items
from source.dialog.splashDialog import SplashDialog
from source.windows.serverWindow import ServerWindow

# Import Interactive Windows
from source.windows.tableWindow import TableWindow

# Misc imports
import random

# Global Variables for color usage
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

# Shuffle the npc data to randomize name assignments.
random.shuffle(npc_data['names'])


class GameInstance:
    """
        Class representing a single instance of the game.

        Attributes:
            WIDTH (int): Width of the game window.
            HEIGHT (int): Height of the game window.
            game_window (pygame.Surface): Pygame Surface representing the game window.
            clock (pygame.time.Clock): Pygame Clock object for controlling game timing.
            tick_rate (int): Number of ticks per second for the game.
            dialog_running (bool): Flag indicating whether a dialog window is currently open.
            attempts (int): The number of attempts the player has to complete the game.
            interaction_running (bool): Flag indicating whether an interaction window is currently open.
            npc_data (List[Dict]): List of dictionaries representing non-player characters in the game.
            animation_tick (int): The number of ticks that have elapsed since the last animation frame was displayed.
            animation_frame (int): The current frame number of the animation being displayed.
            background (GameObject): Game object representing the background image.
            infected_table (Table): Game object representing the infected table.
            hacker (Chair): Game object representing the hacker.
            tv_left (GameObject): Game object representing the left TV.
            tv_right (GameObject): Game object representing the right TV.
            player (Player): Game object representing the player.
            player_direction_y (int): Direction in which the player is moving vertically.
            player_direction_x (int): Direction in which the player is moving horizontally.
            table0 - table5 (Table): Game objects representing the six tables in the game.
            tables (List[Table]): List of all table objects in the game.
            server (Server): Game object representing the server in the game.
            objects (List[List[GameObject]]): List of all game objects in the game, organized by type.

        Methods:
            game_loop(): The main game loop, controlling the flow of the game.
            draw_objects(): Draws all game objects to the game window.
            set_hacker(tables: List[Table]) -> None: Selects a random table and chair in the game and assigns the hacker to it.
            update_animation_frame(): Updates the animation frame number for the game objects.
        """

    def __init__(self) -> None:

        # Initial PyGame Window Setup
        pygame.init()
        # Initialize Window Dimensions
        self.WIDTH = 1200
        self.HEIGHT = 900
        # Create Game Window and Set Dimensions
        self.game_window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        # Set Game Windows Name
        pygame.display.set_caption('Lab Hunt')
        # Initialize the FPS Clock
        self.clock = pygame.time.Clock()
        # Initialize Tick Rate for Refresh
        self.tick_rate = 120
        # Initialize the dialog_running state. (Off by Default)
        self.dialog_running = False
        # Initialize the default attempt amount.
        self.attempts = 3
        # Initialize the interaction_running state. (Off by Default)
        self.interaction_running = False
        # Initialize data
        self.npc_data = npc_data
        self.animation_tick = 0
        self.animation_frame = 0
        # Establish Game Objects
        # Initialize the background image
        self.background = GameObject(0, 0, self.WIDTH, self.HEIGHT, 'source/assets/carpet.png')
        self.infected_table = None
        self.hacker = None
        # Initialize TVs
        self.tv_left = GameObject(41, 48, 241, 128, 'source/assets/red.png')
        self.tv_right = GameObject(self.WIDTH - 241 - 41, 48, 242, 128, 'source/assets/red.png')
        # Initialize Player                           
        self.player = Player(400, 400, 50, 64, 'source/assets/admin_top.png')
        self.player_direction_y = 0
        self.player_direction_x = 0

        # Initialize all table objects.
        self.table0 = Table(100, 530, 160, 160, 'source/assets/table_red.png', '0', self.npc_data)
        self.table1 = Table(100, 270, 160, 160, 'source/assets/table_blue.png', '1', self.npc_data)
        self.table2 = Table(850, 670, 160, 160, 'source/assets/table_blue.png', '2', self.npc_data)
        self.table3 = Table(450, 670, 160, 160, 'source/assets/table_red.png', '3', self.npc_data)
        self.table4 = Table(550, 400, 160, 160, 'source/assets/table_blue.png', '4', self.npc_data)
        self.table5 = Table(850, 250, 160, 160, 'source/assets/table_red.png', '5', self.npc_data)

        # Initialize and populate table list
        self.tables = [
            self.table0,
            self.table1,
            self.table2,
            self.table3,
            self.table4,
            self.table5,
        ]

        # Populate a random chair in a random table with the hacker.
        self.set_hacker(self.tables)

        # Initialize the Server Object
        self.server = Server(1000, 480, 120, 160, 'source/assets/server.png')

        # Initialize and populate the objects list of lists.
        self.objects = [
            self.tables,
            [self.server],
        ]

    def game_loop(self) -> None:

        self.draw_objects()

        # Display the splash screen to the player.
        SplashDialog(self, 'Welcome to lab Hunt!')

        while True:

            # Draw the objects to the screen.
            self.draw_objects()

            # Listen for events
            for event in pygame.event.get():

                # Event Listener for Closing Window
                if event.type == QUIT:
                    # Quit the game if event fired.
                    pygame.quit()
                    sys.exit()

                # Event Listener for key press
                if event.type == pygame.KEYDOWN:

                    # Listen for 'W' Key
                    if event.key == pygame.K_w:
                        # Subtract from players 'y' value to render upward movement.
                        self.player_direction_y = -1
                        # Load appropriate sprite
                        img = pygame.image.load('source/assets/admin_bottom.png').convert_alpha()
                        self.player.img = pygame.transform.scale(img, (self.player.w, self.player.h))

                    # Listen for 'S' Key
                    elif event.key == pygame.K_s:
                        # Add to players 'y' value to render downward movement.
                        self.player_direction_y = 1
                        # Load appropriate sprite
                        img = pygame.image.load('source/assets/admin_top.png').convert_alpha()
                        self.player.img = pygame.transform.scale(img, (self.player.w, self.player.h))

                    # Listen for 'A' Key
                    elif event.key == pygame.K_a:
                        self.player_direction_x = -1
                        # Load appropriate sprite
                        img = pygame.image.load('source/assets/admin_right.png').convert_alpha()
                        self.player.img = pygame.transform.scale(img, (self.player.w, self.player.h))

                    # Listen for 'D' Key
                    elif event.key == pygame.K_d:
                        self.player_direction_x = 1
                        # Load appropriate sprite
                        img = pygame.image.load('source/assets/admin_left.png').convert_alpha()
                        self.player.img = pygame.transform.scale(img, (self.player.w, self.player.h))

                    # Listen for 'E' Key
                    elif event.key == pygame.K_e and self.player.can_interact:
                        # Check type of object selected
                        if self.player.adjacent_object.__class__.__name__ == 'Table':
                            # Render the Table Window is table is selected.
                            TableWindow(self.player.adjacent_object).display(self, self.player.adjacent_object)
                        if self.player.adjacent_object.__class__.__name__ == 'Server':
                            # Render the Server Window is table is selected.
                            ServerWindow(self)

                # Event Listener for released keys.
                if event.type == pygame.KEYUP:
                    # Listen for release of 'W' or 'S'
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        # Stop the players vertical movement
                        self.player_direction_y = 0
                    # Listen for release of 'A' or 'D'
                    elif event.key == pygame.K_a or event.key == pygame.K_d:
                        # Stop the players horizontal movement
                        self.player_direction_x = 0

            # End Event Listeners

            # Handle Player Movement.
            # Each movement function takes in 3 parameters:
            # - Direction: Which direction the character is currently moving based on.
            # - Max Width/Max Height: Supplies the boundaries for the window to contain the player's movement.
            # - Objects: Provides a list of lists which contain all collide-able objects.
            self.player.move_x(self.player_direction_x, self.WIDTH, self.objects)
            self.player.move_y(self.player_direction_y, self.HEIGHT, self.objects)

            self.animation_tick += 1
            if self.animation_tick > 10:
                self.animation_tick = 0
                self.animation_frame += 1
            self.clock.tick(self.tick_rate)

    def draw_objects(self) -> None:

        # Draw Carpet
        self.game_window.blit(self.background.img, (self.background.x, self.background.y))

        TextObject(self, f'Attempts Left: {self.attempts}', 10, 10, size=16, color=(255, 0, 0))

        # Draw and animate tvs
        folder_path = 'source/assets/tv_left'
        folder_contents = os.listdir(folder_path)
        if self.animation_frame > len(folder_contents) - 1:
            self.animation_frame = 0

        tv_full_path = folder_path + '/' + folder_contents[self.animation_frame]

        # Load the left TV image and scale.
        self.tv_left.img = pygame.image.load(tv_full_path)
        self.tv_left.img = pygame.transform.scale(self.tv_left.img, (self.tv_left.w, self.tv_left.h))

        # Load the right TV image and scale.
        self.tv_right.img = pygame.image.load(tv_full_path)
        self.tv_right.img = pygame.transform.scale(self.tv_right.img, (self.tv_right.w, self.tv_right.h))

        # Blit both tv's to screen.
        self.game_window.blit(self.tv_left.img, (self.tv_left.x, self.tv_left.y))
        self.game_window.blit(self.tv_right.img, (self.tv_right.x, self.tv_right.y))

        # Draw Object List
        for object_list in self.objects:
            for game_object in object_list:
                self.game_window.blit(game_object.img, (game_object.x, game_object.y))

        # Draw Table List
        for table in self.tables:
            self.game_window.blit(table.img, (table.x, table.y))
            for npc in table.npcs:
                self.game_window.blit(npc.img, (npc.x, npc.y))

        # Draw Player
        for i, j in self.player.imgs:
            self.game_window.blit(i, j)

        # Update game display
        pygame.display.update()

    def set_hacker(self, table_list: list[Table]) -> None:

        # Choose a table at random
        infected_table = random.randint(0, 5)
        # Set the table as infected
        table_list[infected_table].infected = True
        # Re-Render the table to update its sprite.
        table_list[infected_table].render()

        self.infected_table = table_list[infected_table]
        self.hacker = self.infected_table.get_hacker()
