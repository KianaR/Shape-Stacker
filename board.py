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

        self.grid_surface = pygame.Surface((screen_width, screen_height))
        self.grid_surface.fill(black)

        #Visual grid
        for row in range (15):
            for column in range (10):
                self.update_pixel(row, column, white)
        
    def update_pixel(self, row, column, colour):
        pygame.draw.rect(self.grid_surface, colour, [(pixel_margin + self.pxl_size) * column + pixel_margin, #Pixel size representing height and width
                                (pixel_margin + self.pxl_size) * row + pixel_margin,
                                self.pxl_size,
                                self.pxl_size])

        self.grid[row][column] = "x"
        
        self.screen.blit(self.grid_surface, (0,0))
        #pygame.display.update()