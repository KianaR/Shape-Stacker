#UI management class
import pygame_gui
from pygame_gui.elements import UITextBox, UIPanel, UILabel, UIButton
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
        self.points_label = UITextBox('<font face=Digital-Desolation-Plus size=3>0</font>', pygame.Rect((0, 0), (screen_width, 50)), self.manager, object_id=ObjectID(object_id="#points_label"))

    def update_points_label(self, points):  
        text = "<font face=Digital-Desolation-Plus size=3>" + str(points) + "</font>"
        self.points_label.set_text(text)

    def game_over_screen(self):
        popup_box = UIPanel(pygame.Rect((0, screen_height/2-75/2), (screen_width, 150)), 1, self.manager, object_id=ObjectID(object_id="#gameover_popup"))
        label = UILabel((pygame.Rect((0, 0), (screen_width, 75))), "Game Over!", self.manager, popup_box, object_id=ObjectID(object_id="#gameover_lbl"))

        btn_holder = UIPanel(pygame.Rect((0, 100), (screen_width, 35)), 2, self.manager, container=popup_box, object_id=ObjectID(object_id="#exit_btn_holder"))
        self.exit_btn = UIButton((pygame.Rect((screen_width/2-75/2, 0), (75, 35))), "Exit", self.manager, btn_holder, object_id=ObjectID(object_id="#exit_btn", class_id="@btn"))