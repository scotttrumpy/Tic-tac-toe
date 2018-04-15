#import code to be tested
from tictactoe import Game

g = Game()

# A smoke test
def test_smoke():
	assert True == True

#test to see if board is drawn
def test_board():
	assert Game.draw_board == "[1, 2, 3, 4, 5, 6, 7, 8, 9]"