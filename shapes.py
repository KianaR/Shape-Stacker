#Shape class management

import random
from settings import *

class Shape():
    def __init__(self, x , y, board):
        self.x = x
        self.y = y
        self.board = board
        self.type = random.randint(0, len(shapes) - 1)
        self.colour = random.randint(0, len(colours) - 1)
        self.rotation = 0

        self.update_board()

    def current_image(self):
        return self.shapes[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(shapes[self.type])

    def update_board(self):
        for cell in shapes[self.type][self.rotation]:
            pass
            #self.board.update_pixel(, self.colour) HERE