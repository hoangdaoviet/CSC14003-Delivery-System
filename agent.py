class Agent:
    def __init__(self):
        pass

class PlayerLvl1(Agent):
    def __init__(self):
        pass

    def move(self, board):
        """
        input: list(list()), a 2D list representing the map
        output: list((x, y)), a list of strings representing the moves on the coordinate
        """
        return []

class PlayerLvl2(Agent):
    def __init__(self, timeAllowed):
        self.timeAllowed = timeAllowed

    def move(self, board):
        """
        input: list(list()), a 2D list representing the map
        output: list((x, y)), a list of strings representing the moves on the coordinate
        """
        return []

class PlayerLvl3(Agent):
    def __init__(self, timeAllowed, fuelCapacity):
        self.timeAllowed = timeAllowed
        self.fuelCapacity = fuelCapacity
    
    def move(self, board):
        """
        input: list(list()), a 2D list representing the map
        output: list((x, y)), a list of strings representing the moves on the coordinate
        """
        return []