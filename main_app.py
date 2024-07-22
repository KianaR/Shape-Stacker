#Kiana Rees
#15/09/2022
#Tetris Online

#Imports
from settings import *
from board import *
from shapes import *
from tetris_ui import *

#Initialisation
logo = pygame.image.load("assets\imgs\icon.png")
pygame.display.set_icon(logo)

bg = pygame.image.load("assets\imgs\mainbg.png")

screen = pygame.display.set_mode((screen_width, screen_height))

#Main game run
class Game(object):
    def __init__(self):
        global mouse_pos
        mouse_pos = pygame.mouse.get_pos()
        self.move_shape_down = pygame.USEREVENT + 0

        screen.fill(primary)
        screen.blit(bg, (0,0))
        self.game_ui = GameUI(screen, uimanager)

        self.pixel_size = 20
        self.board = Board(self.pixel_size, screen)

        self.shape = Shape(0, 0, self.board)

        self.points = 0

        pygame.time.set_timer(self.move_shape_down, 250) #testing speed: 250, non-test:1250

    def game_over(self):
       self.game_ui.game_over_screen()

    def new_shape(self):
        self.shape = Shape(0, 0, self.board)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True   

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if self.game_ui.exit_btn.object_ids[0] + "." + self.game_ui.exit_btn.object_ids[1] + ".@btn" == event.ui_object_id:
                    return True

            if event.type == self.move_shape_down:
                if self.shape.can_generate != False:
                    shape_move = self.shape.move_down()
                    if shape_move == True: 
                        for cell in shapes[self.shape.type][self.shape.rotation]:
                            x = cell%4 + self.shape.x
                            y = cell//4 + self.shape.y
                            self.board.update_pixel(y, x, self.shape.colour, False)

                        points_check = self.board.full_row_check() # checks for full rows
                        if points_check and points_check > 0:
                            self.points += points_check
                            self.game_ui.update_points_label(self.points)
                        self.new_shape() # new shape starts

                elif self.shape.can_generate == False:
                    self.game_over()

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 3:
            #         self.shape.rotate()

            if event.type == pygame.KEYDOWN:
                prev_x = None
                prev_y = None

                new_x = self.shape.x
                moving = False

                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    collision = self.shape.check_collisions("left")
                    new_x -= 1
                    moving = True
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    collision = self.shape.check_collisions("right")
                    new_x += 1
                    moving = True

                if new_x >= 0 and self.shape.check_x() + new_x <=10 and moving == True:
                    if collision != True:
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
        uimanager.draw_ui(display)
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