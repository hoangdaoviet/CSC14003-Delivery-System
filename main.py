from agent import *

board = Board('input1_level4.txt')
agent = PlayerLvl4(board.t, board.f)
# path = agent.UCS(board)
path, search_board = agent.move(board)
print(path)
# for line in search_board:
#     print(line)