
# importing necessary modules
import pygame
from PauseMenu.pausemenu import *
from PauseMenu.settingsmenu import *
from PauseMenu.misc import *
from PauseMenu.menu import *
from MainMenu.constants import *
from pygame import mixer



class Game():
    def __init__(self):             # constructor
        pygame.init()               # initialising pygame
        mixer.init()
        self.mix = mixer
        self.mix.music.set_volume(0.2)
        self.mix.music.load("PygameFiles/NewEngine/images/01 Sakuya's Theme.mp3")
        # declaring and assigning variables
        self.CLOCK = pygame.time.Clock() 
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.BACK_KEY, self.START_KEY = False, False, False, False
        
        # creating the canvas to draw on
        self.display = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        self.Manager = pygame_gui.UIManager((DISPLAY_WIDTH, DISPLAY_HEIGHT))

        # setting window for player to see what we are drawing
        self.window = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT), pygame.RESIZABLE)
        self.Text_Input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((350,275),(100,50), manager = self.Manager, object_id = "#texty"))
        
        
        # Creating instances of Menu classes...
        self.pause_menu = PauseMenu(self)
        
        self.settings_menu = SettingsMenu(self)
        self.sound_settings = Sound(self)
        self.misc = HTP(self)
        self.ai_settings = AIDiff(self)
        self.credits_settings = Credits(self)
        self.help_settings = Help(self)
        self.sound_settings = Sound(self)
        
        
        self.curr_menu = self.pause_menu



    # The game loop that runs until the user quits
    def game_loop(self):
        while self.playing:
            UI_Refresh_rate = self.CLOCK.tick(60)/1000             # As long as the player is playing
            self.check_events()         # Check for any keys pressed
            if self.BACK_KEY:           # if BACKSPACE then stop and return to main screen
                self.playing = False

          
            
    
    # event checking -> user input action-reaction...
    def check_events(self):
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                # stop displaying menu as well
                self.curr_menu.run_display =False
            
            self.Manager.process_events(event)
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
    def draw_text(self, text, size, x, y, colour, alignment):
        font = pygame.font.SysFont('arialblack',size)
        text_surface = font.render(text, True, colour)
        text_rect = text_surface.get_rect()
        if alignment == "center":               
            text_rect.center = (x, y)
        elif alignment == "left":               # left-aligned text
            text_rect.bottomleft = (x, y)
        self.display.blit(text_surface, text_rect)







