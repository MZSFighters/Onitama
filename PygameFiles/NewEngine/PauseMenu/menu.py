
import pygame
from MainMenu.constants import *


class Menu():
    def __init__(self, game):           #constructor
        #we taking game as a parameter so we can make use of game variables we have already created
        #we storing the game we got as input in the self.game variable
        self.game = game    

        # some variables
        self.MID_WEIGHT, self.MID_HEIGHT = DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2
        self.run_display = True         # variable that tells our menu to keep running

        #creating the cursor rect
        self.cursor_rect = pygame.Rect(20, 0, self.MID_WEIGHT - 110, self.MID_HEIGHT - 200)

        self.offset = -20      #offset for our cursor


    # to draw cursor on screen
    def draw_cursor(self):
        cursor = pygame.image.load("PygameFiles/NewEngine/images/cursorneon.png")
        cursor = pygame.transform.scale(cursor, (100, 50))
        self.game.display.blit(cursor, (self.cursor_rect.x ,self.cursor_rect.y))

    
    # blitting/displaying our menu to the screen
    def blit_screen(self):
        # from our game loop
        self.game.window.blit(self.game.display, (0,0))
        # whatever we draw on display will nowcome on window
        pygame.display.update()
        self.game.reset_keys()

    def draw(self):
        start_image = pygame.image.load("PygameFiles/NewEngine/images/back3.jpg")
        start_image = pygame.transform.scale(start_image, (DISPLAY_WIDTH, DISPLAY_HEIGHT))
        self.game.display.blit(start_image, (0,0))
                           # font size

        red_king = pygame.image.load("PygameFiles/NewEngine/images/red_king.png")
        red_king = pygame.transform.scale(red_king, (300, 300)).convert_alpha()
        self.game.display.blit(red_king, (-140 ,220))

        blue_king = pygame.image.load("PygameFiles/NewEngine/images/blue_king.png")
        blue_king = pygame.transform.scale(blue_king, (200, 215)).convert_alpha()
        self.game.display.blit(blue_king, (1245,260))


