import pygame 
import pygame_gui
import random

#Initialisation
pygame.init()
#pygame.font.init()

#Screen sizes
screen_width = 330 #220
screen_height = 500 #330

#Title
title = "Tetris Enhanced"

uimanager = pygame_gui.UIManager((screen_width, screen_height), "theme.json")

uimanager.add_font_paths("Digital-Desolation-Plus",
                         "assets/fonts/Digital-Desolation-Plus.otf")
uimanager.preload_fonts([{'name': 'Digital-Desolation-Plus', 'html_size': 3, 'style': 'regular'}])

#Colours
black = (0, 0, 0)
white = (255, 255, 255)
grey = (64, 63, 61)
clear = (255, 255, 255, 0)

primary = (0, 150, 198) #0096c6
secondary = (215, 217, 206) #d7d9ce
highlight = (15, 184, 245) #0fb8f5
dark_accent = (31, 48, 101) #1f3065

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (207, 52, 235)
pink = (235, 52, 204)
yellow = (209, 214, 49)

col1 = (219, 72, 122)
col2 = (163, 115, 222)
col3 = (35, 213, 219)
col4 = (227, 104, 194)
col5 = (132, 209, 165)
col6 = (75, 182, 214)

colours = [col1, col2, col3, col4, col5, col6]

#shapes
shapes = [
    [[0, 4, 8, 12], [0, 1, 2, 3]],
    [[0, 1, 4, 8], [4, 5, 6, 10], [1, 5, 9, 8], [0, 4, 5, 6]],
    [[0, 1, 5, 9], [2, 4, 5, 6], [0, 4, 8, 9], [0, 1, 2, 4]],  
    [[1, 4, 5, 6], [0, 4, 5, 8], [4, 5, 6, 9], [1, 4, 5, 9]],
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
pixel_margin = 2
