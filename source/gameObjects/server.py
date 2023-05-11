from source.gameObjects.gameObject import GameObject


class Server(GameObject):

    def __init__(self, x, y, w, h, img):
        super().__init__(x, y, w, h, img)
        self.interactable = True
