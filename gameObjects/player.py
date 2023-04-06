from gameObjects.gameObject import GameObject
import pygame

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)


class Player(GameObject):

    def __init__(self, x, y, w, h, img):
        super().__init__(x, y, w, h, img)
        # Variable to store if player is within
        # range of and interactable object

        self.font = None
        self.text = None
        self.textRect = None
        self.imgs = None
        self.can_interact = False
        # Variable to store adjacent interactable object.
        self.adjacent_object = None
        # Render player on initialization.
        self.render()

    def move_y(self, direction, max_height, objects):
        # Function to handle player vertical movement.

        # Check window boundaries
        if (self.y >= max_height - self.h and direction > 0) or (self.y <= 200 and direction < 0):
            return
        for object_list in objects:
            for object in object_list:
                # Top collision
                # Check if top of player intersects with the bottom of an object.
                if self.y == object.y + object.h:
                    # Check if player is within the the bounds of object x and x + w on coordinate plane
                    if (self.x >= object.x and self.x <= object.x + object.w) or (
                            self.x + self.w > object.x and self.x + self.w < object.x + object.w):
                        if direction < 0:
                            self.check_interact(object)
                            return

                # Bottom collision
                # check if bottom of player intersects with the top of an object
                if self.y + self.h == object.y:
                    # Check if player is within the the bounds of object x and x + w on coordinate plane
                    if (self.x >= object.x and self.x <= object.x + object.w) or (
                            self.x + self.w > object.x and self.x + self.w < object.x + object.w):
                        if direction > 0:
                            self.check_interact(object)
                            return

            # Move
        self.y += (direction * 2)
        self.render()
        if direction != 0:
            self.can_interact = False

    def move_x(self, direction, max_width, objects):
        # Function to handle player horizontal movement.

        # Check window boundaries
        if (self.x >= max_width - self.w and direction > 0) or (self.x <= 0 and direction < 0):
            return
        for object_list in objects:
            for object in object_list:
                # Left collision
                # Check if left of player intersects with the right of an object.
                if self.x == object.x + object.w:
                    # Check if player is within the bounds of object y and y + h on coordinate plane
                    if (self.y >= object.y and self.y <= object.y + object.h) or (
                            self.y + self.h > object.y and self.y + self.h < object.y + object.h):
                        if direction < 0:
                            self.check_interact(object)
                            return

                # Right collision
                # Check if right of player intersects with the left of an object.
                if self.x + self.w == object.x:
                    # Check if player is within the the bounds of object y and y + h on coordinate plane
                    if (self.y >= object.y and self.y <= object.y + object.h) or (
                            self.y + self.h > object.y and self.y + self.h < object.y + object.h):
                        if direction > 0:
                            self.check_interact(object)
                            return
        # move
        self.x += (direction * 2)
        self.render()
        if direction != 0:
            self.can_interact = False

    def render(self):
        # Function to handle rendering the player object
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = self.font.render(f'', True, green)

        # Render different messages if interaction is available.
        if self.can_interact:
            # Render Table Interaction
            if self.adjacent_object.__class__.__name__ == 'Table':
                self.text = self.font.render(f'E to Attempt Shoulder Surf', True, green)
            elif self.adjacent_object.__class__.__name__ == 'Server':
                self.text = self.font.render(f'E to Interact with Server', True, green)

        self.textRect = self.text.get_rect()
        self.textRect.center = (self.x + 30, self.y - 30)
        self.imgs = [(self.img, (self.x, self.y)), (self.text, self.textRect)]

    def check_interact(self, obj):
        # Check for interactable object
        if obj.interactable:
            self.can_interact = True
            # Set adjacent object
            self.adjacent_object = obj
