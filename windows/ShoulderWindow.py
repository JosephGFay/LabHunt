from windows.interactiveWindow import InteractiveWindow
from windows.ui_Object import UIObject
from windows.ui_InteractableObject import UIInteractableObject
from dialog.textObject import TextObject

import pygame
import sys
from pygame.locals import QUIT
import Joetilities.utilities
from data.npc_activites import activities, articles
import random


class ShoulderWindow(InteractiveWindow):

    def __init__(self, student, detected) -> None:
        super().__init__()
        self.x = 100
        self.w = 1000
        self.h = 600
        self.img = pygame.image.load('assets/dialog_window.png')
        self.img = pygame.transform.scale(self.img, (self.w, self.h))
        self.detected = detected

        self.col_0 = self.x + 45
        self.col_1 = self.x + 45 * 4
        self.col_2 = self.x + 45 * 7
        self.col_3 = self.x + 45 * 10

        self.row_0 = self.y + 80
        self.row_1 = self.y + 40 * 6
        self.row_2 = self.row_1 + 40
        self.row_3 = self.row_2 + 40
        self.row_4 = self.row_3 + 40

        # Random number for student screen text options
        self.ran_student_screen = random.randint(0, len(activities['student']['screens']) - 1)
        # Random number for articles
        self.chance_for_art = random.randint(0, 3)
        self.ran_art = random.randint(0, len(articles))
        # Random number for activities
        self.ran_act = random.randint(0, len(activities['student']['activity']) - 1)
        # Random number for suspicious student text
        self.chance_for_sus = random.randint(0, 9)
        self.ran_student_suspicious = random.randint(0, len(activities['student']['suspicious']) - 1)

        self.ui_elements = [
            # Title
            TextObject(None, f'{student.name}', self.col_0 + 150, self.row_0, 36),
            # Profile
            UIObject(self.x + 40, self.row_0, 100, 120, 'assets/npc_top.png'),
            # Event Picture
            UIObject(self.x + self.w - 390, self.row_0, 350, 480, 'assets/shoulder_view.png'),

            UIInteractableObject(self.x + 190, self.row_0 + 60, 200, 50, 'assets/expose_hacker.png',
                                 object_id='accuse_button')
        ]

        # Default text to display
        self.ui_text = [
            # Event Text
            TextObject(None, f"{student.name} is {activities['student']['activity'][self.ran_act]}", self.col_0,
                       self.row_1,
                       12),
            # Activity 01
            TextObject(None, f"On their screen you can see {activities['student']['screens'][self.ran_student_screen]}",
                       self.col_0, self.row_2, 12),

        ]

        # Display text for viewing an article
        if self.chance_for_art == 1:
            self.ui_text = [
                # Event Text
                TextObject(None, f'{student.name} is browsing cyber security articles', self.col_0, self.row_1, 12),
                # Activity 01
                TextObject(None, f"They are reading \"{articles[self.ran_art - 1]}\"", self.col_0, self.row_2, 12),
                # Activity 02

            ]

        # Display text for the hacker or display text for a suspicious user.
        if student.infected or self.chance_for_sus == 1:
            self.ui_text = [
                TextObject(None, f"{student.name} is {activities['student']['activity'][self.ran_act]}", self.col_0,
                           self.row_1, 12),

                TextObject(None,
                           f"On their screen you can see {activities['hacker']['suspicious'][self.ran_student_suspicious]}",
                           self.col_0, self.row_2, 12),
            ]

        self.populate_menu_options(self.ui_elements + self.ui_text)

    def display(self, game_instance, student):
        # Window Running Loop for the instance.
        while True:
            # Display the background dialog window
            game_instance.game_window.blit(self.img, (self.x, self.y))

            # Display all selection menu objects in menu_options list.
            for index, selection in enumerate(self.menu_options):

                if index == self.selection:
                    self.img_sel = pygame.transform.scale(self.img_sel, (selection.w, selection.h))
                    game_instance.game_window.blit(selection.img, (selection.x, selection.y))
                    game_instance.game_window.blit(self.img_sel, (selection.x, selection.y))
                else:
                    game_instance.game_window.blit(selection.img, (selection.x, selection.y))

            # Get Mouse Position
            mouse_pos = pygame.mouse.get_pos()
            for index, selection in enumerate(self.menu_options):
                if Joetilities.utilities.get_mouse_collision(mouse_pos, selection):
                    # Check if menu option is interactable
                    if selection.interactable:
                        self.selection = index
                    else:
                        self.selection = None

            # Event Listener
            for event in pygame.event.get():
                if event.type == QUIT:
                    # Quit the game if event fired.
                    pygame.quit()
                    sys.exit()
                # Listen for KEY events
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_instance.draw_objects()
                        return
                if event.type == pygame.MOUSEBUTTONUP:
                    for index, selection in enumerate(self.menu_options):
                        if Joetilities.utilities.get_mouse_collision(mouse_pos, selection):
                            if selection.object_id == 'accuse_button':
                                if student.infected:
                                    print('You win')
                                else:
                                    print('You lose')

            pygame.display.update()
