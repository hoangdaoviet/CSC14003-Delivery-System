from board import *
from queue import PriorityQueue, Queue
from collections import deque
from copy import deepcopy
import time

class PlayerLvl1:
    def BFS(self, board: Board):
        """
        input: board: list(list()), a 2D list representing the map
        output: result: list((x, y)), a list of strings representing the moves on the coordinate
        delete pass statement before implementing
        """
        goal = board.end
        start = board.start
        x_movement = [1, -1, 0, 0]
        y_movement = [0, 0, -1, 1]
        reached = {start}
        
        current_node = Node(start[0], start[1])
        frontier = deque([current_node])
        if current_node.x == goal[0] and current_node.y == goal[1]:
            return [start]
        
        while frontier:
            current_node = frontier.popleft()            
            check = False
            for i in range(4):
                x = current_node.x + x_movement[i]
                y = current_node.y + y_movement[i]
                if board.isValid(x, y) and (x, y) not in reached:
                    if x == goal[0] and y == goal[1]:
                        current_node = Node(x, y, current_node)
                        check = True
                        break
                    new_node = Node(x, y, current_node)
                    frontier.append(new_node)
                    reached.add((x, y))
            if check:
                break
        if check == False:
            return -1          
        result = []
        while current_node:
            result.append((current_node.x, current_node.y))
            current_node = current_node.parent
        return {'S': result[::-1]}

    def isCycle(self, node: Node):
        current = node.parent
        while current is not None:
            if current.x == node.x and current.y == node.y:
                return True
            current = current.parent
        return False

    def DFS(self, board):
        """
        input: board: list(list()), a 2D list representing the map
        output: result: list((x, y)), a list of strings representing the moves on the coordinate
        delete pass statement before implementing
        """
        goal = board.end
        start = board.start
        current_node = Node(start[0], start[1], None, 0)
        stack = [current_node]
        reached = {start: current_node}
        if current_node.x == goal[0] and current_node.y == goal[1]:
            return [start]
        x_movement = [1, -1, 0, 0]
        y_movement = [0, 0, -1, 1]

        while stack:
            current_node = stack.pop()
            check = False
            for i in range(4):
                x = current_node.x + x_movement[i]
                y = current_node.y + y_movement[i]
                if board.isValid(x, y) and (x, y) not in reached:
                    if x == goal[0] and y == goal[1]:
                        current_node = Node(x, y, current_node)
                        check = True
                        break
                    new_node = Node(x, y, current_node)
                
                    if not self.isCycle(new_node):
                        stack.append(new_node)
                        reached[(x, y)] = new_node
            if check:
                break
        if check == False:
            return -1
        result = []
        while current_node:
            result.append((current_node.x, current_node.y))
            current_node = current_node.parent
        return {'S': result[::-1]}
    
    def UCS(self, board: Board):
        """
        input: board: list(list()), a 2D list representing the map
        output: result: list((x, y)), a list of strings representing the moves on the coordinate
        delete pass statement before implementing
        """
        start = board.start
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

        if frontier.empty():
            return -1

        result = []
        while current_node:
            result.append((current_node.x, current_node.y))
            current_node = current_node.parent
        return {'S': result[::-1]}

    def GBFS(self, board):
        """
        input: board: list(list()), a 2D list representing the map
        output: result: list((x, y)), a list of strings representing the moves on the coordinate
        delete pass statement before implementing
        """
        def h(node):
            return abs(node.x - goal[0]) + abs(node.y - goal[1])
        
        goal = board.end
        start = board.start
        x_movement = [1, -1, 0, 0]
        y_movement = [0, 0, -1, 1]
        reached = {start}
        
        current_node = Node(start[0], start[1])
        frontier = PriorityQueue()
        frontier.put(( h(current_node), current_node))
        if current_node.x == goal[0] and current_node.y == goal[1]:
            return [start]
        
        while frontier:
            priority, current_node = frontier.get()
            check = False
            for i in range(4):
                x = current_node.x + x_movement[i]
                y = current_node.y + y_movement[i]
                if board.isValid(x, y) and (x, y) not in reached :
                    if x == goal[0] and y == goal[1]:
                        current_node =  Node(x, y, current_node)
                        check = True
                        break
                    new_node = Node(x, y, current_node)
                    frontier.put(( h(new_node), new_node))
                    reached.add((x, y))
            if check:
                break

        if check == False:
            return -1
        
        result = []
        while current_node:
            result.append((current_node.x, current_node.y))
            current_node = current_node.parent
        return {'S': result[::-1]}
    
    def AStar(self, board: Board):
        goal = board.end

        def h(node):
            return abs(node.x - goal[0]) + abs(node.y - goal[1])
        
        start = board.start
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

        if frontier.empty():
            return -1

        result = []
        while current_node:
            result.append((current_node.x, current_node.y))
            current_node = current_node.parent
        return {'S': result[::-1]}

class PlayerLvl2:
    def __init__(self, timeAllowed):
        self.timeAllowed = timeAllowed

    def __get_children(self, board, node):
        x_movement, y_movement = [1, -1, 0, 0], [0, 0, -1, 1]
        children = []

        for i in range(4):
            x = node.x + x_movement[i]
            y = node.y + y_movement[i]

            if board.isValid(x, y):
                new_cost = node.cost + 1
                new_time = node.time + (1 if board.board[x][y] in ['0', 'S', 'G'] else int(board.board[x][y]))

                new_node = Node(x, y, node, cost=new_cost, time=new_time)
                children.append(new_node)

        return children

    def __recursive_DLS(self, board, node, limit):
        if board.board[node.x][node.y] == 'G':
            return node
        elif limit == 0:
            return 0
        else:
            cutoff_occurred = False
            for child in self.__get_children(board, node):
                if child.time > self.timeAllowed or child.isCycle(node):
                    continue
                result = self.__recursive_DLS(board, child, limit - 1)
                if result == 0:
                    cutoff_occurred = True
                elif result != -1:
                    return result
            if cutoff_occurred:
                return 0
            return -1

    def move(self, board):
        """
        input: list(list()), a 2D list representing the map
        output: list((x, y)), a list of strings representing the moves on the coordinate
        """
        """
        idea: IDS with time limit; if the time is up, do not let it get into the queue
        """
        start = board.start
        current_node = Node(start[0], start[1], None, 0, 0)
        limit = 1

        while True:
            res_node = self.__recursive_DLS(board, current_node, limit)
            if res_node == -1:
                return -1
            if res_node == 0:
                limit += 1
            else:
                break

        result = []
        while res_node:
            result.append((res_node.x, res_node.y))

            for _ in range(int(board.board[res_node.x][res_node.y][1:]) if board.board[res_node.x][res_node.y][0] == 'F'
                                                                        else int(board.board[res_node.x][res_node.y])
                                                                        if board.board[res_node.x][res_node.y] not in ['S', 'G']
                                                                        else 0):
                result.append((res_node.x, res_node.y))

            res_node = res_node.parent
        return {'S': result[::-1]}

class PlayerLvl3:
    def __init__(self, timeAllowed, fuelCapacity):
        self.timeAllowed = timeAllowed
        self.fuelCapacity = fuelCapacity

    def __get_children(self, board, node):
        if node.fuel == 0:
            return []

        x_movement, y_movement = [0, 1, 0, -1], [1, 0, -1, 0]
        children = []

        for i in range(4):
            x = node.x + x_movement[i]
            y = node.y + y_movement[i]

            if board.isValid(x, y):
                cell = board.board[x][y]
                new_cost = node.cost + 1
                new_time = node.time + (1 if cell in ['0', 'S', 'G'] else (int(cell[1:]) + 1) if cell[0] == 'F' else int(cell))
                new_fuel = (node.fuel - 1) if cell[0] != 'F' else self.fuelCapacity

                new_node = Node(x, y, node, cost=new_cost, time=new_time, fuel=new_fuel)
                children.append(new_node)

        return children

    def __recursive_DLS(self, board, node, limit, goal):
        if (node.x, node.y) == (goal[0], goal[1]):
            return node
        elif limit == 0:
            return 0
        else:
            cutoff_occurred = False

            for child in self.__get_children(board, node):
                if child.time > self.timeAllowed:
                    continue
                result = self.__recursive_DLS(board, child, limit - 1, goal)

                if result == 0:
                    cutoff_occurred = True
                elif result != -1:
                    return result
                
            if cutoff_occurred:
                return 0
            return -1
    
    def IDS(self, board, start, goal):
        current_node = Node(start[0], start[1], None, 0, 0, self.fuelCapacity)
        limit = 1

        while True:
            res_node = self.__recursive_DLS(board, current_node, limit, goal)
            if res_node == -1:
                return -1
            if res_node == 0:
                limit += 1
            else:
                return res_node

    def move(self, board):
        """
        input: list(list()), a 2D list representing the map
        output: list((x, y)), a list of strings representing the moves on the coordinate
        """
        """
        idea:
            - IDS with time limit; if the time is up, do not let it get into the queue
            - Allow cycles in the path since we can limit the loop by the fuel capacity and the time limit
            - Even if the fuel can be refilled infinitely, the time limit is always finite so the loop will eventually stop
        """

        start = board.start
        goal = board.end
        res_node = self.IDS(board, start, goal)
        if res_node == -1:
            return -1

        result = []
        while res_node:
            result.append((res_node.x, res_node.y))
            
            for _ in range(int(board.board[res_node.x][res_node.y][1:]) if board.board[res_node.x][res_node.y][0] == 'F'
                                                                        else int(board.board[res_node.x][res_node.y])
                                                                        if board.board[res_node.x][res_node.y] not in ['S', 'G']
                                                                        else 0):
                result.append((res_node.x, res_node.y))

            res_node = res_node.parent
        
        return {'S': result[::-1]}