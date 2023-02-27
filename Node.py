""" 
Max children is 4
- Once we find a goal state, need to be able to track back our way to initial state (to find path)
    - To do this: keep track of parent
- Goal state:
    1 2 3
    8 _ 4
    7 6 5
    - as a list: [1, 2, 3, 8, B, 4, 7, 6, 5]
 """
 # Will need to set root parent to null
coordinates = {0:[0,0], 1:[1,0], 2:[2,0],
               3:[0,1], 4:[1,1], 5:[2,1],
               6:[0,2], 7:[1,2], 8:[2,2]}
goalcoordinates = {'B':[1,1], 1:[0,0], 2:[1,0],
               3:[2,0], 4:[2,1], 5:[2,2],
               6:[1,2], 7:[0,2], 8:[0,1]}

goal = [1,2,3,8,'B',4,7,6,5]
cols = 3
class Node:
    def __init__(self, parent, state, depth):
        self.children = []
        self.parent = parent
        self.state = state
        self.depth = depth
        self.pathCost = self.permutationInversion()
    def isGoal(self):
       return self.state == goal
    def moveRight(self, index):
        if index % cols < 2:
            childState = self.state.copy()
            childState[index], childState[index + 1]  =  self.state[index + 1], 'B'
            child = Node(self, childState, self.depth + 1)
            self.children.append(child)
    def moveLeft(self, index):
        if index % cols > 0:
            tempLeftNum = self.state[index - 1]
            childState = self.state.copy()
            childState[index] = tempLeftNum
            childState[index - 1] = 'B' 
            child = Node(self, childState, self.depth + 1)
            self.children.append(child)
    def moveUp(self, index):
        if index - cols >= 0:
            tempUpNum = self.state[index - 3]
            childState = self.state.copy()
            childState[index] = tempUpNum
            childState[index - 3] = 'B'
            child = Node(self, childState, self.depth + 1)
            self.children.append(child)
    def moveDown(self, index):
        # check if i + col < 9
        if index + cols < 9:
            tempNumDown = self.state[index + 3]
            childState = self.state.copy()
            childState[index] = tempNumDown
            childState[index + 3] = 'B'
            child = Node(self, childState, self.depth + 1)
            self.children.append(child)
    def generateSuccessors(self):
        index = self.state.index('B')
        self.moveRight(index)
        self.moveLeft(index)
        self.moveUp(index)
        self.moveDown(index)
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

    def hammingDistance(self):
        # Count the number of tiles out of place, dont count the blank tile
        hammingDistance = 0
        for i, val in enumerate(self.state):
            currPos = coordinates[i]
            goalPos = goalcoordinates[val]
            if currPos != goalPos and val != 'B':
                hammingDistance+=1
        return hammingDistance

    def manhattanDistance(self):
        manDistance = 0
        for i, val in enumerate(self.state):
            currentPosX, currentPosY = coordinates[i]
            goalPosX, goalPosY = goalcoordinates[val]
            manDistance += abs(currentPosY - goalPosY) + abs(currentPosX - goalPosX)     
        return manDistance
    def permutationInversion(state):
        #for each value in state
        #for each value to its right
            #if when we check the goal state, value2 is actually supposed to be to the left of value, we increment 
            # if index of value2 in goal state is < current index of value in goal state increment++ 
        sum = 0
        for i, val in enumerate(state):
            if val == 'B':
                continue
            for j in range(i + 1, len(state)):
                if val == 'B':
                    continue
                index1 = goal.index(val)
                index2 = goal.index(state[j])
                if index2 < index1:
                    sum+=1
        return sum
                


    def fFunctionHeuristic(self):
        return self.manhattanDistance() + self.depth




        
        


    

        
