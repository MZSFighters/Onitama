import pygame
from menu import Menu

class HTP(Menu):
    def __init__(self,game):            # constructor
        Menu.__init__(self,game)        # calling Menu constructor -> initialising Menu
        self.startx, self.starty = 20 , 50
        self.cursor_rect.midtop = (self.startx, self.starty)

    def display_menu(self):
        self.run_display = True     
        while self.run_display:
            self.game.check_events()    # checking input
            self.check_input()

            # reset our canvas and window
            start_image = pygame.image.load("images/CustomCards.jpg")
            start_image = pygame.transform.scale(start_image, (700, 650))
            self.game.display.blit(start_image, (0,0))
            size = 18                # font size

            

            # Let's draw some text on the screen ..
            self.game.draw_text('HOW TO PLAY', 40, self.startx + 335, self.starty)
            self.game.draw_text("Instructions on how to play the Onitama Game Simulator:", 20, self.startx + 310, self.starty+60)
            self.game.drawleft_text("> Onitama is a two-player abstract strategy game.", size, self.startx, self.starty+110)
            self.game.drawleft_text("> The goal is to capture your opponent's master pawn or move", size, self.startx, self.starty+140)
            self.game.drawleft_text("   your own master pawn onto your opponent's starting space", size, self.startx, self.starty+170)
            self.game.drawleft_text("> Players take turns moving one of their pawns according to the", size, self.startx, self.starty+200)
            self.game.drawleft_text("   movement card they have.", size, self.startx, self.starty + 230)
            self.game.drawleft_text("> There are five movement cards in play each game, two for each", size, self.startx, self.starty+260)
            self.game.drawleft_text("   player and one neutral card.", size, self.startx, self.starty + 290)
            self.game.drawleft_text("> Each movement card shows possible moves for any pawn on the", size, self.startx, self.starty+320)
            self.game.drawleft_text("   board.", size, self.startx, self.starty + 350) 
            self.game.drawleft_text("> A pawn may move any number of spaces in any direction shown ", size, self.startx, self.starty+380)
            self.game.drawleft_text("   on the card, given that making that move lands you outside", size, self.startx, self.starty+410)
            self.game.drawleft_text("  the board or on top of your own pawn.", size, self.startx, self.starty+440)
            self.game.drawleft_text("> If a pawn lands on a space occupied by an opponent's pawn, that", size, self.startx, self.starty+470)
            self.game.drawleft_text("  pawn is captured and removed from the board.", size, self.startx, self.starty+500)
            self.game.drawleft_text("> If a player cannot make a move on their turn, they lose the game.", size, self.startx, self.starty+530)
            self.game.drawleft_text("Good luck!", size, self.startx, self.starty+570)
    
            #self.draw_back()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
        self.run_display = False


class LeaderBoard(Menu):
    def __init__(self,game):            # constructor
        Menu.__init__(self,game)        # calling Menu constructor -> initialising Menu
        self.startx, self.starty = 350 , 50
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True     
        while self.run_display:
            self.game.check_events()    # checking input
            self.check_input()

            # reset our canvas and window
            start_image = pygame.image.load("images/Leaderboard.jpg")
            start_image = pygame.transform.scale(start_image, (700, 650))
            self.game.display.blit(start_image, (0,0))
            size = 40                 # font size

            

            # Let's draw some text on the screen ..
            self.game.draw_text('LEADERBOARD', size, self.startx, self.starty)
            
    
            #self.draw_back()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
        self.run_display = False




class LoadSavedGame(Menu):
    def __init__(self,game):            # constructor
        Menu.__init__(self,game)        # calling Menu constructor -> initialising Menu
        self.startx, self.starty = 350 , 300
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True     
        while self.run_display:
            self.game.check_events()    # checking input
            self.check_input()

            # reset our canvas and window
            start_image = pygame.image.load("images/onitama_highres.jpg")
            start_image = pygame.transform.scale(start_image, (700, 650))
            self.game.display.blit(start_image, (0,0))
            size = 30                 # font size

            

            # Let's draw some text on the screen ..
            self.game.draw_text('This functionality is not available yet...', size, self.startx, self.starty)
            
    
            #self.draw_back()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
        self.run_display = False


class CustomCards(Menu):
    def __init__(self,game):            # constructor
        Menu.__init__(self,game)        # calling Menu constructor -> initialising Menu
        self.state = "NEW"
        self.cncx, self.cncy = self.MID_WEIGHT, self.MID_HEIGHT - 35
        self.ecx, self.ecy = self.MID_WEIGHT, self.MID_HEIGHT + 15
        self.dcx, self.dcy = self.MID_WEIGHT, self.MID_HEIGHT + 65
        self.cursor_rect.midtop = (self.cncx + self.offset, self.cncy)

    def display_menu(self):
        self.run_display = True     
        while self.run_display:
            self.game.check_events()    # checking input
            self.check_input()

            # reset our canvas and window
            start_image = pygame.image.load("images/Onitama_highres.jpg")
            start_image = pygame.transform.scale(start_image, (700, 650))
            self.game.display.blit(start_image, (0,0))
            size = 40              # font size

            self.game.draw_text('Create New Card', size, self.cncx, self.cncy)
            self.game.draw_text('Edit Card', size, self.ecx, self.ecy)
            self.game.draw_text('Delete Card', size, self.dcx, self.dcy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "NEW":
                self.cursor_rect.midtop = (self.ecx + self.offset, self.ecy)
                self.state = "EDIT"
            elif self.state == "EDIT":
                self.cursor_rect.midtop = (self.dcx + self.offset, self.dcy)
                self.state = "DELETE"
            elif self.state == "DELETE":
                self.cursor_rect.midtop = (self.cncx + self.offset, self.cncy)
                self.state = "NEW"
        
        elif self.game.UP_KEY:
            if self.state == "NEW":
                self.cursor_rect.midtop = (self.dcx + self.offset, self.dcy)
                self.state = "DELETE"
            elif self.state == "EDIT":
                self.cursor_rect.midtop = (self.cncx + self.offset, self.cncy)
                self.state = "NEW"
            elif self.state == "DELETE":
                self.cursor_rect.midtop = (self.ecx + self.offset, self.ecy)
                self.state = "EDIT"
            
            

    def check_input(self):
        self.move_cursor()
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
        self.run_display = False

