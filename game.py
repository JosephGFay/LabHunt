# Import Pygame and System Utilities
import pygame, sys
from pygame.locals import QUIT

# Import Game Objects
from gameObjects.gameObject import GameObject
from gameObjects.player import Player
from gameObjects.table import Table
from gameObjects.server import Server

# Import Tool Bar and related Items.
from toolbar.toolbar import ToolBar

# Import Dialog Window and related items
from dialog.interactionDialog import InteractionDialog
from dialog.splashDialog import SplashDialog
import random

# Global Variables for color usage
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

class GameInstance:
    def __init__(self):
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
        
        # Establish Game Objects
        # Initialize the background image
        self.background = GameObject(0, 0, self.WIDTH, self.HEIGHT,'assets/carpet.png')
        
        # Initialize Player                           
        self.player = Player(400, 400, 50, 64, 'assets/admin_top.png')
        self.player_direction_y = 0
        self.player_direction_x = 0
        
        # Initialize Toolbar
        self.menu = ToolBar(0, 0, self.WIDTH, 32, 'assets/gamebar.png')

        # Initialize all table objects.
        self.table0 = Table(100, 530, 160, 160, 'assets/table_red.png', '0')
        self.table1 = Table(100, 270, 160, 160, 'assets/table_blue.png', '1')
        self.table2 = Table(900, 670, 160, 160, 'assets/table_blue.png', '2')
        self.table3 = Table(450, 670, 160, 160, 'assets/table_red.png', '3')
        self.table4 = Table(550, 400, 160, 160, 'assets/table_blue.png', '4')
        self.table5 = Table(900, 250, 160, 160, 'assets/table_red.png', '5')

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
        self.server = Server(550, 300, 160, 160, 'assets/red.png')

        # Initialize and populate the objects list of lists.
        self.objects = [
          self.tables,
          [self.server],
        ]

    def game_loop(self):
        # Initial draw of game objects
        self.draw_objects()
        # Display the splash screen to the player.
        SplashDialog(self,'Welcome to lab Hunt!')
        while True:
            # Update the screen.
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
                        InteractionDialog(self, 'INTERACTING')

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
            
            # End Event Listners

            # Handle Player Movement.
            # Each movement function takes in 3 parameters.
            # Direction - Which direction the character is currently moving based on key press.
            # Max Width/Max Height - Supplies the boundaries for the window to contain player.
            # Objects - Provides a list of lists which contain all collideable objects.
            self.player.move_x(self.player_direction_x, self.WIDTH, self.objects)
            self.player.move_y(self.player_direction_y, self.HEIGHT, self.objects)
                               
            self.clock.tick(self.tick_rate)

    def draw_objects(self):
        # Function the draw all objects on the screen.
        
        # Draw Carpet
        self.game_window.blit(self.background.img,
                              (self.background.x, self.background.y))

        # Draw Menu Bar
        self.game_window.blit(self.menu.img, (self.menu.x, self.menu.y))
        self.game_window.blit(self.menu.text, self.menu.textRect)
        # Set an infected NPC
        for table in self.tables:
            for seat in table.npcs:
                seat.check_infected()
        # Draw Object List
        for object_list in self.objects:
            for object in object_list:
                self.game_window.blit(object.img, (object.x, object.y))
        
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

    def set_hacker(self, table_list):
        # Function to establish a hacker within a table list.
        # Choose a table at random
        infected_table = random.randint(0, 5)
        # Set the table as infected
        table_list[infected_table].infected = True
        # Re-Render the table to update its sprite.
        table_list[infected_table].render()
