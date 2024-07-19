from agent import *

board = Board("input0_level2.txt")

res = PlayerLvl2(board.t).move(board)

print(res)