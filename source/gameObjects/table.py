from source.gameObjects.gameObject import GameObject
from source.gameObjects.npc import NPC
import random

green = (0, 255, 0)


class Table(GameObject):

    def __init__(self, x, y, w, h, img, name, data):
        super().__init__(x, y, w, h, img, name)
        self.textRect = None
        self.text = None
        self.font = None
        self.infected = False
        self.interactable = True
        self.name = name
        self.render()
        self.top_seat = (self.x + 52, self.y - 32)
        self.right_seat = ((self.x + self.w), (self.y + 46))
        self.left_seat = ((self.x - 64), (self.y + 46))
        self.bottom_seat = (self.x + 46, (self.y + self.h - 60))

        self.npc_top = NPC(
            x=self.top_seat[0],
            y=self.top_seat[1],
            w=55,
            h=55,
            img='source/assets/npc_top.png',
        )
        self.npc_right = NPC(
            x=self.right_seat[0],
            y=self.right_seat[1],
            w=60,
            h=100,
            img='source/assets/npc_right.png',
        )
        self.npc_left = NPC(
            x=self.left_seat[0],
            y=self.left_seat[1],
            w=60,
            h=100,
            img='source/assets/npc_left.png',
        )
        self.npc_bottom = NPC(
            x=self.bottom_seat[0],
            y=self.bottom_seat[1],
            w=60,
            h=100,
            img='source/assets/npc_bottom.png',
        )

        self.npcs = [self.npc_top, self.npc_right, self.npc_bottom, self.npc_left]
        self.populate_npc_data(data)

    def populate_npc_data(self, npc_data):
        # Populate Names
        for npc in self.npcs:
            npc.name = npc_data['names'][len(npc_data['names']) - 1]
            npc_data['names'].pop()

        # Populate IP
        for npc in self.npcs:
            npc.ip = npc_data['ips'][len(npc_data['ips']) - 1]
            npc_data['ips'].pop()

        # Populate MAC
        for npc in self.npcs:
            npc.mac = npc_data['macs'][len(npc_data['macs']) - 1]
            npc_data['macs'].pop()

    def render(self):
        if self.infected:
            self.set_hacker()

    def set_hacker(self):
        infected_seat = random.randint(0, 3)
        self.npcs[infected_seat].infected = True
        self.npcs[infected_seat].infected_seat = infected_seat

    def get_hacker(self):
        for npc in self.npcs:
            if npc.infected:
                return npc
