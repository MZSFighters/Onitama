import pygame
from MainMenu.menu import Menu
from MainMenu.constants import *

class SettingsMenu(Menu):
    def __init__(self,game):            # constructor
        Menu.__init__(self,game)       # calling Menu constructor -> initialising Menu template

        # we want our cursor to point at the AI difficulty option
        self.state = "AI Difficulty"

        # position coordinates (x,y) for each menu option state
        self.aix, self.aiy = self.MID_WEIGHT, self.MID_HEIGHT - 35
        self.soundx, self.soundy = self.MID_WEIGHT, self.MID_HEIGHT + 15
        self.creditsx, self.creditsy =self.MID_WEIGHT, self.MID_HEIGHT + 65
        self.helpx, self.helpy = self.MID_WEIGHT, self.MID_HEIGHT + 115

        # starting position for our cursor
        self.cursor_rect.midtop = (self.aix , self.aiy+ self.offset)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()    # checking input
            self.check_input()

            self.draw()
            self.game.draw_text("SETTINGS", 40, self.MID_WEIGHT, 150, WHITE, "center")
            self.game.draw_text('AI Difficulty', size, self.aix, self.aiy, WHITE, "center")
            self.game.draw_text('Sound', size, self.soundx, self.soundy, WHITE, "center")
            self.game.draw_text('Credits', size, self.creditsx, self.creditsy, WHITE, "center")
            self.game.draw_text('Help', size, self.helpx, self.helpy, WHITE, "center")
            self.draw_cursor()          # draw cursor on screen
            self.blit_screen()          # put everything on screen

    # defining movement of cursor
    def move_cursor(self):
        # when using the down key -> changing from one state to another
        if self.game.DOWN_KEY:              
            if self.state == 'AI Difficulty':
                self.cursor_rect.midtop = (self.soundx, self.soundy + self.offset)
                self.state = "Sound"
            elif self.state == "Sound":
                self.cursor_rect.midtop = (self.creditsx, self.creditsy + self.offset)
                self.state = "Credits"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.helpx , self.helpy + self.offset)
                self.state = "Help"
            elif self.state == 'Help':
                self.cursor_rect.midtop = (self.aix , self.aiy + self.offset)
                self.state = "AI Difficulty"

        # when using the up key -> changing from one state to another
        elif self.game.UP_KEY:
            if self.state == 'AI Difficulty':
                self.cursor_rect.midtop = (self.helpx , self.helpy + self.offset)
                self.state = "Help"
            elif self.state == "Sound":
                self.cursor_rect.midtop = (self.aix , self.aiy+ self.offset)
                self.state = "AI Difficulty"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.soundx, self.soundy+ self.offset)
                self.state = "Sound"
            elif self.state == 'Help':
                self.cursor_rect.midtop = (self.creditsx , self.creditsy+ self.offset)
                self.state = "Credits"





    # check input in menu to move from one screen to another
    def check_input(self):
        self.move_cursor()                       # player moving cursor
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False      
        elif self.game.START_KEY:
            if self.state == 'AI Difficulty':
                self.game.curr_menu = self.game.ai_settings
            elif self.state == 'Sound':
                self.game.curr_menu = self.game.sound_settings
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits_settings
            elif self.state == 'Help':
                self.game.curr_menu = self.game.help_settings
            # so when player selects the start key, it will tell menu to stop displaying     
            self.run_display = False 

class AIDiff(Menu):
    def __init__(self,game):            # constructor
        Menu.__init__(self,game)        # calling Menu constructor -> initialising Menu
        self.state = "Easy"
        self.easyx, self.easyy = self.MID_WEIGHT, self.MID_HEIGHT - 35
        self.mediumx, self.mediumy = self.MID_WEIGHT, self.MID_HEIGHT + 15
        self.hardx, self.hardy = self.MID_WEIGHT, self.MID_HEIGHT + 65
        self.cursor_rect.midtop = (self.easyx , self.easyy + self.offset)

    def display_menu(self):
        self.run_display = True     
        while self.run_display:
            self.game.check_events()    # checking input
            self.check_input()

            # reset our canvas and window
            self.draw()              # font size
            self.game.draw_text("AI DIFFICULTY", 40, self.MID_WEIGHT, 150, WHITE, "center")
            self.game.draw_text('Easy', size, self.easyx, self.easyy, WHITE, "center")
            self.game.draw_text('Medium', size, self.mediumx, self.mediumy, WHITE, "center")
            self.game.draw_text('Hard', size, self.hardx, self.hardy, WHITE, "center")
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "Easy":
                self.cursor_rect.midtop = (self.mediumx , self.mediumy + self.offset)
                self.state = "Medium"
            elif self.state == "Medium":
                self.cursor_rect.midtop = (self.hardx , self.hardy+ self.offset)
                self.state = "Hard"
            elif self.state == "Hard":
                self.cursor_rect.midtop = (self.easyx, self.easyy+ self.offset)
                self.state = "Easy"
        
        elif self.game.UP_KEY:
            if self.state == "Easy":
                self.cursor_rect.midtop = (self.hardx , self.hardy+ self.offset)
                self.state = "Hard"
            elif self.state == "Medium":
                self.cursor_rect.midtop = (self.easyx , self.easyy+ self.offset)
                self.state = "Easy"
            elif self.state == "Hard":
                self.cursor_rect.midtop = (self.mediumx , self.mediumy + self.offset)
                self.state = "Medium"
            
            

    def check_input(self):
        self.move_cursor()
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.settings_menu
        self.run_display = False

class Sound(Menu):
    def __init__(self,game):            # constructor
        Menu.__init__(self,game)        # calling Menu constructor -> initialising Menu
        self.state = "On"
        self.onx, self.ony = self.MID_WEIGHT, self.MID_HEIGHT - 35
        self.offx, self.offy = self.MID_WEIGHT, self.MID_HEIGHT + 15
        
        self.cursor_rect.midtop = (self.onx, self.ony + self.offset)

    def display_menu(self):
        self.run_display = True     
        while self.run_display:
            self.game.check_events()    # checking input
            self.check_input()

            self.draw()
            self.game.draw_text("SOUND SETTINGS", 40, self.MID_WEIGHT, 150, WHITE, "center")
            self.game.draw_text('On', size, self.onx, self.ony, WHITE, "center")
            self.game.draw_text('Off', size, self.offx, self.offy, WHITE, "center")
            
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY or self.game.UP_KEY:
            if self.state == 'On':
                self.cursor_rect.midtop = (self.offx , self.offy + self.offset)
                self.state = "Off"
            else:
                self.cursor_rect.midtop = (self.onx, self.ony + self.offset)
                self.state = "On"
        
    
    def check_input(self):
        self.move_cursor()
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.settings_menu
        if self.game.START_KEY:
            if self.state == 'On':
                self.game.mix.music.play()
            else:
                self.game.mix.music.stop()
        self.run_display = False

class Credits(Menu):
    def __init__(self,game):            # constructor
        Menu.__init__(self,game)        # calling Menu constructor -> initialising Menu
        self.startx, self.starty = 350 , 300
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True     
        while self.run_display:
            self.game.check_events()    # checking input
            self.check_input()

            self.draw()

            
            self.game.draw_text("CREDITS", 40, self.MID_WEIGHT, 150, WHITE, "center")
            # Let's draw some text on the screen ..
            self.game.draw_text('Made By Us', size, self.startx, self.starty, WHITE, "center")
            
    
            #self.draw_back()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.settings_menu
        self.run_display = False

class Help(Menu):
    def __init__(self,game):            # constructor
        Menu.__init__(self,game)        # calling Menu constructor -> initialising Menu
        self.startx, self.starty = 350, 300
        

    def display_menu(self):
        self.run_display = True     
        while self.run_display:
            self.game.check_events()    # checking input
            self.check_input()

            self.draw()
            self.game.draw_text("HELP", 40, self.MID_WEIGHT, 150, WHITE, "center")
            

            # Let's draw some text on the screen ..
            self.game.draw_text('Help!!!', size, self.startx, self.starty, WHITE, "center")
            
    
            #self.draw_back()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.settings_menu
        self.run_display = False






