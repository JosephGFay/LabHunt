def get_collision(a: object, b: object) -> bool:
    """Check for collision between two rectangular objects.

    Args:
        a (object): The first object.
        b (object): The second object.

    Returns:
        bool: True if there is a collision, False otherwise.
    """
    if b.x <= a.x <= (b.x + b.w):
        if b.y <= a.y <= (b.y + b.h):
            return True
    return False


def get_mouse_collision(a: tuple, b: object) -> bool:
    """Check for collision between a mouse position and a rectangular object.

    Args:
        a (tuple): A tuple representing the mouse position, with the first element being the x-coordinate and the second element being the y-coordinate.
        b (object): The rectangular object.

    Returns:
        bool: True if the mouse is colliding with the object, False otherwise.
    """
    if b.x <= a[0] <= (b.x + b.w):
        if b.y <= a[1] <= (b.y + b.h):
            return True
    return False
