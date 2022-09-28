import pygame 
import random

#Initialisation
pygame.init()
pygame.font.init()

#Screen sizes
screen_width = 220
screen_height = 330

#Title
title = "Tetris Online"

#Colours
black = (0, 0, 0)
white = (255, 255, 255)
grey = (64, 63, 61)
clear = (255, 255, 255, 0)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (207, 52, 235)
pink = (235, 52, 204)
yellow = (209, 214, 49)

colours = [
    red,
    green,
    blue,
    purple,
    pink,
    yellow
]

#shapes
shapes = [
    [[0, 4, 8, 12], [0, 1, 2, 3]],
    [[0, 1, 4, 8], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
    [[0, 1, 5, 9], [0, 1, 2, 4], [0, 4, 8, 9], [2, 4, 5, 6]],  
    [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [0, 4, 5, 8]],
    [[0, 1, 4, 5]],
]

matrix = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
    [12, 13, 14, 15]
]

#Other
FPS = 60
font = pygame.font.SysFont("Poppins", 20)
pixel_margin = 2
