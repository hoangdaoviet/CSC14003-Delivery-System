from agent import *

board = Board('input1_level3.txt')
agent = PlayerLvl3(board.t, board.f)
path = agent.move(board)
# path, search_board = agent.move(board)
print(path)
# for line in search_board:
#     print(line)