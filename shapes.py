# Shape class management

from settings import *


class Shape():
    def __init__(self, x, y, board):
        self.x = x
        self.y = y
        self.board = board
        self.type = random.randint(0, len(shapes) - 1)
        self.colour = colours[random.randint(0, len(colours)-1)]
        self.rotation = 0
        
        self.can_generate = self.generate_shape()

    def generate_shape(self):
        fits = self.check_fits()
        if fits != False:
            self.furthest_point_x = self.check_x()
            self.furthest_point_y = self.check_y()
            self.x = random.randint(0, (10-self.furthest_point_x))
            self.update_board()
        else:
            return False
    
    def check_fits(self):
        rows = []
        for cell in shapes[self.type][self.rotation]: # gets all rows the cells are in on grid
            row_num = int(cell/4)
            rows.append(row_num)
        
        rows_down = max(rows) # get last row shape in
        for row in range(0, rows_down): # for each row between start of grid to highest row num, if x, return false
            for cell in self.board.grid[row]:
                if cell != "":
                    return False

    def check_x(self):
        cell_indexes = []
        for cell in shapes[self.type][self.rotation]:
            for row in matrix:
                if cell in row:
                    cell_indexes.append(row.index(cell))
        furthest_point = max(cell_indexes)+1
        return furthest_point

    def check_y(self):
        row_indexes = []
        for cell in shapes[self.type][self.rotation]:
            for row in matrix:
                if cell in row:
                    row_indexes.append(matrix.index(row))

        furthest_point = max(row_indexes)+1
        return furthest_point

    def check_collisions(self, direction):
        for cell in shapes[self.type][self.rotation]:
            x = cell % 4 + self.x
            y = cell//4 + self.y

            if direction == "y":
                y += 1
            elif direction == "left":
                x -= 1
            else: 
                x += 1
                
            if x >= len(self.board.grid[y]) or (self.board.grid[y][x] != "x" and self.board.grid[y][x] !=""):
                return True

    def move_down(self):
        prev_y = self.y

        # if in board range
        if prev_y + self.furthest_point_y != len(self.board.grid):
            collision = self.check_collisions("y")
            
            if collision:
                return True

            self.y += 1
            self.update_board(None, prev_y)

        elif prev_y + self.furthest_point_y >= len(self.board.grid):
            return True

    def rotate(self):
        prev_rotation = self.rotation
        prev_x = self.x
        prev_y = self.y
        self.rotation = (self.rotation + 1) % len(shapes[self.type])

        # add checks for bounds of window

        self.update_board(prev_x, prev_y, prev_rotation)

    def update_board(self, previous_x=None, previous_y=None, previous_rotation=None):
        if previous_rotation != None:
            shape = shapes[self.type][previous_rotation]
        else:
            shape = shapes[self.type][self.rotation]

        if previous_y != None and previous_x != None:
            for cell in shape:
                for row in matrix:
                    if cell in row:
                        x = previous_x + row.index(cell)
                        y = previous_y + matrix.index(row)
                        self.board.update_pixel(y, x, white)

        elif previous_x != None:
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
