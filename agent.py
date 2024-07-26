from board import *
from queue import PriorityQueue
from collections import deque
from copy import deepcopy as dcopy
import numpy as np
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
    
    @staticmethod
    def AStar(board: Board):
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

class PlayerLvl4:
    def __init__(self, timeAllowed, fuelCapacity):
        self.timeAllowed = timeAllowed
        self.fuelCapacity = fuelCapacity
        self.agents = []
        self.goals = []
        np.random.seed()

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
                new_time = node.time + (1 if cell in ['0', 'S', 'G'] else (int(cell[1:]) + 1) if cell[0] == 'F'
                                                                     else int(cell) if 'G' not in cell
                                                                     else int(cell[1:]))
                new_fuel = (node.fuel - 1) if cell[0] != 'F' else self.fuelCapacity

                new_node = Node(x, y, node, cost=new_cost, time=new_time, fuel=new_fuel)
                children.append(new_node)

        return children
    
    def __get_next_location_hill_climbing(self, board, node, goal):
        def h(node):
            return abs(node.x - goal[0]) + abs(node.y - goal[1])
        
        children = sorted(self.__get_children(board, node), key=lambda x: h(x))

        num_children = len(children)
        ratio = [0.8] + [0.2 / (num_children - 1) for _ in range(num_children - 1)]

        return np.random.choice(children, p=ratio) if num_children > 1 else children[0] if num_children != 0 else node

    def move(self, board: Board):
        """
        input: list(list()), a 2D list representing the map
        output: list((x, y)), a list of strings representing the moves on the coordinate
        """
        start = board.start
        end = board.end
        main_agent = Node(start[0], start[1], None, 0, 0, self.fuelCapacity)

        for agent, location in board.get_all_agents():
            self.agents.append((agent, Node(location[0], location[1], None, 0, 0, self.fuelCapacity)))

        for goal, location in board.get_all_goals():
            self.goals.append((goal, location))

        search_board = dcopy(board)

        cell_values = ['0' for _ in range(10)]

        # check_list = []

        # count = 0

        while True:
            # count += 1
            # print_list = [(main_agent.x, main_agent.y)]
            # for i in range(len(self.agents)):
            #     print_list.append((self.agents[i][1].x, self.agents[i][1].y))
            # check_list.append(print_list)
            # if count == 1000:
            #     with open('output.txt', 'w') as f:
            #         for row in check_list:
            #             f.write(str(row) + '\n')
            #     return -1

            tmp_next_location = self.__get_next_location_hill_climbing(search_board, main_agent, end)
            if tmp_next_location.time > self.timeAllowed:
                break
            if search_board.board[tmp_next_location.x][tmp_next_location.y] == 'G':
                break

            search_board.board[main_agent.x][main_agent.y] = cell_values[0]
            cell_values[0] = search_board.board[tmp_next_location.x][tmp_next_location.y]
            search_board.board[tmp_next_location.x][tmp_next_location.y] = 'S'

            main_agent = tmp_next_location

            for i in range(len(self.agents)):
                current_agent = self.agents[i][1]
                current_goal = self.goals[i][1]
                tmp_next_location = self.__get_next_location_hill_climbing(search_board, current_agent, current_goal)
                if tmp_next_location.time > self.timeAllowed:
                    break
                if search_board.board[tmp_next_location.x][tmp_next_location.y] == 'G' + str(i):
                    search_board.board[current_agent.x][current_agent.y] = 0
                    
                    new_row = np.random.randint(0, search_board.n - 1)
                    new_col = np.random.randint(0, search_board.m - 1)

                    while search_board.board[new_row][new_col] in ['S', 'G', '-1'] or 'G' in search_board.board[new_row][new_col]:
                        new_row = np.random.randint(0, search_board.n - 1)
                        new_col = np.random.randint(0, search_board.m - 1)

                    search_board.board[new_row][new_col] = 'G' + str(i)

                search_board.board[current_agent.x][current_agent.y] = cell_values[i + 1]
                cell_values[i + 1] = search_board.board[tmp_next_location.x][tmp_next_location.y]
                search_board.board[tmp_next_location.x][tmp_next_location.y] = 'S' + str(i)

                self.agents[i] = (i, tmp_next_location)

        result = [[]]
        while main_agent:
            result[0].append((main_agent.x, main_agent.y))
            main_agent = main_agent.parent

        for i in range(len(self.agents)):
            current_agent = self.agents[i][1]
            result.append([])
            while current_agent:
                result[i + 1].append((current_agent.x, current_agent.y))
                current_agent = current_agent.parent

        return [{'S': result[0][::-1]}] + [{'S' + str(i): result[i + 1][::-1]} for i in range(len(self.agents))]