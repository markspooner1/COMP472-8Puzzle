import random
from test import linearConfictsAndMD2

# mapping of index to x,y coordinates for a given index
coordinates = {0:[0,0], 1:[1,0], 2:[2,0],
               3:[0,1], 4:[1,1], 5:[2,1],
               6:[0,2], 7:[1,2], 8:[2,2]}

# mapping of tiles in the 8-puzzle to their goal state (x, y) coordinates
goalcoordinates = {'B':[1,1], 1:[0,0], 2:[1,0],
               3:[2,0], 4:[2,1], 5:[2,2],
               6:[1,2], 7:[0,2], 8:[0,1]}
goal = [
    1,2,3,
    8,'B',4,
    7,6,5]
cols = 3
class Node:
    def __init__(self, parent, state, depth, heuristic = None, searchType = None):
        self.children = []
        self.parent = parent
        self.state = state
        self.depth = depth
        self.heuristicName = heuristic
        self.searchType = searchType
        # if search type is A* initialize f(n) = g(n) + h(n)

        if heuristic == "HD":
            self.pathCost = self.hammingDistance()
        elif heuristic == "MD":
            self.pathCost = self.manhattanDistance()
        elif heuristic == "A1":
            self.pathCost = self.linearConfictsAndMD()
        elif heuristic == "IH":
            self.pathCost = self.inAdmissableHeuristic()
        else:
            self.pathCost = self.permutationInversion()
        if searchType == "A*":
            self.f_value = self.depth + self.pathCost
    def isGoal(self):
       return self.state == goal
    """ 
    if the blank tile can be slided right (not in the rightmost column), swap blank tile and tile at index to its right 
    then add child to current nodes children
     """
    def moveRight(self, index):
        if index % cols < 2:
            childState = self.state.copy()
            childState[index], childState[index + 1]  =  self.state[index + 1], 'B'
            child = Node(self, childState, self.depth + 1, self.heuristicName, self.searchType)
            self.children.append(child)
    """ 
    if the blank tile can be slided left (not in the left column), swap blank tile and tile at index to its left 
    then add child to current nodes children
     """
    def moveLeft(self, index):
        if index % cols > 0:
            tempLeftNum = self.state[index - 1]
            childState = self.state.copy()
            childState[index] = tempLeftNum
            childState[index - 1] = 'B' 
            child = Node(self, childState, self.depth + 1, self.heuristicName, self.searchType)
            self.children.append(child)

    """ 
    if the blank tile can be slided Up (not in first row), swap blank tile and tile at index the above it 
    then add child to current nodes children
    """
    def moveUp(self, index):
        if index - cols >= 0:
            tempUpNum = self.state[index - 3]
            childState = self.state.copy()
            childState[index] = tempUpNum
            childState[index - 3] = 'B'
            child = Node(self, childState, self.depth + 1, self.heuristicName, self.searchType)
            self.children.append(child)
    """ 
    if the blank tile can be slided down (not in last row), swap blank tile and tile at index the below it 
    then add child to current nodes children
    """
    def moveDown(self, index):
        if index + cols < 9:
            tempNumDown = self.state[index + 3]
            childState = self.state.copy()
            childState[index] = tempNumDown
            childState[index + 3] = 'B'
            child = Node(self, childState, self.depth + 1, self.heuristicName, self.searchType)
            self.children.append(child)

    # generate all possible successors for a given node
    def generateSuccessors(self):
        index = self.state.index('B')
        self.moveRight(index)
        self.moveLeft(index)
        self.moveUp(index)
        self.moveDown(index)

    # print the puzzle in a 3x3 grid
    def printPuzzle(self):
        print("\n")
        for i in range(3):
            row = ''
            for j in range(3):
                index = i * 3 + j
                if self.state[index] == 'B':
                    row += '| {:^3} '.format(' ')
                else:
                    row += '| {:^3} '.format(self.state[index])
            row += '|'
            print(row)
        print("\n")


    # for each tile, if it is not in its goal state, increment the hamming distance
    def hammingDistance(self):
        hammingDistance = 0
        for i, val in enumerate(self.state):
            currPos = coordinates[i]
            goalPos = goalcoordinates[val]
            if currPos != goalPos and val != 'B':
                hammingDistance+=1
        return hammingDistance

    # for each tile, get its goal state (x, y) coordinates and current state (x, y) coordinates
    # then add the absolute value of the difference between the x coordinates and the y coordinates
    def manhattanDistance(self):
        manDistance = 0
        for i, val in enumerate(self.state):
            currentPosX, currentPosY = coordinates[i]
            goalPosX, goalPosY = goalcoordinates[val]
            manDistance += (abs(currentPosY - goalPosY) + abs(currentPosX - goalPosX)   )  
        return manDistance
    
    # for each tile i, check if the tiles (j) to its right have a goal state that that is less than i's goal state
    def permutationInversion(self):
        sum = 0
        for i, val in enumerate(self.state):
            if val == 'B':
                continue
            for j in range(i + 1, len(self.state)):
                if val == 'B':
                    continue
                index1 = goal.index(val)
                index2 = goal.index(self.state[j])
                if index2 < index1:
                    sum+=1
        return sum
     # need to find the linear conflicts for each row and column
     # this method will be called twice, once for the rows, then we get the transpose of the matix and call it again for the columns
    def linearConflict(self, board ,conflict):
        conflicts = 0
        # for each row
        for i in range(0, 3, 1):
            count = 0
            # for each tile in the ith row
            for j in range(i * 3, i*3 + 3 - 1, 1):
                if(board[j] == 'B'): continue

                # get the goal index of the current tile
                goalstate = goal.index(board[j])
                
                # for each tile to the right of the current tile
                # if the goal index of the current tile is greater than the goal index of the tile to the right
                # and the tile to the right is in the same row as the current tile
                # increment number of conflicts
                # we keep track of a count of conflicts per row to ensure that we only count a conflict once

                for k in range(j + 1, i*3 + 3 - 1 + 1, 1):
                    if(board[k] == 'B'): continue
                    neighbourGoalState = goal.index(board[k])
                    count += 1
                
                    if goalstate > neighbourGoalState and board[j] in conflict[i] and board[k] in conflict[i] and count < 3:
                        
                        conflicts += 1        
        return conflicts*2
    
    def linearConfictsAndMD(self):
        # to find the linear conflicts, we need to find the conflicts for each row and column
        # we can do this by transposing the matrix and calling the linear conflict method twice
        conflict = [
            [1, 2, 3],
            [8, 'B', 4],
            [7, 6, 5]
        ]
        conflictTranspose = [
            [1, 8, 7],
            [2, 'B', 6],
            [3, 4, 5]
        ] 
        transposed = [[] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                val = self.state[j * 3 + i]
                if isinstance(val, (int, str)):
                    transposed[i].append(val)
        transposed = [val for row in transposed for val in row]

        return self.manhattanDistance() + self.linearConflict(self.state, conflict) + self.linearConflict(transposed, conflictTranspose) 
    


    def inAdmissableHeuristic(self):
        return self.permutationInversion() + self.manhattanDistance() + random.uniform(100,200)

                    


   






        
        


    

        
