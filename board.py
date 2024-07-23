class Board:
    def __init__(self, filename):
        try:
            with open(filename, 'r') as f:
                self.n, self.m, self.t, self.f = map(int, f.readline().split())
                self.board = [list(map(str, f.readline().split())) for _ in range(self.n)]
        except FileNotFoundError:
            print('File not found')
            exit()

        self.index, self.level = self.extractInformation(filename)
        for i in range(self.n):
            for j in range(self.m):
                if self.board[i][j] == 'G':
                    self.end = (i, j)
                if self.board[i][j] == 'S':
                    self.start = (i, j)

    def extractInformation(self, filename):
        index_, buffer = filename.split('_')
        level_, _ = buffer.split('.')
        index = int(index_[5:])
        level = int(level_[5:])
        return index, level
    
    def isValid(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.m and self.board[x][y] != '-1'
    
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
        if not isinstance(other, Node):
            return False
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.cost < other.cost

    def __hash__(self):
        return hash((self.x, self.y))
    
    def isCycle(self, node):
        while node is not None:
            if node == self:
                return True
            node = node.parent
        return False