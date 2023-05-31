import pygame
from GamePlay.Player import Player
from GamePlay.Card import Card
from GamePlay.Board import Board
from GamePlay.Constants import *
from PauseMenu.pausemenu import *
from PauseMenu.game import Game as pause
from GamePlay.PillowTalk import *


class Game:
    def __init__(self, gameState="N02000103044240414344NNNNN", gameStates=[], player1Name = "Player1", player2Name = "Player2")->None:
        
        pygame.init()
        self.running, self.playing = True, False
        self.FPS = 60

        Card.makeDeck() # Make The Deck
        self.turnCount=0 #turn count
        self.gameStates=gameStates
        
        # Make the players
        self.player1 =Player(player1Name, True )
        self.player2 =Player(player2Name, False )

        #Give each player their set of pieces
        self.player1.givePieces(gameState[1:11])
        self.player2.givePieces(gameState[11:21] )

        
        Game.handOutCards(self, gameState[21:]) # hand out their cards + neutral card handled as well

        self.board = Board(self.player1, self.player2) #Populate the  board with players' pieces
        self.gameStates.append(self.getGameState(self)) #Initial game state added to list of all game states
        
        self.selectedCard = 0
        self.selectedPiece = 0
        self.clicked = False
        self.list = []

        self.display = pygame.Surface((WIDTH, HEIGHT))
        self.window  = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Onitama Game")

    def game_loop(self):
        clock = pygame.time.Clock()
        while self.playing:
            
            clock.tick(self.FPS)

            # display background on screen
            background = pygame.image.load("PygameFiles/NewEngine/images/background.jpg")
            background = pygame.transform.scale(background, (WIDTHEXCB, HEIGHT)).convert_alpha()
            self.display.blit(background, (WIDTH / 2, 0))

            # turn counter
            if self.turnCount%2==0:
                player, opp = self.player1, self.player2
            else:
                player, opp = self.player2, self.player1

            # checking events -> user input
            self.check_events(player)

            # fetching card names for each card
            self.neutralCardName = (self.neutralCard.name)
            self.p_firstCardName, self.p_secondCardName = player.cards[0].name, player.cards[1].name
            self.opp_firstCardName, self.opp_secondCardName = opp.cards[0].name, opp.cards[1].name
            


            # draw headings and board on screen
            self.draw_text("PLAYER 1 CARDS:", HEADING_TEXTSIZE, 800, 150, RED, "left")
            self.draw_text("PLAYER 2 CARDS:", HEADING_TEXTSIZE, 800, 550,BLUE, "left")
            self.draw_text("NEUTRAL CARD:", HEADING_TEXTSIZE, 800, 350, GREEN, "left")
          
            self.board.printBoard(self.display, self.board)
            
            # highlight piece and when selected by the player 
            if self.selectedCard != 0:
                self.highlightCardSelected(player, self.cardNum )
            if self.selectedPiece != 0:
                row, col = self.currPiece[0], self.currPiece[1]
                self.highlightPieceSelected(row, col)

            # drawing cards on screen
            if player.colour == True:
                self.draw_card(self.display, self.neutralCardName, 800, 390)
                self.draw_card(self.display, self.p_firstCardName, 800, 190)
                self.draw_card(self.display, self.p_secondCardName, 1050, 190)
                self.draw_card(self.display, self.opp_firstCardName, 800, 590)
                self.draw_card(self.display, self.opp_secondCardName, 1050, 590)
            else:
                self.draw_card(self.display, self.neutralCardName, 800, 390)
                self.draw_card(self.display, self.opp_firstCardName, 800, 190)
                self.draw_card(self.display, self.opp_secondCardName, 1050, 190)
                self.draw_card(self.display, self.p_firstCardName, 800, 590)
                self.draw_card(self.display, self.p_secondCardName,  1050, 590)

            
            self.window.blit(self.display, (0,0))

            
            
            # when both card and piece are selected then display the possible moves to the player
            if self.selectedCard != 0 and self.selectedPiece != 0:
                possibleMoves = player.previewMoves(self.selectedCard,self.selectedPiece,self.board)
                self.list = possibleMoves
                self.highlightPossibleMoves(possibleMoves)
                
                if len(possibleMoves) == 0:
                    self.selectedCard == 0
                    self.selectedPiece == 0
                
                
                else:
                    for move in possibleMoves:
                        self.move_row,self.move_col = move[0], move[1]
            
                       
                        if self.clicked == True:
                            # make the move...
                            takePiece = player.MakeMove(self.board, self.selectedPiece,self.curr_row,self.curr_col)
                            if (takePiece != None):
                                self.deletePiece(takePiece)
                            
                            # updating board
                            self.board = Board(self.player1, self.player2)
                            self.board.printBoard(self.display,self.board)

                            # updating the neutral card
                            self.neutralCard, player.cards[player.cards.index(self.selectedCard) ] = self.selectedCard, self.neutralCard
                            
                            # win condition
                            win = self.WinCon()
                            if(win == 1):
                                self.draw_winner_text("Player 1 wins")
                            elif(win == 2):
                                self.draw_winner_text("Player 2 wins")
                            elif(win == 0):
                                pass
                            if(win != 0):
                                print("game over")
                                return
                            
                            # turn change
                            self.turnCount= self.turnCount+1

                            # resetting variables
                            self.selectedCard = 0
                            self.selectedPiece = 0
                            self.clicked = False
                            break
                       
            
            pygame.display.update()


    # Checking input from user
    def check_events(self,player):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mousepos = pygame.mouse.get_pos()

                # Left button clicked
                if event.button == 1:
                    self.mouse_posx, self.mouse_posy = self.mousepos    #mouse position

                    # left clicking on the right hand side of the screen
                    if self.mouse_posx > 750:
                        if player.colour == True:       # player colour is red
                            selectedCardNum = self.getSelectedCardFromUser(self.mousepos,800,150,1050,150)
                            if selectedCardNum != 2:
                                self.cardNum = selectedCardNum
                                self.selectedCard = self.fetchSelectedCard(player,selectedCardNum)
                        else:                           # player colour is blue
                            selectedCardNum = self.getSelectedCardFromUser(self.mousepos,800,550,1050,550)
                            if selectedCardNum != 2:
                                self.cardNum = selectedCardNum
                                self.selectedCard = self.fetchSelectedCard(player,selectedCardNum)
                        
                    # left clciking on the left hand side of the screen
                    elif self.mouse_posx < 750:
                        selectedPieceCoords = self.getSelectedPieceFromUser(self, player, self.mousepos)
                        if selectedPieceCoords != [-1,-1]:
                            self.currPiece = selectedPieceCoords
                            self.selectedPiece = self.fetchSelectedPiece( player, selectedPieceCoords)

                # Right button clicked    
                elif event.button  == 3:
                    self.pos_x,self.pos_y = self.mousepos
                    self.makePossibleMove(self.pos_x, self.pos_y)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    g = pause()

# until the game runs, display the menu on screen and loop the game
                    while g.running:  
                        g.curr_menu.display_menu()
                        g.game_loop()

                    
                    
            
                    
                                
    


    ## Methods for game initialization
    @staticmethod
    def handOutCards(self, cardString):
        '''
        A function which hands out player1's cards, player2's cards and the neutral card \n
        ------------------------------
        Parameters
            cardString: String - specifies desired cards for the game (look at documentation for more detail) \n
        '''

        cards=[Card]*5
        #hand out specified cards first
        for i in range(0 , 5):
            if cardString[i]!= "N":
                cards[i]= Card.selectCard(cardString[i])


        # Now hand out random cards
        for i in range(0 , 5):
            if cardString[i]== "N":
                cards[i]= Card.selectCard(cardString[i])

        self.player1.cards = cards[0:2]
        self.player2.cards = cards[2:4]
        self.neutralCard =cards[-1]

    @staticmethod
    def getSelectedCardFromUser(mouse_pos, x1, y1, x2, y2):
        '''
        Function that returns user input for which card they want to use as an integer
        x1, y1 -> card 1 (x, y) coordinates
        x2, y2 -> card 2 (x, y) coordinates
        '''
        while True:
            pos_x, pos_y = mouse_pos
            
            if(pos_x > x1 and pos_x < x1+card_width and pos_y > y1 and pos_y < y1 + card_height):
                return 0
                
            elif (pos_x > x2 and pos_x < x2+card_width and pos_y > y2 and pos_y < y2 + card_height):
                return 1
            else:
                return 2
            
    @staticmethod
    def fetchSelectedCard(player, val):
        '''
        Function that returns a user's selected card \n
        '''
        return player.cards[val]

    @staticmethod
    def getSelectedPieceFromUser(self, player, mouse_pos):
        '''
        Function that allows a user to select a piece they want to play
        '''
        
        while True:
            self.pos_x, self.pos_y = mouse_pos
            
            
            for piece in player.pieces:
                
                if self.pos_x // SQUARE_SIZE == piece.col and self.pos_y // SQUARE_SIZE == piece.row:
                    
                    return [piece.row, piece.col]
            
            return [-1,-1]
            

    @staticmethod
    def fetchSelectedPiece( player, coords):
        '''
        Function that allows the user to select one of their pawns \n
        -----------
        Parameters \n
        player: Player - the player instance currently selecting a Piece
        '''
        
        for piece in player.pieces:
            if piece.row == coords[0] and piece.col ==coords[1]:
                return piece

    
    def makePossibleMove(self, pos_x, pos_y):
       
        for moves in self.list:

            if ((pos_y//SQUARE_SIZE == moves[0] and pos_x//SQUARE_SIZE == moves[1]) ):
                            
                self.curr_row = moves[0]
                self.curr_col = moves[1]
                           
                self.clicked = True
                break
            else:
                self.clicked = False

    def WinCon(self):
        # need to check if either Sensei is taken, or in arch
        dedSensei = True
        # Player 1 checks
        for player1 in self.player1.pieces:
            if (player1.col == 2 and player1.row == 4):
                print("p1 arch")
                return 1
            if(player1.isMaster == True):
               
                dedSensei = False
                break
        if(dedSensei == True):
            print("p2 take")
            return 2 # player 2 wins
        dedSensei = True
        #player 2
        for player2 in self.player2.pieces:
            if (player2.col == 2 and player2.row == 0):
                print("p2 arch")
                return 2
            if(player2.isMaster == True):
                
                dedSensei = False
                break
        if(dedSensei == True):
            print("p1 take")
            return 1 # player 1 wins
        return 0 


    @staticmethod
    def getGameState(self)-> str:
        '''
        returns the gameState for game as a string \n
        '''
        gameState =""
        #get the turn count
        gameState+=(str(self.turnCount%2))
        
        #next we get the coordinates of the pieces of the players first coordinates of each player's pieces is the master
        players =[self.player1, self.player2]
        for player in players:
            pieceString =["N"]*10
            i=2
            for piece in player.pieces:
                if (piece.isMaster ):
                    pieceString[0] = str(piece.row)
                    pieceString[1]= str(piece.col)
                else:
                    pieceString[i]= str(piece.row)
                    pieceString[i+1] = str(piece.col)
                    i=i+2

            gameState+= ''.join(pieceString)

        # Now we add the card numbers

        for player in players:
            for card in player.cards:
                gameState+= str(Card.Deck.index(card))

        # finally the neutral card
        gameState+= str(Card.Deck.index(self.neutralCard))

        return gameState


    def deletePiece(self, piece):
        '''
        removes piece from the game \n
        ---------
        piece:Piece - piece to be removed from the game \n
        '''
        for player in [self.player1, self.player2]:
            for userPiece in player.pieces:
                if userPiece== piece:
                    player.pieces.remove(userPiece)
                    return


    
    '''

    Drawing methods below:
    -> draw_text: draws text on screen
    -> draw_card: draws the card on screen with the card name and background
    -> draw_winner_text: draws the text on screen when one of the two players wins
    -> highlightCardSelected: highlights the card selected by the player
    -> highlightPieceSelected: highlights the piece selected by the player
    -> highlightPossibleMoves: highlights the possible moves playable with respect to card and piece selected by the player

    '''
    def draw_text(self, text, size, x, y, colour, alignment):
       
        font = pygame.font.SysFont('arialblack',size)
        text_surface = font.render(text, True, colour)
        text_rect = text_surface.get_rect()
        if alignment == "center":
            text_rect.center = (x, y)
        elif alignment == "left":
            text_rect.bottomleft = (x, y)
        self.display.blit(text_surface, text_rect)


    def draw_card(self, display, cardName, x, y):

        #GenerateImage("MainMenu/images/"+cardName+".jpg", cardMoveset)
        #img = pygame.image.load("MainMenu/images/FireandIceCardBackground.jpg")
        img = pygame.image.load("PygameFiles/NewEngine/images/cardbgg.jpg")
        pygame.draw.rect(display, RED,( x, y-35,card_width, card_height))
        img = pygame.transform.scale(img, (card_width,card_height)).convert_alpha()

        grid_img = pygame.image.load("PygameFiles/NewEngine/images/"+cardName+".jpg")
        grid_img = pygame.transform.scale(grid_img, (card_width/2, card_height-57)).convert_alpha()
        self.display.blit(img, (x,y-35))
        self.display.blit(grid_img, (x + card_width / 4, y+10))
        self.draw_text(cardName, 25, x + card_width / 2, y-10, WHITE, "center")

    def draw_winner_text(self,text):

        drawText = Win_font.render(text, 1, WHITE)
        self.window.blit(drawText, (WIDTH/2 - drawText.get_width() /2, HEIGHT / 2 - drawText.get_height() / 2))
        pygame.display.update()
        pygame.time.delay(5000)


    def highlightCardSelected(self,player, cardNum):

        outline = 10
        if player.colour == True:

            if cardNum == 0:
                pygame.draw.rect(self.display, RED, (800,156,card_width+outline, card_height+outline))
                self.window.blit(self.display, (0,0))
            elif cardNum == 1:
                pygame.draw.rect(self.display, RED, (1050,156,card_width+outline, card_height+outline))
                self.window.blit(self.display, (0,0))

        else:

            if cardNum == 0:
                pygame.draw.rect(self.display, BLUE, (800,556,card_width+outline, card_height+outline))
                self.window.blit(self.display, (0,0))
            elif cardNum == 1:
                pygame.draw.rect(self.display, BLUE, (1050,556,card_width+outline, card_height+outline))
                self.window.blit(self.display, (0,0))

    def highlightPieceSelected(self, row, col):
        
        offset = 27
        pygame.draw.rect(self.display, YELLOW, (col * SQUARE_SIZE + offset, row * SQUARE_SIZE + offset, SQUARE_SIZE, 2))
        pygame.draw.rect(self.display, YELLOW, (col * SQUARE_SIZE + offset, row * SQUARE_SIZE + offset, 2, SQUARE_SIZE))
        pygame.draw.rect(self.display, YELLOW, (col * SQUARE_SIZE + offset, row * SQUARE_SIZE + offset + SQUARE_SIZE - 2, SQUARE_SIZE, 2))
        pygame.draw.rect(self.display, YELLOW, (col * SQUARE_SIZE + offset + SQUARE_SIZE - 2, row * SQUARE_SIZE + offset, 2, SQUARE_SIZE))
        self.window.blit(self.display, (0,0))

    def highlightPossibleMoves(self,possibleMoves):
         
         '''
         Highlights the possible moves that are playable
         Input: possibleMoves array
         Output: drawing a small rectangle pointer for each move on board to highlight the possible moves
         '''
         for move in possibleMoves:
            x,y = move[0], move[1]
            row, col = x * SQUARE_SIZE, y * SQUARE_SIZE
            offset = 87
            pygame.draw.rect(self.display, GREEN, (col+offset, row+offset, 20, 20))
            self.window.blit(self.display, (0,0))    

        

