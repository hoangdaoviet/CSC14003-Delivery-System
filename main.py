from agent import *

board = Board('input1_level4.txt')
agent = PlayerLvl4(board.t, board.f)
path = agent.move(board)
print(path)