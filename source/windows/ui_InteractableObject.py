from source.windows.ui_Object import UIObject


class UIInteractableObject(UIObject):

    def __init__(self, x: int, y: int, w: int, h: int, img: str, object_id=None) -> None:
        super().__init__(x, y, w, h, img)
        self.interactable = True
        self.object_id = object_id

