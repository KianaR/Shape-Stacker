import pygame 

#Initialisation
pygame.init()
pygame.font.init()

#Screen sizes
screen_width = 200
screen_height = 350

#Title
title = "Tetris Online"

#Colours
black = (0, 0, 0)
white = (255, 255, 255)
clear = (255, 255, 255, 0)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

colours = {
    1: red,
    2: green,
    3: blue
}

#shapes
shapes = [
    [[1, 5, 9, 13], [4, 5, 6, 7]],
    [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
    [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],  
    [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
    [[1, 2, 5, 6]],
]
    

#Other
FPS = 60
font = pygame.font.SysFont("Poppins", 20)
pixel_margin = 2
