# test_tictactoe.py
# 
# import code to be tested

from tictactoe import Game

tic = game()

# a smoke test
def test_smoke():
  assert True == True

def test_draw_board():
	assert tic.draw_board == [1, 2, 3, 4, 5, 6, 7, 8, 9]