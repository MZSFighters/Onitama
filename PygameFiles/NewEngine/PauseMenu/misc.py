import pygame
import pygame_gui
from PauseMenu.menu import Menu
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
            self.game.curr_menu = self.game.pause_menu
        self.run_display = False




            

       









