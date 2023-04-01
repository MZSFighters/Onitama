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
    
    -playersNames : a string that is used as a value in a row in the GameTable. Can link a players name with 
                        with a login in the future. This is mainly used to identify games.
    -gameStringsArr : an array that represents the entire game (i.e. positions of pieces, position
                    of sensei, cards present, cards allocated, AND each game state (turn) in the game)
    
    ------
    Methods:
    ------
    
    - createDatabase() : creates the database that will store the table containing the games (and states) for individual games. 
                            (If database exists locally, then the database will not be created again. Instead a connection with
                             the database is established in order to send queries to the database)
    - createTable() : creates our table in the database that will store all games played
    - saveGame() : saves the current gameStringsArr (array with all gameStates stored) to the GameTable table to be saved in the database.
    - fetchGame() : fetches a gameStringArr from the respective table in the database. gameNo is an integer value representing the game number
                        if one/two players have multiple games together. (Currently returns 
                        what is says but can make a better use of this feature in next sprint. Will fix properly in next sprint)
    
    
    """

    #"N02000103044240414344NNNNN" : example of gameString

    """
    UPDATE: No longer using strings. Now inserting whole array representing array into table.
            fixes issue with multiple games between two people.

            Now only need a single table to store everyones games! 
    
    """

    def __init__(self, playersNames, gameStringsArr):

        """
        Note : will implement proper checks at later time. These can be ignored for now.

        """

        if len(gameString) != 25:
            raise Exception("Invalid game state string : Incorrect length")
        self.gameString = gameString

        if gameString[1:3] == "NN" or gameString[11:13] == "NN": #or ZZ
            raise Exception("Invalid game state string : Sensei piece already captured")


        thisTableName = "GamesTable"
        self.gameStringsArr = gameStringsArr
        self.playersNames = playersNames
        self.createDatabase()
        self.createTable()
        self.saveGame(gameStringsArr)


    def createDatabase(self): 
        
        conn = sqlite3.connect('OnitamaSimulator.db')

        cursor = conn.cursor()

        conn.commit()
        conn.close()

        
    def createTable(self):
        #thisTableName = "GamesTable"
        conn = sqlite3.connect('OnitamaSimulator.db')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS " + thisTableName + "(gameStringsArr TEXT, PlayersNames TEXT)")

        conn.commit()
        conn.close()

    def saveGame(self, gameStringsArr):
        conn = sqlite3.connect('OnitamaSimulator.db')
        cursor = conn.cursor()

        jsonList = json.dumps(gameStringsArr)

        cursor.execute("INSERT INTO " + thisTableName + " VALUES(?)" ,(jsonList,))

        conn.commit()
        conn.close()
    
    def fetchGame(self, gameNo): #just an idea atm. gameNo can be an int if a player has played multiple games
        """
        I think in the future this can be some kind of question at the main menu.
        The persons 'name' or other ID can be used to fetch all relevent info from
        the GameTable. etc etc something of the sort.
        
        """

        conn = sqlite3.connect('OnitamaSimulator.db')
        cursor = conn.cursor()

        #cursor = createConnection() will test this at a later time
        
        gameNo = str(gameNo)
        cursor.execute("SELECT * FROM " + thisTableName + " WHERE rowid=" + gameNo)
        collect = cursor.fetchone()
        process = collect[0]
        fetchedGameArray = json.loads(process)

        conn.commit()
        conn.close()

        return fetchedGameArray

    def createConnection(self):
        conn = sqlite3.connect('OnitamaSimulator.db')
        cursor = conn.cursor()
        return cursor

    def closeConnection(self):
        conn.commit()
        conn.close()