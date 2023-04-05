from windows.ui_Object import UIObject


class UIInteractableObject(UIObject):

    def __init__(self, x: int, y: int, w: int, h: int, img: str) -> None:
        super().__init__(x, y, w, h, img)
        self.interactable = True

