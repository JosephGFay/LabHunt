import pygame

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)


class TextObject:
    def __init__(self, game_instance, string: str, x: int, y: int, size=12, color=white, back_ground_color=None) -> None:
        self.x = x
        self.y = y
        self.font = pygame.font.Font('freesansbold.ttf', size)
        self.text = self.font.render(string, True, color, back_ground_color)
        self.textRect = self.text.get_rect(x=x, y=y)
        self.img = self.text
        self.w = self.textRect.w
        self.h = self.textRect.h
        self.interactable = False
        self.object_id = None
        if game_instance:
            game_instance.game_window.blit(self.text, self.textRect)
