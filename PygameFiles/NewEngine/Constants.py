import pygame

# initialising pygame's font library
pygame.font.init()

# some useful colours
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

# some measurement variables
WIDTH = 1400                                # window width
HEIGHT = 750                                # window height
ROWS, COLS = 5, 5
BOARD_WIDTH, BOARD_HEIGHT = 750, 750
SQUARE_SIZE = 140
card_width, card_height = 200, 100
WIDTHEXCB = WIDTH - BOARD_WIDTH             # width excluding board width


# some font initialisation
HEADING_TEXTSIZE = 40
Win_font = pygame.font.SysFont('arialblack',100)
