import pygame


class GameObject:
    """
    A class to represent a GameObject prototype.

    Attributes
    ----------
    x : int
      A coordinate value to be used for horizontal positioning.
    y : int
      A coordinate value to be used for vertical positioning
    w : int
      Determines the width of the object.
    h : int
      Determines the height of the object.
    img : str
      String path to image file.
    """

    def __init__(self, x: int, y: int, w: int, h: int, img: str = None, name: str = None) -> None:
        """
        Constructs the object, giving it a position, a size, and an image.

        Parameters
        ----------
        x : int
          A coordinate value to be used for horizontal positioning.

        y : int
          A coordinate value to be used for vertical positioning.

        w : int
          Determines the width of the object.

        h : int
          Determines the height of the object.
        """
        # Supply a value to name if it is given as parameter
        if name:
            self.name = name
        # Supply a value to img if it is given as parameter
        if img:
            img = pygame.image.load(img).convert_alpha()
            self.img = pygame.transform.scale(img, (w, h))
        # Initialize instance attributes.
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.interactable = False
        self.selected = False
        self.object_id = None
