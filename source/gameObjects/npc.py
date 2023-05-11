from source.gameObjects.gameObject import GameObject
import pygame

SPRITES = [
    'assets/hacker_top.png',
    'assets/hacker_right.png',
    'assets/hacker_bottom.png',
    'assets/hacker_left.png',
]


class NPC(GameObject):
    """
        Class object for the game's NPC objects.

        Parameters:

            x : int
                stores the objects x coordinate.
            y : int
                stores the objects y coordinate.
            w : int
                stores the objects width
            h : int
                stores the objects height
            img :str
                string value for the img path to be used for the object's image.

        Attributes:
            infected : bool
                determines if the npc is a hacker or not.
            infected_seat : bool
                determines of the seat that the NPC occupies is a hacker seat.
            name : None
                value to store the NPC's name, populated later by npc_data file.
            ip : None
                value to store the NPC's ip, populated later by npc_data file.
            mac : None
                value to store the NPC's mac, populated later by npc_data file.

        Methods:
            check_infected -> None
                Checks if current NPC is a hacker and then displays their image.

            set_hacker_visible -> None
                loads hacker images and sets them for current NPC.

    """

    def __init__(self, x: int, y: int, w: int, h: int, img: str) -> None:
        super().__init__(x, y, w, h, img)
        self.infected = False
        self.infected_seat = None
        self.check_infected()
        self.name = None
        self.ip = None
        self.mac = None

    def check_infected(self):
        # Check to see if an NPC is infected.
        if self.infected:
            self.set_hacker_visible()

    def set_hacker_visible(self):
        # Change sprites if infected to hacker sprite
        for i in range(4):
            if self.infected_seat == i:
                img = pygame.image.load(SPRITES[i]).convert_alpha()
                self.img = pygame.transform.scale(img, (self.w, self.h))
