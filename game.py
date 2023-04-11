# Import Pygame and System Utilities
import pygame
import sys
from pygame.locals import QUIT
import os
# Import NPC Data
from data.npc_data import npc_data

# Import Game Objects
from gameObjects.gameObject import GameObject
from gameObjects.player import Player
from gameObjects.table import Table
from gameObjects.server import Server

# Import Tool Bar and related Items.
from toolbar.toolbar import ToolBar

# Import Dialog Window and related items
from dialog.splashDialog import SplashDialog
from windows.serverWindow import ServerWindow

# Import Interactive Windows
from windows.tableWindow import TableWindow

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
    Game instance class created to house the main functionality of the game.

    Attributes
    -----------
    WIDTH : int
        Variable for the window width.
    HEIGHT : int
        Variable for the window height.
    game_window : Surface
        The main game window.
    clock : Clock
        mirrors the pygame clock.
    tick_rate : int
        Handles the FPS for the clock.
    dialog_running : bool
        Checks if there is an active dialog window running
    interaction_running : bool
        Checks if there is n active interaction running.
    npc_data : dict
        Holds the data for the npcs
    background : GameObject
        Sets the background to a gameObject class that is same size as window.
    player : Player
        Stores the player data and methods
    player_direction_x : int.
        Sets direction on the horizontal axis
    player_direction y: int
        sets direction on the vertical axis.
    table0-table5: Table
        Initialize tables within the game instance.
    tables: list[Table]
        A collection of the game tables.
    server: GameObject
        The games Network Server object.
    objects: list[[objects]]
        Nested list of objects used for rendering.

    Methods
    ----------
    # TODO Add more documentation for GameInstance methods
    game_loop
    draw_objects
    set_hacker
    """

    def __init__(self) -> None:
        """
        Constructs the game instance object.

        """
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
        # Initialize the interaction_running state. (Off by Default)
        self.interaction_running = False
        # Initialize data
        self.npc_data = npc_data
        self.animation_tick = 0
        self.animation_frame = 0
        # Establish Game Objects
        # Initialize the background image
        self.background = GameObject(0, 0, self.WIDTH, self.HEIGHT, 'assets/carpet.png')

        # Initialize TVs
        self.tv_left = GameObject(41, 48, 241, 128, 'assets/red.png')
        self.tv_right = GameObject(self.WIDTH - 241-41, 48, 242, 128, 'assets/red.png')
        # Initialize Player                           
        self.player = Player(400, 400, 50, 64, 'assets/admin_top.png')
        self.player_direction_y = 0
        self.player_direction_x = 0

        # Initialize Toolbar
        self.menu = ToolBar(0, 0, self.WIDTH, 32, 'assets/gamebar.png')

        # Initialize all table objects.
        self.table0 = Table(100, 530, 160, 160, 'assets/table_red.png', '0', self.npc_data)
        self.table1 = Table(100, 270, 160, 160, 'assets/table_blue.png', '1', self.npc_data)
        self.table2 = Table(850, 670, 160, 160, 'assets/table_blue.png', '2', self.npc_data)
        self.table3 = Table(450, 670, 160, 160, 'assets/table_red.png', '3', self.npc_data)
        self.table4 = Table(550, 400, 160, 160, 'assets/table_blue.png', '4', self.npc_data)
        self.table5 = Table(850, 250, 160, 160, 'assets/table_red.png', '5', self.npc_data)
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
        self.server = Server(1000, 480, 120, 160, 'assets/server.png')

        # Initialize and populate the objects list of lists.
        self.objects = [
            self.tables,
            [self.server],
        ]

    def game_loop(self) -> None:
        """
        GameInstance method that handles running the main game loop.

        @return: None
        """
        # Initial draw of game objects

        self.draw_objects()
        # Display the splash screen to the player.
        SplashDialog(self, 'Welcome to lab Hunt!')
        while True:
            # Update the screen.
            # if animation_frame > 60:
            #     animation_frame = 40
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
                        img = pygame.image.load('assets/admin_bottom.png').convert_alpha()
                        self.player.img = pygame.transform.scale(img, (self.player.w, self.player.h))

                    # Listen for 'S' Key
                    elif event.key == pygame.K_s:
                        # Add to players 'y' value to render downward movement.
                        self.player_direction_y = 1
                        # Load appropriate sprite
                        img = pygame.image.load('assets/admin_top.png').convert_alpha()
                        self.player.img = pygame.transform.scale(img, (self.player.w, self.player.h))

                    # Listen for 'A' Key
                    elif event.key == pygame.K_a:
                        self.player_direction_x = -1
                        # Load appropriate sprite
                        img = pygame.image.load('assets/admin_right.png').convert_alpha()
                        self.player.img = pygame.transform.scale(img, (self.player.w, self.player.h))

                    # Listen for 'D' Key
                    elif event.key == pygame.K_d:
                        self.player_direction_x = 1
                        # Load appropriate sprite
                        img = pygame.image.load('assets/admin_left.png').convert_alpha()
                        self.player.img = pygame.transform.scale(img, (self.player.w, self.player.h))

                    # Listen for 'E' Key
                    elif event.key == pygame.K_e and self.player.can_interact:
                        # Check type of object selected
                        if self.player.adjacent_object.__class__.__name__ == 'Table':
                            # Render the Table Window is table is selected.
                            TableWindow(self.player.adjacent_object).display(self, self.player.adjacent_object)
                        if self.player.adjacent_object.__class__.__name__ == 'Server':
                            # Render the Table Window is table is selected.
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
            # Each movement function takes in 3 parameters.
            # Direction - Which direction the character is currently moving based on key press.
            # Max Width/Max Height - Supplies the boundaries for the window to contain player.
            # Objects - Provides a list of lists which contain all collide-able objects.
            self.player.move_x(self.player_direction_x, self.WIDTH, self.objects)
            self.player.move_y(self.player_direction_y, self.HEIGHT, self.objects)

            self.animation_tick += 1
            if self.animation_tick > 40:
                self.animation_tick = 0
                self.animation_frame += 1
            self.clock.tick(self.tick_rate)

    def draw_objects(self) -> None:
        """
        Function to draw all objects on the screen.

        @return: None
        """

        # Draw Carpet
        self.game_window.blit(self.background.img, (self.background.x, self.background.y))

        # Draw and animate tvs
        folder_path = 'assets/tv_left'
        folder_contents = os.listdir(folder_path)
        if self.animation_frame > len(folder_contents)-1:
            self.animation_frame = 0

        self.tv_left.img = pygame.image.load(folder_path + '/' + folder_contents[self.animation_frame])

        self.tv_left.img = pygame.transform.scale(self.tv_left.img, (self.tv_left.w, self.tv_left.h))

        self.tv_right.img = pygame.image.load(folder_path + '/' + folder_contents[self.animation_frame])

        self.tv_right.img = pygame.transform.scale(self.tv_right.img, (self.tv_right.w, self.tv_right.h))

        self.game_window.blit(self.tv_left.img, (self.tv_left.x, self.tv_left.y))
        self.game_window.blit(self.tv_right.img, (self.tv_right.x, self.tv_right.y))

        # Draw Menu Bar
        self.game_window.blit(self.menu.img, (self.menu.x, self.menu.y))
        self.game_window.blit(self.menu.text, self.menu.textRect)
        # Set an infected NPC
        for table in self.tables:
            for seat in table.npcs:
                seat.check_infected()
        # Draw Object List
        for object_list in self.objects:
            for game_object in object_list:
                self.game_window.blit(game_object.img, (game_object.x, game_object.y))

        # Draw Table List
        for table in self.tables:
            self.game_window.blit(table.img, (table.x, table.y))
            self.game_window.blit(table.text, table.textRect)
            for npc in table.npcs:
                self.game_window.blit(npc.img, (npc.x, npc.y))

        # Draw Player
        for i, j in self.player.imgs:
            self.game_window.blit(i, j)

        # Update game display
        pygame.display.update()

    @staticmethod
    def set_hacker(table_list: list[Table]) -> None:
        """
        Populates the game tables with a randomized hacker.

        @param table_list: list[Table]
        @return: None
        """

        # Choose a table at random
        infected_table = random.randint(0, 5)
        # Set the table as infected
        table_list[infected_table].infected = True
        # Re-Render the table to update its sprite.
        table_list[infected_table].render()
