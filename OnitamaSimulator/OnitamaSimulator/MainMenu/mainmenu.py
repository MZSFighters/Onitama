import pygame
from menu import Menu

# Main Menu which makes use of the Menu template class we created
class MainMenu(Menu):
    def __init__(self,game):            # constructor
        Menu.__init__(self,game)        # calling Menu constructor -> initialising Menu

        # we want our cursor to point at the start option
        self.state ="Start"

        # position coordinates (x,y) for each menu option state   
        self.startx, self.starty = self.MID_WEIGHT , self.MID_HEIGHT -35
        self.lsgx, self.lsgy = self.MID_WEIGHT, self.MID_HEIGHT + 15
        self.htpx, self.htpy = self.MID_WEIGHT, self.MID_HEIGHT + 65
        self.customcardsx, self.customcardsy = self.MID_WEIGHT, self.MID_HEIGHT + 115
        self.leaderboardx, self.leaderboardy = self.MID_WEIGHT, self.MID_HEIGHT + 165
        self.settingsx, self.settingsy = self.MID_WEIGHT, self.MID_HEIGHT + 215
        self.exitx, self.exity = self.MID_WEIGHT, self.MID_HEIGHT + 265

        # starting position for our cursor
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    # displaying menu
    def display_menu(self):
        self.run_display = True     
        while self.run_display:             
            self.game.check_events()    # checking input
            self.check_input()

            # reset our canvas and window
            start_image = pygame.image.load("images/onitama_highres.jpg")
            start_image = pygame.transform.scale(start_image, (700, 650))
            self.game.display.blit(start_image, (0,0))
            size = 40                   # font size


            # Let's draw some text on the screen ..
            self.game.draw_text('Start New Game', size, self.startx, self.starty)
            self.game.draw_text('Load Saved Game', size, self.lsgx, self.lsgy)
            self.game.draw_text('How To Play', size, self.htpx, self.htpy)
            self.game.draw_text('Custom Cards', size, self.customcardsx, self.customcardsy)
            self.game.draw_text('Leaderboard', size, self.leaderboardx, self.leaderboardy)
            self.game.draw_text('Settings', size, self.settingsx, self.settingsy)
            self.game.draw_text('Exit', size, self.exitx, self.exity)
            self.draw_cursor()      # draw cursor on screen
            self.blit_screen()      # put everything on screen

    # defining movement of cursor
    def move_cursor(self):
        # when using the down key -> changing from one state to another
        if self.game.DOWN_KEY:              
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.lsgx + self.offset, self.lsgy)
                self.state = "LSG"
            elif self.state == 'LSG':
                self.cursor_rect.midtop = (self.htpx + self.offset, self.htpy)
                self.state = "HTP"
            elif self.state == "HTP":
                self.cursor_rect.midtop = (self.customcardsx + self.offset, self.customcardsy)
                self.state = "CustomCards"
            elif self.state == "CustomCards":
                self.cursor_rect.midtop = (self.leaderboardx + self.offset, self.leaderboardy)
                self.state = "LeaderBoard"
            elif self.state == "LeaderBoard":
                self.cursor_rect.midtop = (self.settingsx + self.offset, self.settingsy)
                self.state = "Settings"
            elif self.state == "Settings":
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = "Exit"
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Start"

        # when using the up key -> changing from one state to another
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = "Exit"
            elif self.state == 'LSG':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Start"
            elif self.state == "HTP":
                self.cursor_rect.midtop = (self.lsgx + self.offset, self.lsgy)
                self.state = "LSG"
            elif self.state == "CustomCards":
                self.cursor_rect.midtop = (self.htpx + self.offset, self.htpy)
                self.state = "HTP"
            elif self.state == "LeaderBoard":
                self.cursor_rect.midtop = (self.customcardsx + self.offset, self.customcardsy)
                self.state = "CustomCards"
            elif self.state == "Settings":
                self.cursor_rect.midtop = (self.leaderboardx + self.offset, self.leaderboardy)
                self.state = "LeaderBoard"
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.settingsx + self.offset, self.settingsy)
                self.state = "Settings"

    # check input in menu to move from one screen to another
    def check_input(self):
        self.move_cursor()          # player moving cursor
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.curr_menu = self.game.play_settings
            elif self.state == 'LSG':
                self.game.curr_menu = self.game.loadsaved_settings
            elif self.state == 'HTP':
                self.game.curr_menu = self.game.misc
            elif self.state == 'CustomCards':
                self.game.curr_menu = self.game.customcard_settings
            elif self.state == 'LeaderBoard':
                self.game.curr_menu = self.game.highscore_settings
            elif self.state == 'Settings':
                self.game.curr_menu = self.game.settings_menu
            elif self.state == 'Exit':
                # Exit the Game
                self.game.playing, self.game.running, self.run_display = False, False, False

            # so when player selects the start key, it will tell menu to stop displaying     
            self.run_display = False 


class PlayMenu(Menu):
    def __init__(self,game):            # constructor
        Menu.__init__(self,game)        # calling Menu constructor -> initialising Menu
        self.state = "PVAI"
        self.pvax, self.pvay = self.MID_WEIGHT, self.MID_HEIGHT - 35
        self.pvpx, self.pvpy = self.MID_WEIGHT, self.MID_HEIGHT + 15
        
        self.cursor_rect.midtop = (self.pvax + self.offset, self.pvay)

    def display_menu(self):
        self.run_display = True     
        while self.run_display:
            self.game.check_events()    # checking input
            self.check_input()

            # reset our canvas and window
            start_image = pygame.image.load("images/onitama_highres.jpg")
            start_image = pygame.transform.scale(start_image, (700, 650))
            self.game.display.blit(start_image, (0,0))
            size = 40                 # font size

            self.game.draw_text('Player vs AI', size, self.pvax, self.pvay)
            self.game.draw_text('Player vs Player', size, self.pvpx, self.pvpy)
            
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY or self.game.UP_KEY:
            if self.state == 'PVAI':
                self.cursor_rect.midtop = (self.pvpx + self.offset, self.pvpy)
                self.state = "PVP"
            else:
                self.cursor_rect.midtop = (self.pvax + self.offset, self.pvay)
                self.state = "PVAI"
        
    
    def check_input(self):
        self.move_cursor()
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
        self.run_display = False





