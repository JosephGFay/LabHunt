

def get_collision(a: object, b: object) -> bool:
    if b.x <= a.x <= (b.x + b.w):
        if b.y <= a.y <= (b.y + b.h):
            return True
    return False


def get_mouse_collision(a: tuple, b: object) -> bool:
    if b.x <= a[0] <= (b.x + b.w):
        if b.y <= a[1] <= (b.y + b.h):
            return True
    return False
