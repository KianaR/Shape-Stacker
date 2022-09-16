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

        self.check_x()
        self.update_board()

    def check_x(self):
        cell_indexes = []
        for cell in shapes[self.type][self.rotation]:
            for row in matrix:
                if cell in row:
                    cell_indexes.append(row.index(cell))
        furthest_point = max(cell_indexes)

        self.x = random.randint(0,(11-furthest_point))

    def current_image(self):
        return self.shapes[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(shapes[self.type])

    def update_board(self):
        shape = shapes[self.type][self.rotation]
        for cell in shape:
            # if shape.index(cell) == 0:
            #     self.board.update_pixel(self.x, self.y, self.colour)
            # else:
            #     x = shape.index(cell)
            #     for row in matrix:
            #         if cell in row:
            #             y = matrix.index(row)
            #     self.board.update_pixel(x, y, self.colour)
            for row in matrix:
                if cell in row:
                    y = self.x + row.index(cell)
                    x = self.y + matrix.index(row)
                    self.board.update_pixel(x, y, self.colour)