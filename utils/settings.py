import pygame
pygame.init()
pygame.font.init()

#Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PINK = (255, 0, 255)
PURPLE = (138,43,226)
BROWN = (139,69,19)
ORANGE = (255,140,0)
GREY = (105,105,105)
CYAN = (0,191,255)
PEACH = (255,218,185)

FPS = 120

WIDTH, HEIGHT = 500, 600

ROWS = COLS = 50

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH // ROWS

BG_COLOUR = WHITE

DRAW_GRID_LINES = True

def get_font(size):
    return pygame.font.SysFont("comicsans", size)
