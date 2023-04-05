from windows.interactiveWindow import InteractiveWindow
from windows.ui_Object import UIObject
from windows.ui_InteractableObject import UIInteractableObject
from dialog.textObject import TextObject


class TableWindow(InteractiveWindow):

    def __init__(self) -> None:
        super().__init__()
        self.col_0 = self.x + 45
        self.col_1 = self.x + 45 * 4
        self.col_2 = self.x + 45 * 7
        self.col_3 = self.x + 45 * 10

        self.row_0 = self.y + 40
        self.row_1 = self.y + 40 * 5

        self.ui_objects = [
            UIObject(self.col_0, self.row_0, 100, 120, 'assets/npc_top.png'),
            UIObject(self.col_1, self.row_0, 100, 120, 'assets/npc_top.png'),
            UIObject(self.col_2, self.row_0, 100, 120, 'assets/npc_top.png'),
            UIObject(self.col_3, self.row_0, 100, 120, 'assets/npc_top.png'),

            TextObject(None, 'Chris', self.col_0+30, self.row_1),
            TextObject(None, 'Joseph', self.col_1+30, self.row_1),
            TextObject(None, 'Brittany', self.col_2+25, self.row_1),
            TextObject(None, 'Damion', self.col_3+25, self.row_1),
        ]
        self.populate_menu_options(self.ui_objects)
