# Init open list with top node
# init closed list to empty

from Node import *
from collections import deque
start = [1,2,3,4,5,6,7,'B',8]
# 1 2 3
# 8   4  
# 7 6 5
root = Node(None, start, 0)
goal = [1,2,3,8,'B',4,7,6,5]

def DFS():
    
    # root.printPuzzle()
    # root.generateSuccessors()
    # for child in root.children:
    #     child.printPuzzle()
    open = [root]
    closed = []
    while(len(open) > 0):
        x = open.pop()  
        
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
    open = deque([root])
    closed = []
    while(len(open) > 0):
        x = open.popleft()
        closed.append(x)
        if x.isGoal():
            return 'Goal'
        else:
            x.generateSuccessors()
            for child in x.children:
                if not isOnOpenOrClosed(open, closed, child.state):
                    open.append(child)
            sorted(open, key=lambda x: x.pathCost)

def AStar():
    open = deque([root])
    closed = []
    while(len(open) > 0):
        x = open.popleft()
        if x.isGoal():
            return "Goal"
        else:
            closed.append(x)
            x.generateSuccessors()
            for child in x.children:
                if not isOnOpenOrClosed(open, closed, child.state):
                    open.append(child)
            sorted(open, key=lambda x: x.pathCost)

    
def isOnOpenOrClosed(open, closed, puzzle):
    res = False
    for node in open:
       if node.state == puzzle:
           res = True
    for node in closed:
        if node.state == puzzle:
            res= True
    return res

if __name__ == "__main__":

    pass
    #DFS()
    #print(BFS())
    #print(BestFS())
    #print(AStar())