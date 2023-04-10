from gameObjects.gameObject import GameObject


class UIObject(GameObject):

    def __init__(self, x: int, y: int, w: int, h: int, img: str) -> None:
        super().__init__(x, y, w, h, img)

