from agent import *

board = Board("input1_level1.txt")

res = PlayerLvl1().AStar(board)

print(res)