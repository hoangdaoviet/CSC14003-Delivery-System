from agent import *

board = Board('input0_level3.txt')
agent = PlayerLvl3(board.t, board.f)
path = agent.move(board)
print(path)