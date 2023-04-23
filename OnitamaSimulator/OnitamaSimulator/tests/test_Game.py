import os, sys
import unittest
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
sys.path.append( parentdir+ '\\GameEngine')
from Game import Game
from Card import Card

class testGame(unittest.TestCase):


    def test_Constructor(self):
        pass

    
    def test_startGame(self):
        pass


    def test_handOutCards(self):
        game = Game()
        ## Assert that 
        self.assertNotEqual(game.player1.cards, [])
        self.assertNotEqual(game.player2.cards, [])
        self.assertIsNotNone(game.neutralCard)

        ## Assert that each card is unique
        for card in game.player1.cards:
            self.assertNotIn(card, game.player2.cards)
            self.assertNotEqual(card, game.neutralCard)
        for card in game.player2.cards:
            self.assertNotIn(card, game.player1.cards)
            self.assertNotEqual(card, game.neutralCard)

        self.assertNotEqual(game.player1.cards[0], game.player1.cards[1])
        self.assertNotEqual(game.player2.cards[0], game.player2.cards[1])
        

    def test_fetchSelectedCard(self):
        game = Game()
        player1Cards = game.player1.cards
        self.assertEqual(game.fetchSelectedCard(game.player1, 0), player1Cards[0])
        self.assertEqual(game.fetchSelectedCard(game.player1, 1), player1Cards[1])

    
        player2Cards = game.player2.cards
        self.assertEqual(game.fetchSelectedCard(game.player2, 0), player2Cards[0])
        self.assertEqual(game.fetchSelectedCard(game.player2, 1), player2Cards[1])



    def test_fetchSelectedPiece(self):
        game = Game()
        pieces = game.player1.pieces
        for piece in pieces:
            self.assertEqual(piece, game.fetchSelectedPiece(game.player1, [piece.row, piece.col]))

        
        pieces = game.player2.pieces
        for piece in pieces:
            self.assertEqual(piece, game.fetchSelectedPiece(game.player2, [piece.row, piece.col]))


    def test_deletePiece(self):
        game = Game()
        pieces = game.player1.pieces
        for piece in pieces:
            game.deletePiece(piece)
            self.assertNotIn(piece, pieces)

        pieces = game.player2.pieces
        for piece in pieces:
            game.deletePiece(piece)
            self.assertNotIn(piece, pieces)
        
    
    def test_WinCon(self):
        pass

    
    def test_getGameState(self):
        game = Game()
        self.assertEqual(game.gameStates[-1], game.getGameState(game))


    def test_returnToPreviousGameState(self):
        pass


if __name__ =='__main__':
      
      unittest.main()
