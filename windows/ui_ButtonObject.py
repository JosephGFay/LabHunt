import pygame.mouse

import Joetilities.utilities
from windows.ui_InteractableObject import UIInteractableObject
from Joetilities.utilities import *


class ButtonObject(UIInteractableObject):

    def __init__(self, x: int, y: int, w: int, h: int, img: str, object_id=None) -> None:
        super().__init__(x, y, w, h, img)
        self.collision = self.check_collision()
        self.object_id = object_id

    def check_collision(self) -> bool:
        mouse = pygame.mouse.get_pos()
        return Joetilities.utilities.get_mouse_collision(mouse, self)

