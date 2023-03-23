import Board
import Piece
import Tile
import sqlite3
import json

"""
Very much still a work in progress. But intend for GameState 
to save the Board at turn 'x' to a database. i.e. should hopefully save 
the print of the board at the begining of the previous turn


need to implement 'turn' somewhere in the main program. My idea was a 
integer counter whitch should hopefully be fine. (Assuming a game does not last
thousands of turns long)


"""

class GameState:


    def __init__(self, Board, turn):
        self.Board = Board
        self.turn = turn

    
    def createDatabase(): 
        conn = sqlite3.connect('GameState.db')

        cursor = conn.cursor()

        conn.commit()
        conn.close()

        
    def createTable(gameNo):
        gameNoStr = str(gameNo)
        #Still need to find a way to 
        #incoporate the game number into 
        #the sqlite syntax to create a new
        #table per game

        cursor.execute("""CREATE TABLE GameState1 (

            Board TEXT,
            turn INTEGER,

        )""")

        conn.commit()
        conn.close()

    def saveGame(Board, turn):

        jsonList = json.dumps(Board)

        cursor.execute("INSERT INTO GameState1 VALUES (?, ?)", (jsonList, turn))

        conn.commit()
        conn.close()
    
    def fetchGame(turn):

        """
        Can discuss how to actually use this feature in the game.
        As of now it just fetches the board at turn = 'x' and 
        returns it
    
        """

        cursor.execute("SELECT Board FROM GameState1 where turn=(?)", (turn,))
        collect = cursor.fetchone()
        process = collect[0]
        newBoard = json.loads(process)

        conn.commit()
        conn.close()

        return newBoard
