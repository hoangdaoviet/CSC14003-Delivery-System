from agent import *

board = Board('input1_level1.txt')
agent = PlayerLvl1()
path = agent.UCS(board)
# path, search_board = agent.move(board)
print(path)
# for line in search_board:
#     print(line)