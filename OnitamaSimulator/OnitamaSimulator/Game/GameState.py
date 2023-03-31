#import Board
#import Piece
#import Tile
import sqlite3
import json


class GameState:

    #"N02000103044240414344NNNNN"

    def __init__(self, tableName, gameString):
        if len(gameString) != 25:
            raise Exception("Invalid game state string : Incorrect length")
        self.gameString = gameString

        if gameString[1:2] == "NN" or gameString[11:12] == "NN": #or ZZ
            raise Exception("Invalid game state string : Sensei piece already dead")

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
