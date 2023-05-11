from source.gameObjects.gameObject import GameObject


class Hacker(GameObject):
    """
        An Object created to handle functionality for the game's hacker NPC.

        Still in implementation phase

        Parameters:

            x : int
                stores the x coordinate
            y : int
                stores the y coordinate
            w : int
                stores the width of the object
            h : int
                stores the height of the object
            img : str
                string value to be used for loading the objects image.

    """

    def __init__(self, x, y, w, h, img):
        """
            Class constructor for the hacker object.
        """
        # Call to parent class.
        super().__init__(x, y, w, h, img)
