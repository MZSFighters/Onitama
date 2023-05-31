import os, sys
import unittest
from unittest import mock

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)

sys.path.append(parentdir)
sys.path.append( parentdir+ '\\GameEngine')
from GameEngine.Game import Game

class testGame(unittest.TestCase):

    def test_Constructor(self):
        pass

    def test_startGame(self):
        game= Game()

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
        
    def test_determineStartingTurn(self):

        game = Game()

        game.determineStartingTurn('0')
        self.assertEqual(game.turnCount,0)

        game.determineStartingTurn('1')
        self.assertEqual(game.turnCount,1)

        game.determineStartingTurn('N')
        self.assertTrue(game.turnCount==1 or game.turnCount== 0)

    def test_AImakeTurn(self):

        game = Game()
        card1= game.player1.cards[0]
        card2= game.player2.cards[0]

        piece1 = game.player1.pieces[0]
        piece2 = game.player2.pieces[0]

        move1 =game.getPossibleMoves(game.player1, card1, piece1, game.board, PRINT=False)[0]
        print(move1)
        move2 =game.getPossibleMoves(game.player2, card2, piece2, game.board, PRINT=False)[0]

        #call AImakeTurn with wrong card and piece
        game.AImakeTurn(game.player1, piece2, card1, move1 ) 
        game.AImakeTurn(game.player1, piece1, card2, move2 )

        # let each player use function with correct cards
        
        game.AImakeTurn(game.player1, piece1, card1, move1 )
        game.AImakeTurn(game.player2, piece2, card2, move2 )

    def test_startGame(self):
        
        with mock.patch.object(Game, '_startGame', return_value =None) as mock_method:
            game= Game()
            game.startGame('0', 'easy', stopLoop=True)

            game= Game()
            game.startGame('0', 'Player2', stopLoop=True)

            mock_method.assert_called()


    @mock.patch('builtins.input', side_effect=['0', '0'])
    def test_PrivatestartGame(self, side_effects):
         
         with mock.patch.object(Game, 'playerMakeTurn', return_value=True) as mock_method:
             
             game= Game()
             game._startGame('0', 'easy', stopLoop=True)

             mock_method.assert_called()


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
        self.assertEqual(game.gameStates[-1], game.getGameState())


    def test_returnToPreviousGameState(self):
        pass

    def test_SaveGame(self):
        pass

if __name__ =='__main__':
      
      unittest.main()
