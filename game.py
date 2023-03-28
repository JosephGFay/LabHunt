import pygame, sys
from pygame.locals import QUIT
from gameObject import GameObject
from player import Player
from hacker import Hacker

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)


class GameInstance:

  def __init__(self):
      pygame.init()
      self.WIDTH = 800
      self.HEIGHT = 800
      self.game_window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
      pygame.display.set_caption('Lab Hunt')

      self.tick_rate = 60

      self.clock = pygame.time.Clock()

      self.background = GameObject(0, 0, self.WIDTH, self.HEIGHT,
                                   'assets/Lab proto.png')
      self.player = Player(400, 400, 64, 64, 'assets/Admin.png')

      self.player_direction_y = 0
      self.player_direction_x = 0

      self.hacker = Hacker(200,200,64,64, 'assets/Hacker_02.png')
      
  def draw_objects(self):
      self.game_window.blit(self.background.img,
                            (self.background.x, self.background.y))
      for i, j in self.player.imgs:
          self.game_window.blit(i, j)
      self.game_window.blit(self.hacker.img, (self.hacker.x, self.hacker.y))
      pygame.display.update()

  def game_loop(self):
    while True:
      self.draw_objects()
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP:
              self.player_direction_y = -1
          elif event.key == pygame.K_DOWN:
              self.player_direction_y = 1
          elif event.key == pygame.K_LEFT:
              self.player_direction_x = -1
          elif event.key == pygame.K_RIGHT:
              self.player_direction_x = 1
            
        if event.type == pygame.KEYUP:
          if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
              self.player_direction_y = 0
          elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            self.player_direction_x = 0
            
      self.player.move_y(self.player_direction_y, self.HEIGHT)
      self.player.move_x(self.player_direction_x, self.WIDTH)
      self.clock.tick(self.tick_rate)
      
