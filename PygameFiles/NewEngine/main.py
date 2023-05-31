
# importing game
from MainMenu.game import Game

# making an instance of game class
g = Game()

# until the game runs, display the menu on screen and loop the game
while g.running:  
    g.curr_menu.display_menu()
    g.game_loop()




