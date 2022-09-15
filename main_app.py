#Kiana Rees
#15/09/2022
#Tetris Online

#Imports
import pygame
import pygame_gui

from settings import *
from board import *
from shapes import *

#Initialisation
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((screen_width, screen_height))
uimanager = pygame_gui.UIManager((screen_width, screen_height))

#Main game run
class Game(object):
    def __init__(self):
        global mouse_pos
        mouse_pos = pygame.mouse.get_pos()

        screen.fill(white)
        self.pixel_size = 20
        self.board = Board(self.pixel_size, screen)

        self.shape = Shape(0, 0, self.board)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True      

            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     mouse_x = event.pos[0]
            #     mouse_y = event.pos[1]

            #     column = mouse_x // (self.pixel_size + pixel_margin)
            #     row = mouse_y // (self.pixel_size + pixel_margin)

            #     if self.board.grid[row][column] != self.shape.colour:
            #         self.board.grid[row][column] = self.shape.colour
    
            #         self.board.update_pixel(row, column, colours[self.shape.colour])

            uimanager.process_events(event)

        return False

    def run_logic(self): #run each frame, checks positions and looks for collisions
        pass

    def update_display(self, display):
        uimanager.draw_ui(screen)
        pygame.display.update()


class MainRun():
    def __init__(self):
        self.Main()

    def Main(self):
        pygame.display.set_caption(title)
        screen.fill(black)

        done = False
        self.clock = pygame.time.Clock()

        game = Game() #makes instance of the game

        #Main loop
        while not done:
            done = game.process_events()
            game.run_logic()
            game.update_display(screen)

            time_delta = self.clock.tick(FPS) #Pause for next frame
            uimanager.update(time_delta)

        pygame.quit()


if __name__ == '__main__':
    MainRun()