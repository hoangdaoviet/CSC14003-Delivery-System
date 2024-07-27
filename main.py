from agent import *

board = Board('input0_level4.txt')
agent = PlayerLvl4(board.t, board.f)
path, _ = agent.move(board)
print(path)