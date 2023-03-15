from tkinter.tix import ROW
import Piece

class Tile:
    """
    A class used to represents a tile on the Onitama board
    ...

    Attributes

    Boolean isSenseiChair: True if tile contains Sensei Chair
    Piece piece: piece located on this tile
    Integer row, col

    ----------
    Methods
    -------

    """

    #Attributes

    isSenseiChair = False
    piece=None
    row=None
    col=None

    #Methods