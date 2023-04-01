import pygame, sys
from pygame.locals import QUIT
from gameObject import GameObject
from player import Player
from table import Table
from gamebar import GameBar
import random

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)


class GameInstance:

    def __init__(self):
        pygame.init()
        self.WIDTH = 1200
        self.HEIGHT = 1000
        self.game_window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Lab Hunt')

        self.tick_rate = 120

        self.clock = pygame.time.Clock()

        self.background = GameObject(0, 0, self.WIDTH, self.HEIGHT,
                                     'assets/carpet.png')
        self.player = Player(400, 400, 64, 64, 'assets/green.png')

        self.player_direction_y = 0
        self.player_direction_x = 0

        self.menu = GameBar(0, 0, self.WIDTH, 32, 'assets/gamebar.png')

        self.table0 = Table(100, 500, 160, 160, 'assets/table_red.png', '0')
        self.table1 = Table(100, 100, 160, 160, 'assets/table_blue.png', '1')
        self.table2 = Table(800, 750, 160, 160, 'assets/table_blue.png', '2')
        self.table3 = Table(400, 750, 160, 160, 'assets/table_red.png', '3')
        self.table4 = Table(500, 350, 160, 160, 'assets/table_blue.png', '4')
        self.table5 = Table(800, 100, 160, 160, 'assets/table_red.png', '5')

        self.tables = [
            self.table0,
            self.table1,
            self.table2,
            self.table3,
            self.table4,
            self.table5,
        ]

        self.set_hacker(self.tables)

        self.objects = [
            self.tables,
        ]

    def set_hacker(self, table_list):
        infected_table = random.randint(0, 5)
        print(infected_table)
        table_list[infected_table].infected = True
        table_list[infected_table].render()

    def detected_collision(self, object1, object2):
        if (object1.x + object1.w) < object2.x:
            return False
        elif object1.x > (object2.x + object2.w):
            return False

        if object1.y > (object2.y + object2.h):
            return False
        elif (object1.y + object1.h) < object2.y:
            return False
        return True

    def draw_objects(self):

        # Draw Carpet
        self.game_window.blit(self.background.img,
                              (self.background.x, self.background.y))

        # Draw Menu Bar
        self.game_window.blit(self.menu.img, (self.menu.x, self.menu.y))
        self.game_window.blit(self.menu.text, self.menu.textRect)

        for table in self.tables:
            for seat in table.npcs:
                seat.check_infected()

        for object_list in self.objects:
            for object in object_list:
                self.game_window.blit(object.img, (object.x, object.y))

        for i, j in self.player.imgs:
            self.game_window.blit(i, j)

        for table in self.tables:
            self.game_window.blit(table.img, (table.x, table.y))
            self.game_window.blit(table.text, table.textRect)
            for npc in table.npcs:
                self.game_window.blit(npc.img, (npc.x, npc.y))

        pygame.display.update()

    def game_loop(self):
        while True:
            self.draw_objects()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    # Y
                    if event.key == pygame.K_UP:
                        self.player_direction_y = -1
                    elif event.key == pygame.K_DOWN:
                        self.player_direction_y = 1
                # X
                    elif event.key == pygame.K_LEFT:
                        self.player_direction_x = -1
                    elif event.key == pygame.K_RIGHT:
                        self.player_direction_x = 1

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.player_direction_y = 0
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.player_direction_x = 0
            self.player.move_x(self.player_direction_x, self.WIDTH,
                               self.objects)
            self.player.move_y(self.player_direction_y, self.HEIGHT,
                               self.objects)
            self.clock.tick(self.tick_rate)
