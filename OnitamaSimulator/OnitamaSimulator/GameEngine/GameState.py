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

    def __init__(self):

        """
        Note : will implement proper checks at later time. These can be ignored for now.

        (Sprint 2 notes)
        Note : Will probably need to create an instance of GameState somewhere early in the program (Maybe main menu,
                right at the start of the game etc.)

                The reasoning for this is on creation of an instance, the tables for the custom cards 
                and the table for the games are created. Allowing a user to create and save a custom card from 
                the main menu. When wanting to save the final game list (List of gameState strings), need to be done 
                only once at the end of the game.

                To do : Put instance and function calls in correct place

        """

        #self.gameStringsArr = gameStringsArr
        self.GameTableName = "GamesTable"
        self.CustCardTableName = "CardsTable"
    
        self.createDatabase()
        self.createTable()
        self.createTableCustCard()
        #self.saveGame(gameStringsArr)

       
    def createDatabase(self): 
        
        conn = sqlite3.connect('OnitamaSimulator.db')

        conn.commit()
        conn.close()

    
    """
    Creation of Tables:
    -------------------
    One table for games

    One table for the custom card

    """

    def createTable(self):
        conn = sqlite3.connect('OnitamaSimulator.db')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS " + self.GameTableName + " (gameStringsArr TEXT)")

        conn.commit()
        conn.close()

    def createTableCustCard(self):
        conn = sqlite3.connect("OnitamaSimulator.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS " + self.CustCardTableName + " (Card TEXT, CardName TEXT)")

        conn.commit()
        conn.close()


    """
    SaveGame and fetchGame (For the gameState)
    -----------------------------------------
    
    """


    def saveGame(self, gameStringsArr):
        conn = sqlite3.connect('OnitamaSimulator.db')
        cursor = conn.cursor()

        jsonList = json.dumps(gameStringsArr)

        cursor.execute("INSERT INTO " + self.GameTableName + " VALUES(?)" ,(jsonList,))

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

        gameNo = str(gameNo)
        cursor.execute("SELECT * FROM " + self.GameTableName + " WHERE rowid=" + gameNo)
        collect = cursor.fetchone()
        process = collect[0]
        fetchedGameArray = json.loads(process)

        conn.commit()
        conn.close()

        return fetchedGameArray
    


    """
    saveCard and fetchCard (For the custom card)
    --------------------------------------------

    """

    def saveCard(self, card):
        conn = sqlite3.connect("OnitamaSimulator.db")
        cursor = conn.cursor()
        cardName = card.name

        cardAsList= [cardName, card.colour, card.moveset]
        jsonListCard = json.dumps(cardAsList)

        cursor.execute("INSERT INTO " + self.CustCardTableName + " VALUES(? , ?)", (cardName, jsonListCard))

        conn.commit()
        conn.close()

    def fetchCards(self): 
        """        
        """

        cards=[]

        conn = sqlite3.connect('OnitamaSimulator.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM " + self.CustCardTableName)
        collect = cursor.fetchall()
        
        for cardDict in collect:
            cards.append(json.loads(cardDict[1] ))


        conn.commit()
        conn.close()

        return cards


    
    def createConnection(self):
        conn = sqlite3.connect('OnitamaSimulator.db')
        cursor = conn.cursor()
        return cursor

    def closeConnection(self):
        conn = sqlite3.connect('OnitamaSimulator.db')
        conn.commit()
        conn.close()

