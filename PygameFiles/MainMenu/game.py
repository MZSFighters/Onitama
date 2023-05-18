
# importing necessary modules
import pygame
from mainmenu import *
from settingsmenu import *
from misc import *
from menu import *

# Game class
class Game():
    def __init__(self):             # constructor
        pygame.init()               # initialising pygame

        # declaring and assigning variables -> setup & font type + some colours
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.BACK_KEY, self.START_KEY = False, False, False, False
        self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT = 700, 650
        self.font_name = "arialblack"
        self.BLACK, self.WHITE = (0,0,0), (255,255,255)
        self.GOLD = (255,215,0)

        # creating the canvas to draw on
        self.display = pygame.Surface((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))  
        # setting window for player to see what we are drawing
        self.window = pygame.display.set_mode(((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT)))
        # Game Object Done!
        
        self.misc = HTP(self)
        # Creating an instance of Main Menu class
        self.main_menu = MainMenu(self)
        # Now...
        self.highscore_settings = LeaderBoard(self)
        self.loadsaved_settings = LoadSavedGame(self)
        self.settings_menu = SettingsMenu(self)
        self.sound_settings = Sound(self)
        self.ai_settings = AIDiff(self)
        self.credits_settings = Credits(self)
        self.help_settings = Help(self)
        self.play_settings = PlayMenu(self)
        self.customcard_settings = CustomCards(self)
        self.curr_menu = self.main_menu

    # The game loop that runs until the user quits
    def game_loop(self):
        while self.playing:             # As long as the player is playing
            self.check_events()         # Check for any keys pressed
            if self.BACK_KEY:           # if BACKSPACE then stop and return to main screen
                self.playing = False
            # reset ur canvas and the window
            start_image = pygame.image.load("images/onitama_highres.jpg")
            start_image = pygame.transform.scale(start_image, (700, 650))

            # else draw "Hi" on screen
            self.display.blit(start_image, (0,0))
            self.draw_text("Hi", 20, self.DISPLAY_WIDTH/2, self.DISPLAY_HEIGHT/2)
            self.window.blit(self.display, (0,0)) # whatever we draw on display will nowcome on window
            pygame.display.update() # physically moves image on the computer screen
            self.reset_keys()   # resetting the screens
    
    
    # event checking -> user input action-reaction...
    def check_events(self):
        for event in pygame.event.get():
            # Quitting event instance
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                # stop displaying menu as well (added later)
                self.curr_menu.run_display =False
            
            # If Key is pressed then store that key as
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:        # Enter Key
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:     # Backspace Key
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:          # Down Key
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:            # Up Key
                    self.UP_KEY = True


    # we need a way to reset these variables after each game loop or each frame
    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.BACK_KEY, self.START_KEY = False, False, False, False

    # to draw text on the screen
    def draw_text(self, text, size, x, y):
        font = pygame.font.SysFont("arial black", size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def drawleft_text(self, text, size, x, y):
        font = pygame.font.SysFont("arialblack", size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (x, y)
        self.display.blit(text_surface, text_rect)



    def renderTextCenteredAt(self, text, font, colour, x, y, screen, allowed_width):
    # first, split the text into words
        words = text.split()

        # now, construct lines out of these words
        lines = []
        while len(words) > 0:
            # get as many words as will fit within allowed_width
            line_words = []
            while len(words) > 0:
                line_words.append(words.pop(0))
                fw, fh = font.size(' '.join(line_words + words[:1]))
                if fw > allowed_width:
                    break

            # add a line consisting of those words
            line = ' '.join(line_words)
            lines.append(line)

        # now we've split our text into lines that fit into the width, actually
        # render them

        # we'll render each line below the last, so we need to keep track of
        # the culmative height of the lines we've rendered so far
        y_offset = 0
        for line in lines:
            fw, fh = font.size(line)

            # (tx, ty) is the top-left of the font surface
            tx = x - fw / 2
            ty = y + y_offset

            font_surface = font.render(line, True, colour)
            self.display.blit(font_surface, (tx, ty))

            y_offset += fh

