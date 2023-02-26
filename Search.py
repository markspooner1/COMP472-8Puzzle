# Init open list with top node
# init closed list to empty

from Node import *
from collections import deque
start = [1, 2, 3, 7, 8, 4, 'B', 6, 5]

root = Node(None, start, 0, 0)
def DFS():
    
    # root.printPuzzle()
    # root.generateSuccessors()
    # for child in root.children:
    #     child.printPuzzle()
    open = [root]
    closed = []
    while(len(open) > 0):
        x = open.pop()
       # x.printPuzzle()
        
        if x.isGoal():
            
            return "Goal"
        else:
            x.generateSuccessors()
            closed.append(x)
            for child in x.children:
                if not isOnOpenOrClosed(open, closed, child.state):
                    open.append(child)
def BFS():
    open = deque([root])
    closed = []
    while(len(open) > 0):
        x = open.popleft()
        x.printPuzzle()
        if x.isGoal():
            x.printPuzzle()
            return 'Goal'
        else:
            x.generateSuccessors()
            closed.append(x)
            for child in x.children:
                if not isOnOpenOrClosed(open, closed, child.state):
                    open.append(child)
    return "Fail"
def BestFS():
    pass

    
def isOnOpenOrClosed(open, closed, puzzle):
   return puzzle in open or puzzle in closed



if __name__ == "__main__":
    DFS()
    #print(BFS())

