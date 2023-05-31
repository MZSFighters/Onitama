import pygame
from PauseMenu.menu import Menu
from MainMenu.constants import *

import sys

# Main Menu which makes use of the Menu template class we created
class PauseMenu(Menu):

    def __init__(self,game):            # constructor
        Menu.__init__(self,game)        # calling Menu constructor -> initialising Menu

        # we want our cursor to point at the start option
        self.state ="Resume Game"

        # position coordinates (x,y) for each menu option state   
        self.resumex, self.resumey = self.MID_WEIGHT , self.MID_HEIGHT -35
        self.htpx, self.htpy = self.MID_WEIGHT, self.MID_HEIGHT + 15
        self.settingsx, self.settingsy = self.MID_WEIGHT, self.MID_HEIGHT + 65
        self.exitx, self.exity = self.MID_WEIGHT, self.MID_HEIGHT + 115
        

        # starting position for our cursor
        self.cursor_rect.midtop = (self.resumex, self.resumey + self.offset)

    # displaying menu
    def display_menu(self):
        self.run_display = True     
        while self.run_display:             
            self.game.check_events()    # checking input
            self.check_input()

            # reset our canvas and window
            self.draw()
            
            
            # Let's draw some text on the screen...
            self.game.draw_text('PAUSE MENU', 50, self.MID_WEIGHT, 150, WHITE, "center")
            self.game.draw_text('Resume Game', size, self.resumex, self.resumey, WHITE, "center")
            self.game.draw_text('How To Play', size, self.htpx, self.htpy, WHITE, "center")
            self.game.draw_text('Settings', size, self.settingsx, self.settingsy, WHITE, "center")
            self.game.draw_text('Exit', size, self.exitx, self.exity, WHITE, "center")
            self.draw_cursor()      # draw cursor on screen
            self.blit_screen()      # put everything on screen

    # defining movement of cursor
    def move_cursor(self):
        
        # when using the down key -> changing from one state to another
        if self.game.DOWN_KEY:              
            if self.state == 'Resume Game':
                self.cursor_rect.midtop = (self.htpx , self.htpy + self.offset)
                self.state = "HTP"
            elif self.state == 'HTP':
                self.cursor_rect.midtop = (self.settingsx, self.settingsy + self.offset)
                self.state = "Settings"
            elif self.state == "Settings":
                self.cursor_rect.midtop = (self.exitx, self.exity + self.offset)
                self.state = "Exit"
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.resumex , self.resumey + self.offset)
                self.state = "Resume Game"

        # when using the up key -> changing from one state to another
        elif self.game.UP_KEY:
            if self.state == 'Resume Game':
                self.cursor_rect.midtop = (self.exitx, self.exity + self.offset)
                self.state = "Exit"
            elif self.state == 'HTP':
                self.cursor_rect.midtop = (self.resumex , self.resumey + self.offset)
                self.state = "Resume Game"
            elif self.state == "Settings":
                self.cursor_rect.midtop = (self.htpx , self.htpy+ self.offset)
                self.state = "HTP"
            elif self.state == "Exit":
                self.cursor_rect.midtop = (self.settingsx , self.settingsy+ self.offset)
                self.state = "Settings"
           


    # check input in menu to move from one screen to another
    def check_input(self):
        self.move_cursor()          # player moving cursor
        if self.game.START_KEY:
            if self.state == 'Resume Game':
                self.game.playing, self.game.running, self.run_display = False, False, False

            elif self.state == 'HTP':
                self.game.curr_menu = self.game.misc
            elif self.state == 'Settings':
                self.game.curr_menu = self.game.settings_menu
            elif self.state == 'Exit':
                # Exit the Game
                #self.game.GamePlaying, self.game.GameRunning, self.game.playing,self.game.running, self.run_display = False,False,False,False,False
                sys.exit()
            # so when player selects the start key, it will tell menu to stop displaying     
            self.run_display = False 


