class Board:
    def __init__(self, filename):
        try:
            f = open(filename, 'r')
        except FileNotFoundError:
            print('File not found')
            exit()

        self.n, self.m, self.t, self.f = map(int, f.readline().split())
        self.board = [list(map(str, f.readline().split())) for _ in range(self.n)]
        f.close()

        self.index, self.level = self.extractInformation(filename)
        self.start = self.findStart()
        self.end = self.findEnd()

    def extractInformation(self, filename):
        index_, buffer = filename.split('_')
        level_, _ = buffer.split('.')
        index = int(index_[5:])
        level = int(level_[5:])
        return index, level
    
    def findStart(self):
        for i in range(self.n):
            for j in range(self.m):
                if self.board[i][j] == 'S':
                    return (i, j)
        return None
    
    def findEnd(self):
        for i in range(self.n):
            for j in range(self.m):
                if self.board[i][j] == 'G':
                    return (i, j)
        return None
    
class Node:
    __slots__ = ['x', 'y', 'parent', 'cost', 'time', 'fuel']
    def __init__(self, x, y, parent=None, cost=0, time=0, fuel=0):
        self.x = x
        self.y = y
        self.parent = parent
        self.cost = cost
        self.time = time
        self.fuel = fuel

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.cost < other.cost

    def __hash__(self):
        return hash((self.x, self.y))