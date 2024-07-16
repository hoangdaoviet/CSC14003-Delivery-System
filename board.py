class Board:
    def __init__(self, filename):
        try:
            f = open(filename, 'r')
        except FileNotFoundError:
            print('File not found')
            exit()

        self.n, self.m, self.t, self.f = map(int, f.readline().split())
        self.board = [list(f.readline().strip()) for _ in range(self.n)]
        f.close()

        self.index, self.level = self.extractInformation(filename)

    def extractInformation(self, filename):
        index_, buffer = filename.split('_')
        level_, _ = buffer.split('.')
        index = int(index_[5:])
        level = int(level_[5:])
        return index, level