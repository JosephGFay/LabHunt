from windows.interactiveWindow import InteractiveWindow
from windows.ui_Object import UIObject
from windows.ui_InteractableObject import UIInteractableObject
from dialog.textObject import TextObject


class TableWindow(InteractiveWindow):

    def __init__(self, table) -> None:
        super().__init__()
        self.col_0 = self.x + 45
        self.col_1 = self.x + 45 * 4
        self.col_2 = self.x + 45 * 7
        self.col_3 = self.x + 45 * 10

        self.row_0 = self.y + 80
        self.row_1 = self.y + 40 * 5
        self.row_2 = self.row_1 + 40 * 5

        self.ui_objects = [
            # Title
            TextObject(None, 'Select A Student', self.col_0 + 100, self.row_0, 36),
            # Player cards
            UIInteractableObject(self.col_0, self.row_1, 100, 120, 'assets/npc_top.png'),
            UIInteractableObject(self.col_1, self.row_1, 100, 120, 'assets/npc_top.png'),
            UIInteractableObject(self.col_2, self.row_1, 100, 120, 'assets/npc_top.png'),
            UIInteractableObject(self.col_3, self.row_1, 100, 120, 'assets/npc_top.png'),
            # Names
            TextObject(None, table.npc_top.name, self.col_0 + 30, self.row_2),
            TextObject(None, table.npc_right.name, self.col_1 + 30, self.row_2),
            TextObject(None, table.npc_bottom.name, self.col_2 + 25, self.row_2),
            TextObject(None, table.npc_left.name, self.col_3 + 25, self.row_2),
        ]
        self.populate_menu_options(self.ui_objects)
