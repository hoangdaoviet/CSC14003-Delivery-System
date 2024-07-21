from agent import *

board = Board('input0_level2.txt')
agent = PlayerLvl1()
path = agent.BFS(board)