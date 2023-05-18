from GameEngine.Board import Board
from GameEngine.Player import Player
from GameEngine.Card import Card
from configparser import ConfigParser
import copy
import random

class Game:

    """
    A class used to represent a single Onitama Game
    ...

    Attributes

    Player: player1, player2 
    Board: board 
    Card: neutralCard
    gameStates: Str List - list of current and all previous game states
    turnCount: int - the current turn number for the game
    ----------
    Methods
    -------

    Game(self, gameState, gameStates, player1Name, ppayer2Name): Initiates game by distributing two cards to each player
            (Player.Cards) and neutralCard, gives each player a colour, setups board, and enter while loop that lasts
            until someone wins the game 

    startGame(self, turn): Initializes and begins the gameplay loop

    handOutCards(self, cardString): Distributes cards from deck to players.

    userSelectCard(player): returns the card selected by a player for a turn

    userSelectPiece(self, player): returns the piece selected by player during a turn

    deletePiece(self, piece): Removes the piece specified from the game

    getGameState(self): returns a str of the current game state 

    returnToPreviousGameState(self,i): function that returns the game instance to a previous GameState
    """
    ## Methods for game initialization
    def __init__(self, gameState="N02000103044240414344NNNNN", gameStates=[], player1Name="Player1", player2Name= "Player2") -> None:
        '''
        Constructor for a game instance. \n
        ------------------------------
        Parameters \n

        gameState: str - the gameState we want to create, default value is an initial game \n
        player1Name: str - name of player1 \n
        player2Name: str - name of player 2 \n
        ----------------------------

        '''
        
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
        self.gameStates.append(self.getGameState()) #Initial game state added to list of all game states

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
    
    def determineStartingTurn(self, turn):

        if (turn=='0'):
            self.turnCount=0 
        elif (turn =='1'):
            self.turnCount=1
        else: #select turn in normal way 

            if (self.player1.colour == self.neutralCard.colour):
                    self.turnCount=0
            else:
                self.turnCount=1


### Methods used in game architecture

    def startGame(self, turn:str, player2Name):
        '''A function which either starts a player-controlled game or an AI-controlled game'''

        if (player2Name=="Player2"): # second player is another human player
            self._startGame(turn, self.playerMakeTurn)

        if (player2Name=="easy"):
            self._startGame(turn, self.easy)

    def _startGame(self, turn:str, player2AI)->None:
        """
        Initiates game loop for human player \n
        -------
        Parameters:
        string: turn: '0' if player 1 starts, '1' if player 2 starts 'N' if default starting order
        """
        
        AIs = [self.playerMakeTurn, player2AI]

        self.determineStartingTurn(turn)

        while (True): # while True game is running

            if self.turnCount%2==0:
                    player, opp = self.player1, self.player2
            else:
                    player, opp = self.player2, self.player1

            while (True):

                if player == self.player1:
                    playedTurn =AIs[0](player, opp)
                else:
                    playedTurn= AIs[1](player, opp)

                self.board = Board(self.player1, self.player2)
                self.board.printBoard()

                if (playedTurn==True):
                    break

            #did a player win?
            win = self.WinCon()
            if(win == 1):
                print("Player 1 wins")
            elif(win == 2):
                print("Player 2 wins")
            elif(win == 0):
                pass
            if(win != 0):
                print("game over")
                break
            self.turnCount= self.turnCount+1
            self.gameStates.append(self.getGameState())

    def playerMakeTurn(self, player, opp):

                print("The current board is") # Show the current board
                self.board.printBoard()
                
                print(" The neutral card is") # print neutral cards
                print(self.neutralCard)

                print("The opposition has the following cards") # print the opposition's cards
                print(opp.cards[0], opp.cards[1])

                 #  Ask user which card they want and fetch it
                selectedCardNum = self.getSelectedCardFromUser(self,player)
                selectedCard = self.fetchSelectedCard(player,selectedCardNum)

                selectedPieceCoords = self.getSelectedPieceFromUser(self, player) # let user a chooses a piece
                selectedPiece = self.fetchSelectedPiece( player, selectedPieceCoords)
                
                possibleMoves = self.getPossibleMoves( player, selectedCard,selectedPiece,self.board) # let user see all possible moves

                if (len(possibleMoves)==0): # there are no valid moves, player should reselect piece and card
                    input("No valid moves, press Enter to confirm")
                    return False

                elif (input("Would you like to play one of these moves (yes or no)")=="yes"): # player can decide not to play a move
                    move = self.playerPickMove(possibleMoves)
                    self.makeMove(move[0], move[1], selectedPiece)
                    self.neutralCard, player.cards[player.cards.index(selectedCard) ] = selectedCard, self.neutralCard
                    return True
                
                return False

## Methods used to gather user input
    
    @staticmethod
    def getSelectedCardFromUser(self, player):
        '''
        Function that allows a user to select a card they want to play and returns the selected index of the card \n
        with respect to the list of their own cards.
        '''

        while True:

            print("You have the following cards:")

            for card in player.cards:
                print(card)

            selectedCard = int(input("Which card would you like to use? 0 or 1?"))

            if (selectedCard==0 or selectedCard==1):
                return selectedCard

            else:
                print("Invalid card selection, please try again.")    
        
    @staticmethod
    def fetchSelectedCard(player, val):
        '''
        Function that returns a user's selected card \n
        '''
        return player.cards[val]

    @staticmethod
    def getSelectedPieceFromUser(self, player):
        '''
        Function that allows a user to select a piece they want to play
        '''

        while True:
            self.board.printBoard()
            print("Your pieces are at the following positions")
            for piece in player.pieces:
                print(piece.row, piece.col)

            selectedPiece = input(" Which piece would you like to select?")
            row = int(selectedPiece[0])
            col = int(selectedPiece[2])

            for piece in player.pieces:
                if piece.row == row and piece.col ==col:
                    return [row,col]
            
            print("Invalid coordinates given, please try again")

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

    def fetchSelectedPieceFromPlayerPieces(self, player, i):
        '''
        Function that allows the user to select one of their pawns \n
        -----------
        Parameters \n
        player: Player - the player instance currently selecting a Piece
        '''

        return(player.pieces[i])                          


    ## Core Loop functions

    def playerPickMove(self,possibleMoves:int):
        '''
        Lets the player pick a desired move from a list of all possible moves 
        ----------------
        Parameters
            possibleMoves is the output from previewMoves
        '''
        for move in possibleMoves:
            print(move[0]," ", move[1])

        selectedMove = input(" Which move would you like to select?")
        row = int(selectedMove[0])
        col =int(selectedMove[2])

        return row, col

    def makeMove(self, row, col, pieceFrom):
        """
        Takes in the pawn and the desired location and moves the pawn \n
        to that location
        """
        pieceFrom.row = row
        pieceFrom.col = col

        if (self.board.returnTile(row,col).piece!= None):
            takePiece = self.board.returnTile(row, col).piece
            self.deletePiece(takePiece)
            print("Took piece at tile : ", int(takePiece.row), " ", int(takePiece.col))
            return self.board.returnTile(row,col).piece

    def getPossibleMoves(self,player ,card:Card, piece, board:Board, PRINT= True) -> int:
        """
        A preview of possible moves the player can make
        \n
        Debugs an array where the possible moves are represented by 7s
        \n
        Returns a list of possible moves as 2d co ords
        
        """
        returnArray = [] # the array that returns possible moves that is used by the move function
        debugBoard:int = [[0]*len(board.arr) for i in range(len(board.arr[0]))] # the board that debugs the possible moves
        debugBoard[piece.row][piece.col]=2 
        #converting the board into an array of ints, i think that this should be part of the board code but i dont want to tamper with too many classes at once
        for row in range(5):
            for col in range(5):
                debugBoard[row][col] = board.arr[row][col].Value()
        
        intColor = 2
        if (player.colour):
            intColor = 1
        
        moves = copy.copy(card.moveset)
        for move in moves:
            #Need to flip move based on player, From the moves it looks like we assume we are player 2
            if (player.colour == True):
                calcMoveRow = piece.row + move[0]
                calcMoveCol  = piece.col + move[1]

            elif (player.colour == False):
                calcMoveRow = piece.row - move[0]
                calcMoveCol  = piece.col - move[1]
     

            #Check if the move is within the bounds of the board
            #And check to see if the tile is a friendly piece

            if (((calcMoveRow < 5) and (calcMoveRow >= 0)) and  (calcMoveCol < 5 and calcMoveCol >= 0)):

                if (board.returnTile(calcMoveRow,calcMoveRow).piece==None):
                 
                    debugBoard[calcMoveRow][calcMoveCol]=7
                    returnArray.append([calcMoveRow, calcMoveCol])   
                                     
                elif board.returnTile(calcMoveRow,calcMoveRow).piece.colour != player.colour :

                    debugBoard[calcMoveRow][calcMoveCol]=7
                    returnArray.append([calcMoveRow, calcMoveCol])

        if PRINT==True:
            print("Piece:", piece.row, piece.col)
            print(board.printBoard())
            print(returnArray)

            #Printing board with possible moves
            for row in range(5):
                for col in range(5):
                    print(debugBoard[row][col] , end = ' ')
                print()
            #Return array of possible moves
        return returnArray
    
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
                    # setting row and column to identify the piece object as dead
                    userPiece.row = -1
                    userPiece.col = -1
                    return

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

    ## Utility Functions
    def returnToPreviousGameState(self, i):
        '''
        Allows a user to return to a previous round in their current game \n
        -----
        Parameter
        i: int - how many turns back to go, -1 to restart game \n
        '''

        if (i==-1):
            return Game(self.gameStates[0], [])

        if i>= len(self.gameStates ) :
            print("Can not go back more turns than currently played!" )
            return 
        
        if len(self.gameStates)==1:
            print("This is far back as this game goes!")
            return 
        
        else:
            return Game(self.gameStates[len(self.gameStates)-i-1], self.gameStates[:len(self.gameStates)-i-1])

    def SaveGame(self, GameState,GameName):
        """
        Allows a user to save game state to config file \n
        -----
        Parameter
        GameState: string - GameString with state to be saved \n
        GameName: string - Name of the game to be saved,used to create new section in config file \n
        """
        #create ConfigParser object and read the config file
        config = ConfigParser()
        config.read("save_game_config.ini")

        #add info to be saved to config file
        config.add_section(GameName)
        config.set(GameName,"GameString",GameState)

        with open("save_game_config.ini", "w") as configfile:
            config.write(configfile)

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

    ## AI functions

    def easy(self, player, opp):

        card = self.fetchSelectedCard(player, random.randint(0, len(player.cards)-1))
        piece = self.fetchSelectedPieceFromPlayerPieces(player, random.randint(0, len(player.pieces)-1))
        moves = self.getPossibleMoves(player, card, piece, self.board, False)

        if (len(moves)==0):
            return self.easy(self, player)

        move = moves[random.randint(0, len(moves)-1)]
        self.makeMove(move[0], move[1], piece)
        self.neutralCard, player.cards[player.cards.index(card) ] = card, self.neutralCard
        print("Easy AI makes an incredible move!")
        return True

    def medium(self, player, opp):
        ''' use minimax to make optimal move with depth 3'''
        pass
