#import Board
#import Piece
#import Tile
import sqlite3
import json


class GameState:
    
    """
    A class used to store a game state during the onitama game
    ...
    
    Attributes : 
    
    -tableName : a string that is used as the table name when creating and referring to a desired table
    -gameString : a string that represents the game (i.e. positions of pieces, position
                    of sensei, cards present, cards allocated)
    
    ------
    Methods:
    ------
    
    - createDatabase() : creates the database that will store the tables containing the game states for individual games. (If database exists locally
                                , then the database will not be created again. Instead a connection with the database is established in order to send 
                                queries to the database)
    - createTable() : creates a new table in the database for a new game
    - saveGame() : saves the current gameString to the respective table to be saved in the database. updateGameString is string passed to the method,
                        representing the game at that turn
    - fetchGame() : fetches a gameString from the respective table in the database. turn is an integer value representing the turn number. It is
                        used to query a row in the table that has the desired gameString
    
    
    """

    #"N02000103044240414344NNNNN" : example of gameString

    def __init__(self, tableName, gameString):
        if len(gameString) != 25:
            raise Exception("Invalid game state string : Incorrect length")
        self.gameString = gameString

        if gameString[1:2] == "NN" or gameString[11:12] == "NN": #or ZZ
            raise Exception("Invalid game state string : Sensei piece already captured")

        self.gameString = gameString
        self.tableName = tableName
        

    def createDatabase(self): 
        
        conn = sqlite3.connect('OnitamaSimulator.db')

        cursor = conn.cursor()

        conn.commit()
        conn.close()

        
    def createTable(self):
        thisTableName = str(self.tableName)
        conn = sqlite3.connect('OnitamaSimulator.db')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS " + thisTableName + "(GameString TEXT)")

        conn.commit()
        conn.close()

    def saveGame(self, updateGameString):
        thisTableName = str(self.tableName)
        conn = sqlite3.connect('OnitamaSimulator.db')
        cursor = conn.cursor()

        jsonList = json.dumps(updateGameString)

        cursor.execute("INSERT INTO " + thisTableName + " VALUES(?)" ,(jsonList,))

        conn.commit()
        conn.close()
    
    def fetchGame(self, turn):

        conn = sqlite3.connect('OnitamaSimulator.db')
        cursor = conn.cursor()
        thisTableName = str(self.tableName)
        turn = str(turn)
        cursor.execute("SELECT * FROM " + thisTableName + " WHERE rowid=" + turn)
        collect = cursor.fetchone()
        process = collect[0]
        fetchedGameString = json.loads(process)

        conn.commit()
        conn.close()

        return fetchedGameString
