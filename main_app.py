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
        self.move_shape_down = pygame.USEREVENT + 0

        screen.fill(white)
        self.pixel_size = 20
        self.board = Board(self.pixel_size, screen)

        self.shape = Shape(0, 0, self.board)

        pygame.time.set_timer(self.move_shape_down, 1750)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True      

            if event.type == self.move_shape_down:
                self.shape.move_down()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    pass

            if event.type == pygame.KEYDOWN:
                prev_x = None
                prev_y = None

                new_x = self.shape.x

                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    new_x -= 1
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    new_x += 1

                if new_x >= 0 and self.shape.check_x() + new_x <=10:
                    prev_x = self.shape.x
                    self.shape.x = new_x
                
                self.shape.update_board(prev_x, prev_y)

            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     mouse_x = event.pos[0]
            #     mouse_y = event.pos[1]

            #     column = mouse_x // (self.pixel_size + pixel_margin)
            #     row = mouse_y // (self.pixel_size + pixel_margin)

            #     if self.board.grid[row][column] != self.shape.colour:
            #         self.board.grid[row][column] = self.shape.colour
    
            #         self.board.update_pixel(row, column, colours[self.shape.colour])

            # add dark mode after u add movement, detect whether cell has block on it or not if so dont change the bg colour. 
            
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