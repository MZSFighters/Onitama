
import pygame

class Menu():
    def __init__(self, game):           #constructor
        #we taking game as a parameterso we can make use of game variables we have already created
        #we storing the game we got as input in the self.game variable
        self.game = game    

        # some variables
        self.MID_WEIGHT, self.MID_HEIGHT = self.game.DISPLAY_WIDTH / 2, self.game.DISPLAY_HEIGHT / 2
        self.run_display = True         # variable that tells our menu to keep running

        #creating the cursor rect
        self.cursor_rect = pygame.Rect(20, 0, self.MID_WEIGHT - 110, self.MID_HEIGHT - 200)
        self.backButton_rect = pygame.Rect(20,0,self.MID_WEIGHT, self.MID_HEIGHT)
        self.offset = 70       #offset for our cursor


    # to draw cursor on screen
    def draw_cursor(self):
        cursor = pygame.image.load("images/katana-28768.png")
        cursor = pygame.transform.scale(cursor, (100, 50))
        self.game.display.blit(cursor, (self.cursor_rect.x,self.cursor_rect.y))

    def draw_back(self):
        back = pygame.image.load("images/pawn.png")
        back = pygame.transform.scale(back, (100, 50))
        self.game.display.blit(back, (self.backButton_rect.x, self.backButton_rect.y))
    
    # blitting/displaying our menu to the screen
    def blit_screen(self):
        # from our game loop
        self.game.window.blit(self.game.display, (0,0))
        # whatever we draw on display will nowcome on window
        pygame.display.update()
        self.game.reset_keys()

