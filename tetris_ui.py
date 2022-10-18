#UI management class
import pygame_gui
from pygame_gui.elements import UILabel, UITextBox
from pygame_gui.core import ObjectID

from settings import *

class TetrisUI():
    def __init__(self, screen, ui_manager):
        self.screen = screen
        self.manager = ui_manager


class GameUI(TetrisUI):
    def __init__(self, screen, ui_manager):
        super().__init__(screen, ui_manager)

        self.standard_ui_build()

    def standard_ui_build(self):
        self.points_label = UITextBox("0", pygame.Rect((0, 0), (screen_width, 35)), self.manager, object_id=ObjectID(object_id="#transparent_label"))

    def update_points_label(self, points):     
        self.points_label.set_text(str(points))