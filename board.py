#Board setup and scripts

from settings import *

class Board():
    def __init__(self, pixel_size, screen):
        self.screen = screen

        self.pxl_size = pixel_size

        self.generate_board()

    def generate_board(self):
        #Logical grid
        self.grid = []
        for row in range(15):
            self.grid.append([]) #List to represent each row
            for column in range(10):
                self.grid[row].append(0)

        self.grid_width = 222 #20+2 (x10) +2
        self.grid_height = (15*22) +2 

        self.grid_surface = pygame.Surface((self.grid_width, self.grid_height), pygame.SRCALPHA)
        self.grid_surface.fill(0)
        self.grid_surface.fill(dark_accent)

        #Visual grid
        for row in range (15):
            for column in range (10):
                self.update_pixel(row, column, white)
        
    def update_pixel(self, row, column, colour, moving=True):
        self.grid_surface.fill(0)
        pygame.draw.rect(self.grid_surface, colour, [(pixel_margin + self.pxl_size) * column + pixel_margin, #Pixel size representing height and width
                                (pixel_margin + self.pxl_size) * row + pixel_margin,
                                self.pxl_size,
                                self.pxl_size])
                                
        if colour == white:
            self.grid[row][column] = ""
        elif moving:
            self.grid[row][column] = "x"
        else: 
            self.grid[row][column] = colour
        
        self.screen.blit(self.grid_surface, (screen_width / 2 - self.grid_width / 2, screen_height / 2 - self.grid_height / 2))
        #pygame.display.update()

    def full_row_check(self):
        filled_row = 0
        filled_rows = 0

        for ind, row in enumerate(self.grid):
            filled = []
            for cell in row:
                if cell != "":
                    filled.append(cell)

            if len(filled) == len(row):
                filled_rows += 1
                filled_row = ind+1

                prev_row = []
                for temp_row in range(0, filled_row):
                    current_row = self.grid[temp_row].copy()
                    for cindex, cell in enumerate(self.grid[temp_row]):
                        if temp_row != 0 and prev_row[cindex] != "":
                            self.update_pixel(temp_row, cindex, prev_row[cindex], False)
                        else:
                            self.update_pixel(temp_row, cindex, white)
                    prev_row = current_row
            
        return filled_rows*10