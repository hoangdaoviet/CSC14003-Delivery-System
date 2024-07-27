from board import *
from queue import PriorityQueue
from collections import deque
from copy import deepcopy as dcopy
import numpy as np
import time

class PlayerLvl1:
    def BFS(self, board):
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
            return {'S': [start]}
        
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
            return {}
        result = []
        while current_node:
            result.append((current_node.x, current_node.y))
            current_node = current_node.parent
        return {'S': result[::-1]}

    def isCycle(self, node):
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
            return {'S': [start]}
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
            return {}
        result = []
        while current_node:
            result.append((current_node.x, current_node.y))
            current_node = current_node.parent
        return {'S': result[::-1]}
    
    def UCS(self, board):
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
            return {}

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
            return {'S': [start]}
        
        while frontier:
            _, current_node = frontier.get()
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
            return {}
        
        result = []
        while current_node:
            result.append((current_node.x, current_node.y))
            current_node = current_node.parent
        return {'S': result[::-1]}

    def AStar(self, board):
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
            return {}

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
                return {}
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
                new_time = node.time + (1 if cell[0] in ['0', 'S', 'G'] else (int(cell[1:]) + 1) if cell[0] == 'F'
                                                                        else int(cell))
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
    
    def __IDS(self, board, start, goal):
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
        res_node = self.__IDS(board, start, goal)
        if res_node == -1:
            return {}

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
        def update_manhattan_distance(heuristic, node, goal):
            if node.x == goal[0]:
                path = board.board[node.x][node.y:goal[1]:1]
                if len(path) > 0 and ('-1' in path or 'S' in path[0]):
                    heuristic += 2
            elif node.y == goal[1]:
                path = [row[node.y] for row in board.board[node.x:goal[0]:1]]
                if len(path) > 0 and ('-1' in path or 'S' in path[0]):
                    heuristic += 2

            if board.board[goal[0]][goal[1]][0] == 'F':
                return heuristic

            current = node.parent
            while current is not None:
                if current == node:
                    heuristic += 1
                current = current.parent

            return heuristic

        def h(node):
            min_heuristic = abs(node.x - goal[0]) + abs(node.y - goal[1])

            min_heuristic = update_manhattan_distance(min_heuristic, node, goal)

            if board.board[node.x][node.y][0] == 'F' and min_heuristic - 1 > node.parent.fuel:
                min_heuristic = 0
            elif min_heuristic - 1 > node.parent.fuel:
                fuel_locations = board.get_all_fuels()

                for location in fuel_locations:
                    heuristic = abs(node.x - location[0]) + abs(node.y - location[1])
                    
                    heuristic = update_manhattan_distance(heuristic, node, location)

                    if heuristic < min_heuristic:
                        min_heuristic = heuristic

            return min_heuristic
        
        children = sorted(self.__get_children(board, node), key=lambda x: h(x))

        num_children = len(children)
        ratio = [0.9] + [0.1 / (num_children - 1) for _ in range(num_children - 1)]

        return np.random.choice(children, p=ratio) if num_children > 1 else children[0] if num_children != 0 \
                                                                       else Node(node.x, node.y, node, node.cost, node.time + 1, node.fuel)

    def __multiagents_hill_climbing(self, board):
        start = board.start
        end = board.end
        main_agent = Node(start[0], start[1], None, 0, 0, self.fuelCapacity)

        for agent, location in board.get_all_agents():
            self.agents.append((agent, Node(location[0], location[1], None, 0, 0, self.fuelCapacity)))

        for goal, location in board.get_all_goals():
            self.goals.append((goal, location))

        search_board = dcopy(board)

        cell_values = ['0' for _ in range(10)]

        while True:
            tmp_next_location = self.__get_next_location_hill_climbing(search_board, main_agent, end)
            if tmp_next_location.time > self.timeAllowed:
                break

            search_board.board[main_agent.x][main_agent.y] = cell_values[0]
            cell_values[0] = search_board.board[tmp_next_location.x][tmp_next_location.y]
            search_board.board[tmp_next_location.x][tmp_next_location.y] = 'S'

            main_agent = tmp_next_location

            if main_agent.x == end[0] and main_agent.y == end[1]:
                break

            for i in range(len(self.agents)):
                current_agent = self.agents[i][1]
                current_goal = self.goals[i][1]
                tmp_next_location = self.__get_next_location_hill_climbing(search_board, current_agent, current_goal)
                if tmp_next_location.time > self.timeAllowed:
                    break
                if tmp_next_location.x == current_goal[0] and tmp_next_location.y == current_goal[1]:
                    new_row = np.random.randint(0, search_board.n - 1)
                    new_col = np.random.randint(0, search_board.m - 1)

                    while '0' not in search_board.board[new_row][new_col]:
                        new_row = np.random.randint(0, search_board.n - 1)
                        new_col = np.random.randint(0, search_board.m - 1)

                    tmp_next_location.time = 0
                    tmp_next_location.fuel = self.fuelCapacity
                    search_board.board[new_row][new_col] = 'G' + str(i+1)
                    self.goals[i] = (i, (new_row, new_col))

                search_board.board[current_agent.x][current_agent.y] = cell_values[i + 1]
                cell_values[i + 1] = search_board.board[tmp_next_location.x][tmp_next_location.y]
                search_board.board[tmp_next_location.x][tmp_next_location.y] = 'S' + str(i)

                self.agents[i] = (i, tmp_next_location)

        if main_agent.x != end[0] or main_agent.y != end[1]:
            return {}, [[]]

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

        res_dict = {'S': result[0][::-1]}
        for i in range(1, len(result)):
            res_dict['S' + str(i)] = result[i][::-1]

        for key in res_dict.keys():
            search_board.board[res_dict[key][0][0]][res_dict[key][0][1]] = key
            if key == 'S':
                search_board.board[end[0]][end[1]] = 'G'
            else:
                search_board.board[res_dict[key][-1][0]][res_dict[key][-1][1]] = cell_values[int(key[1:])]

        return res_dict, search_board.board
    
    def move(self, board):
        """
        input: list(list()), a 2D list representing the map
        output: list((x, y)), a list of strings representing the moves on the coordinate
        """
        """
        idea:
            - Hill climbing variant combined with global search with multiple agents, random choices and forced movements
            (need to move to 4 directions even if the current cell have maximum value)
            - The main agent will move first and then the other agents will move
            - If the time is up and the fuel is 0, return an empty dictionary
            - The value function is a variant of Manhattan distance heuristic
            - The value function ensure that there is always a solution if the time limit and fuel capacity are sufficient
        """
        for _ in range(30):
            self.agents = []
            self.goals = []

            res, search_board = self.__multiagents_hill_climbing(board)
            if res == {}:
                continue
            return res, search_board
        return {}, [[]]