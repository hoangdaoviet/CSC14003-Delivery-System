from agent import *

board = Board("input1_level1.txt")

res = PlayerLvl1().DFS(board)

print(res)