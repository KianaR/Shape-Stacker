#Shape class management

from settings import *

class Shape():
    def __init__(self, x, y, board):
        self.x = x
        self.y = y
        self.board = board
        self.type = random.randint(0, len(shapes) - 1)
        self.colour = colours[random.randint(0, len(colours)-1)]
        self.rotation = 0

        furthest_point = self.check_x() 
        self.x = random.randint(0,(10-furthest_point))
        self.update_board()

    def check_x(self):
        cell_indexes = []
        for cell in shapes[self.type][self.rotation]:
            for row in matrix:
                if cell in row:
                    cell_indexes.append(row.index(cell))
        furthest_point = max(cell_indexes)+1
        return furthest_point

    def move_down(self):
        prev_y = self.y
        self.y += 1
        self.update_board(None, prev_y)

    def current_image(self):
        return self.shapes[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(shapes[self.type])

    def update_board(self, previous_x=None, previous_y=None):
        shape = shapes[self.type][self.rotation]

        if previous_x != None:
            for cell in shape:
                for row in matrix:
                    if cell in row:
                        x = previous_x + row.index(cell)
                        y = self.y + matrix.index(row)
                        self.board.update_pixel(y, x, white)
        elif previous_y != None:
            for cell in shape:
                for row in matrix:
                    if cell in row:
                        x = self.x + row.index(cell)
                        y = previous_y + matrix.index(row)
                        self.board.update_pixel(y, x, white)

        for cell in shape:
            for row in matrix:
                if cell in row:
                    x = self.x + row.index(cell)
                    y = self.y + matrix.index(row)
                    self.board.update_pixel(y, x, self.colour)