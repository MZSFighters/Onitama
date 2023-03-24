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


Please note i'll put some descriptions to the methods just underneath the method declaration

Also note, This class is quite rough, (in the literal and figurative sense). The implementations of the methods
and or addition/removal of other methods canbe discussed. 

In terms of the diagram. I would suggest that:
- def createDatabase : database is created once somewhere, either here or in the main program
- def createTable : a table is created in the above diagram once every game
- def saveGame : This should happen once every turn. sends the current board of that turn to the table 
    in the database
- def fetchGame : This is up for decision. can be called once or many times per turn, per game. 

"""

class GameState:


    def __init__(self, Board, turn):
        self.Board = Board
        self.turn = turn

    
    def createDatabase(): 
        
        """
        This creates the database that will save the board at each turn. It should not be created 
        every instance of the class but rather once. So this can be implemented somewhere else.
        
        conn is the connection created between the database and the python syntax.
        
        cursor variable is a simpler way of sending and receiving queries to and from the database and the python syntax.
        (has some of its own built in functions.)
        
        .commit() just saves the changes that are made to the database
        .close() just closes the connection 
        (The above two built in functions are just good practice. Not super important) 
        
        HOWEVER: I think i saw somewhere that there is sql syntax that prevents a database from being made multiple times.
        I will look into this
        
        """
        
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
        
        """
        This method will (in theory) create a new table for every game (table is stored in database above).
        The table will store the turns and corresponding boards of that game.
        
        """

        cursor.execute("""CREATE TABLE GameState1 (

            Board TEXT,
            turn INTEGER,

        )""")

        conn.commit()
        conn.close()

    def saveGame(Board, turn):
        
        """
        This method will (in theory) be called after every turn and save the changes made to the board 
        in that turn. It will send this board info to the table in the database. (These can be called later 
        for future reference etc etc)
        
        To store the board properly in the table without losing any info, The board is sent as a json 
        object (basically just a long string). NOTE: This is done as the table can only accept certain 
        data types in sqlite. Some other database management systems may allow other types wich we can explore
        at a later point.
        
        cursor.execute() -- basically just sends a query to the database. In this method, we are sending 
        the current state of the board in the current turn to be saved in the table in the database. 
        
        """
        

        jsonList = json.dumps(Board)

        cursor.execute("INSERT INTO GameState1 VALUES (?, ?)", (jsonList, turn))

        conn.commit()
        conn.close()
    
    def fetchGame(turn):

        """
        Can discuss how to actually use this feature in the game.
        As of now it just fetches the board at turn = 'x' and 
        returns it
        
        This method will query the databse and select the board corresponding to the turn one wishes to 
        fetch. This could be implemented with a 'back' button or some other feature we can discuss. 
        
        the .fetchone() built in function catches the query that is received from the database. It is however in tuple form.
        so the few following lines just isolates the board that is now a very long string.
        
        json.loads() will return our borad back into a 2d list.
        
        This method will return a 2d list. i.e. the board which we want to fetch or 'go back to'.
    
        """

        cursor.execute("SELECT Board FROM GameState1 where turn=(?)", (turn,))
        collect = cursor.fetchone()
        process = collect[0]
        newBoard = json.loads(process)

        conn.commit()
        conn.close()

        return newBoard
