from board import *
from queue import PriorityQueue

class PlayerLvl1:
    def __init__(self):
        pass

    def BFS(self, board):
        """
        input: board: list(list()), a 2D list representing the map
        output: result: list((x, y)), a list of strings representing the moves on the coordinate
        delete pass statement before implementing
        """
        pass

    def DFS(self, board):
        """
        input: board: list(list()), a 2D list representing the map
        output: result: list((x, y)), a list of strings representing the moves on the coordinate
        delete pass statement before implementing
        """
        pass

    @staticmethod
    def UCS(board: Board):
        """
        input: board: list(list()), a 2D list representing the map
        output: result: list((x, y)), a list of strings representing the moves on the coordinate
        delete pass statement before implementing
        """
        start = board.findStart()
        current_node = Node(start[0], start[1], None, 0)
        frontier = PriorityQueue()
        frontier.put((current_node.cost, current_node))
        reached = {start: current_node}

        x_movement = [1, -1, 0, 0]
        y_movement = [0, 0, -1, 1]

        while not frontier.empty():
            current_node = frontier.get()[1]

            if board.board[current_node.x][current_node.y] == 'G':
                break

            for i in range(4):
                x = current_node.x + x_movement[i]
                y = current_node.y + y_movement[i]

                if board.isValid(x, y):
                    new_node = Node(x, y, current_node, current_node.cost + 1)

                    if (x, y) not in reached or new_node.cost < reached[(x, y)].cost:
                        reached[(x, y)] = new_node
                        frontier.put((new_node.cost, new_node))

        result = []
        while current_node:
            result.append((current_node.x, current_node.y))
            current_node = current_node.parent
        return result[::-1]

    def GBFS(self, board):
        """
        input: board: list(list()), a 2D list representing the map
        output: result: list((x, y)), a list of strings representing the moves on the coordinate
        delete pass statement before implementing
        """
        pass
    
    @staticmethod
    def AStar(board: Board):
        goal = board.findEnd()

        def h(node):
            return abs(node.x - goal[0]) + abs(node.y - goal[1])
        
        start = board.findStart()
        current_node = Node(start[0], start[1], None, 0)
        frontier = PriorityQueue()
        frontier.put((current_node.cost + h(current_node), current_node))
        reached = {start: current_node}

        x_movement = [1, -1, 0, 0]
        y_movement = [0, 0, -1, 1]

        while not frontier.empty():
            current_node = frontier.get()[1]

            if board.board[current_node.x][current_node.y] == 'G':
                break

            for i in range(4):
                x = current_node.x + x_movement[i]
                y = current_node.y + y_movement[i]

                if board.isValid(x, y):
                    new_node = Node(x, y, current_node, current_node.cost + 1)

                    if (x, y) not in reached or new_node.cost < reached[(x, y)].cost:
                        reached[(x, y)] = new_node
                        frontier.put((new_node.cost + h(new_node), new_node))

        result = []
        while current_node:
            result.append((current_node.x, current_node.y))
            current_node = current_node.parent
        return result[::-1]

class PlayerLvl2:
    def __init__(self, timeAllowed):
        self.timeAllowed = timeAllowed

    def move(self, board):
        """
        input: list(list()), a 2D list representing the map
        output: list((x, y)), a list of strings representing the moves on the coordinate
        """
        return []

class PlayerLvl3:
    def __init__(self, timeAllowed, fuelCapacity):
        self.timeAllowed = timeAllowed
        self.fuelCapacity = fuelCapacity
    
    def move(self, board):
        """
        input: list(list()), a 2D list representing the map
        output: list((x, y)), a list of strings representing the moves on the coordinate
        """
        return []