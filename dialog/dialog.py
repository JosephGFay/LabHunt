import pygame
from gameObjects.gameObject import GameObject

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)


class Dialog(GameObject):
    def __init__(self, game_instance, string):
        x = 400
        y = 200
        w = 400
        h = 400
        img = 'assets/dialog_window.png'
        super().__init__(x, y, w, h, img)
        game_instance.dialog_running = True
        game_instance.game_window.blit(self.img, (self.x - 10, self.y - 28))
        self.set_header(string, game_instance)
        self.set_footer(game_instance)
        pygame.display.update()

    def set_header(self, string, game_instance):
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.header = self.font.render(string, True, white)
        self.headerRect = self.header.get_rect(x=self.x + 10, y=self.y + 20)
        game_instance.game_window.blit(self.header, self.headerRect)

    def set_footer(self, game_instance):
        self.font = pygame.font.Font('freesansbold.ttf', 10)
        self.footer = self.font.render('Press ESC to close dialog...', True, white)
        self.footerRect = self.footer.get_rect(x=self.x, y=self.y + self.h - 60)
        game_instance.game_window.blit(self.footer, self.footerRect)

    def run_dialog(self, game_instance):
        while game_instance.dialog_running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_instance.dialog_running = False
