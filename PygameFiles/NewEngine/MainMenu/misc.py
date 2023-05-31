import pygame
import pygame_gui
from MainMenu.menu import Menu
from MainMenu.constants import *

class HTP(Menu):
    def __init__(self,game):            # constructor
        Menu.__init__(self,game)        # calling Menu constructor -> initialising Menu
        self.startx, self.starty = 20, 50
        self.cursor_rect.midtop = (self.startx, self.starty)

    def display_menu(self):
        self.run_display = True     
        while self.run_display:
            self.game.check_events()    # checking input
            self.check_input()
            
            # reset our canvas and window
            start_image = pygame.image.load("PygameFiles/NewEngine/images/background.jpg")
            start_image = pygame.transform.scale(start_image, (DISPLAY_WIDTH, DISPLAY_HEIGHT))
            self.game.display.blit(start_image, (0,0))
            size = 20               # font size

            

            # Let's draw some text on the screen ..
            self.game.draw_text('HOW TO PLAY', 50, self.startx + self.MID_WEIGHT, self.starty, WHITE, "center")
            self.game.draw_text("Instructions on how to play the Onitama Game Simulator:", 23, self.startx, self.starty+90, WHITE, "left")
            self.game.draw_text("> Onitama is a two-player abstract strategy game.", size, self.startx, self.starty+140, WHITE, "left")
            self.game.draw_text("> The goal is to capture your opponent's master pawn or move your own master pawn onto your opponent's starting space.", size, self.startx, self.starty+200, WHITE, "left")
            self.game.draw_text("> Players take turns moving one of their pawns according to the movement card they have.", size, self.startx, self.starty+260, WHITE, "left")
           
            self.game.draw_text("> There are five movement cards in play each game, two for each player and one neutral card.", size, self.startx, self.starty+320, WHITE, "left")
      
            self.game.draw_text("> Each movement card shows possible moves for any pawn on the board.", size, self.startx, self.starty+380, WHITE, "left")
             
            self.game.draw_text("> A pawn may move any number of spaces in any direction shown on the card, except for invalid moves on the board ", size, self.startx, self.starty+440, WHITE,"left")
           
            self.game.draw_text("> If a pawn lands on a space occupied by an opponent's pawn, that pawn is captured and removed from the board.", size, self.startx, self.starty+500, WHITE, "left")
            
            self.game.draw_text("> If a player cannot make a move on their turn, they lose the game.", size, self.startx, self.starty+560, WHITE, "left")
            self.game.draw_text("> Now that you are an expert at Onitama, Good luck!", size, self.startx, self.starty+620, WHITE, "left")
    
            #self.draw_back()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
        self.run_display = False




            

       




class LoadSavedGame(Menu):
    def __init__(self,game):            # constructor
        Menu.__init__(self,game)        # calling Menu constructor -> initialising Menu
        self.startx, self.starty = self.MID_WEIGHT , 300
        

    def display_menu(self):
        self.run_display = True     
        while self.run_display:
            self.game.check_events()    # checking input
            self.check_input()

            self.draw()               

            

            # Let's draw some text on the screen ..
            self.game.draw_text('This functionality is not available yet...', size, self.startx, self.starty, WHITE, "center")
            
    
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
        self.cursor_rect.midtop = (self.cncx, self.cncy + self.offset)

    def display_menu(self):
        self.run_display = True     
        while self.run_display:
            self.game.check_events()    # checking input
            self.check_input()

            start_image = pygame.image.load("PygameFiles/NewEngine/images/cardbgg.jpg")
            start_image = pygame.transform.scale(start_image, (DISPLAY_WIDTH, DISPLAY_HEIGHT))
            self.game.display.blit(start_image, (0,0))

            self.game.draw_text('CUSTOM CARDS', 50, self.MID_WEIGHT, 115, WHITE, "center")
            self.game.draw_text('Create New Card', size, self.cncx, self.cncy, WHITE, "center")
            self.game.draw_text('Edit Card', size, self.ecx, self.ecy, WHITE, "center")
            self.game.draw_text('Delete Card', size, self.dcx, self.dcy, WHITE, "center")
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "NEW":
                self.cursor_rect.midtop = (self.ecx, self.ecy + self.offset)
                self.state = "EDIT"
            elif self.state == "EDIT":
                self.cursor_rect.midtop = (self.dcx , self.dcy + self.offset)
                self.state = "DELETE"
            elif self.state == "DELETE":
                self.cursor_rect.midtop = (self.cncx , self.cncy + self.offset)
                self.state = "NEW"
        
        elif self.game.UP_KEY:
            if self.state == "NEW":
                self.cursor_rect.midtop = (self.dcx , self.dcy + self.offset)
                self.state = "DELETE"
            elif self.state == "EDIT":
                self.cursor_rect.midtop = (self.cncx , self.cncy + self.offset)
                self.state = "NEW"
            elif self.state == "DELETE":
                self.cursor_rect.midtop = (self.ecx, self.ecy + self.offset)
                self.state = "EDIT"
            
            

    def check_input(self):
        self.move_cursor()
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
        elif self.game.START_KEY:
            if self.state == "NEW":
                self.game.curr_menu = self.game.add_card
        self.run_display = False


class AddCard(Menu):
    def __init__(self,game):            # constructor
        Menu.__init__(self,game) 
              # calling Menu constructor -> initialising Menu
        '''self.state = "NEW"
        self.cncx, self.cncy = self.MID_WEIGHT, self.MID_HEIGHT - 35
        self.ecx, self.ecy = self.MID_WEIGHT, self.MID_HEIGHT + 15
        self.dcx, self.dcy = self.MID_WEIGHT, self.MID_HEIGHT + 65
        self.cursor_rect.midtop = (self.cncx, self.cncy + self.offset)'''

    def display_menu(self):
        self.run_display = True     
        while self.run_display:
            
            self.game.check_events()    # checking input
            self.check_input()
        
            start_image = pygame.image.load("PygameFiles/NewEngine/images/cardbgg.jpg")
            start_image = pygame.transform.scale(start_image, (DISPLAY_WIDTH, DISPLAY_HEIGHT))
            self.game.display.blit(start_image, (0,0))

            self.game.draw_text('ADD CARD', 50, self.MID_WEIGHT, 115, WHITE, "center")
            self.game.draw_text('Card Name:', size, 200, 300, WHITE, "left")
            #self.game.draw_text('Edit Card', size, self.ecx, self.ecy, WHITE, "center")
            #self.game.draw_text('Delete Card', size, self.dcx, self.dcy, WHITE, "center")
            #self.draw_cursor()
           
            self.blit_screen()
            

   
            
            

    def check_input(self):
        
        if self.game.BACK_KEY:
            
            self.game.curr_menu = self.game.customcard_settings
        
        
        
        self.run_display = False



