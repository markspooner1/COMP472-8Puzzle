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
goal = [1, 2, 3, 8, 'B', 4, 7, 6, 5]
cols = 3
class Node:
    def __init__(self, parent, state, depth, pathCost):
        self.children = []
        self.parent = parent
        self.state = state
        self.depth = depth
        self.pathCost = pathCost
    def isGoal(self):
       return self.state == goal
    def moveRight(self, index):
        # mod by number of cols to make sure move right is valid
        # if valid, generate puzzle
        # get num to right of blank, swap them
        if index % cols < 2:
            
           
            # todo -> check if deep copy
            childState = self.state.copy()
            childState[index], childState[index + 1]  =  self.state[index + 1], 'B'
            # TODO Path Cost
              # add node to children of self
             # set parent of new node to self
            child = Node(self, childState, self.depth + 1, 0)
            self.children.append(child)
    def moveLeft(self, index):
        
        # similar idea for move right
        # can only move left if the index mod cols is greater than 0
        # follow same algo for move Right
        if index % cols > 0:
     
            tempLeftNum = self.state[index - 1]
            # todo -> check if deep copy
            childState = self.state.copy()
            childState[index] = tempLeftNum
            childState[index - 1] = 'B' 
            # TODO Path Cost
              # add node to children of self
             # set parent of new node to self
            child = Node(self, childState, self.depth + 1, 0)
            self.children.append(child)
    def moveUp(self, index):
        # check if index - cols >= 0
        if index - cols >= 0:

            tempUpNum = self.state[index - 3]
            childState = self.state.copy()
            childState[index] = tempUpNum
            childState[index - 3] = 'B'

            child = Node(self, childState, self.depth + 1, 0)
            self.children.append(child)
    def moveDown(self, index):
        # check if i + col < 9
        if index + cols < 9:
        
            tempNumDown = self.state[index + 3]
            childState = self.state.copy()
            childState[index] = tempNumDown
            childState[index + 3] = 'B'

            child = Node(self, childState, self.depth + 1, 0)
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
        pass
    
        
        


    

        
