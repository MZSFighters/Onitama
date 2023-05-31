import pygame
from Constants import *

from Tile import Tile

class Board:

    """
    A class used to represents the Onitama Board
    ...
    
    ----------
    Attributes

    arr (Tile) - An array which contains tiles with values such as 0 for no piece on the tile and 1 for a piece present on the tile

    ----------
    Methods
    -------
    
    printBoard(): prints/draws the current state of the board as a 5 by 5 grid/matrix whenever the method is called upon.
                  
    
    returnTile(i,j): Return the tile located at position (i,j)
    """

    def __init__(self, player1, player2) -> None:
        
        array = [[0, 0, 0, 0, 0] ,[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]   
        # Initiate Array to be 2d array of empty tiles

        for i in range(ROWS):
            for j in range(COLS):
                array[i][j] = Tile(None, i, j)

        for playerPiece in player1.pieces:
            array[playerPiece.row][playerPiece.col].piece = playerPiece

        for playerPiece in player2.pieces:
            array[playerPiece.row][playerPiece.col].piece = playerPiece

        self.arr = array


    def returnTile(self, i,j):
        '''Returns the tile at the position i,j on the board'''
        return(self.arr[i][j])


    def printBoard(self, display,curr_board):
        # board image drawn on display screen
        self.display = display
        board_image = pygame.image.load("PygameFiles/NewEngine/images/board_background.jpg")
        board_image = pygame.transform.scale(board_image, (BOARD_WIDTH, BOARD_HEIGHT)).convert_alpha()
        self.display.blit(board_image, (0, 0))

        # drawing pieces on the board
        self.offset = 30
        for row in range(ROWS):
            for col in range(COLS):
                if curr_board.arr[row][col].Value() == 1:

                    if curr_board.arr[row][col].piece.isMaster:
                        
                        #pygame.draw.rect(self.display, RED, (col*SQUARE_SIZE + self.offset, row*SQUARE_SIZE + self.offset, 50,80))
                        red_king = pygame.image.load("PygameFiles/NewEngine/images/red_king.png")
                        red_king = pygame.transform.scale(red_king, (SQUARE_SIZE*1.4, SQUARE_SIZE*1.4)).convert_alpha()
                        self.display.blit(red_king, (col*SQUARE_SIZE ,row*SQUARE_SIZE))
                    else:
                        #pygame.draw.rect(self.display, RED, (col*SQUARE_SIZE + self.offset, row*SQUARE_SIZE + self.offset, 50,50))
                        red_pawn = pygame.image.load("PygameFiles/NewEngine/images/red_pawn.png")
                        red_pawn = pygame.transform.scale(red_pawn, (SQUARE_SIZE, SQUARE_SIZE)).convert_alpha()
                        self.display.blit(red_pawn, (col*SQUARE_SIZE + self.offset,row*SQUARE_SIZE + self.offset))

                elif curr_board.arr[row][col].Value() == 2:
                    
                    if curr_board.arr[row][col].piece.isMaster:
                        #pygame.draw.rect(self.display, BLUE, (col*SQUARE_SIZE + self.offset, row*SQUARE_SIZE + self.offset, 50,80))
                        blue_king = pygame.image.load("PygameFiles/NewEngine/images/blue_king.png")
                        blue_king = pygame.transform.scale(blue_king, (SQUARE_SIZE, SQUARE_SIZE-20)).convert_alpha()
                        self.display.blit(blue_king, (col*SQUARE_SIZE + self.offset,row*SQUARE_SIZE + self.offset+10))
                    else:
                        #pygame.draw.rect(self.display, BLUE, (col*SQUARE_SIZE + self.offset, row*SQUARE_SIZE + self.offset, 50,50))
                        blue_pawn = pygame.image.load("PygameFiles/NewEngine/images/blue_pawn.png")
                        blue_pawn = pygame.transform.scale(blue_pawn, (SQUARE_SIZE, SQUARE_SIZE)).convert_alpha()
                        self.display.blit(blue_pawn, (col*SQUARE_SIZE + self.offset,row*SQUARE_SIZE + self.offset))
                



       
            

