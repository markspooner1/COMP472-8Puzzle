# Init open list with top node
# init closed list to empty

from Node import *
from collections import deque
# 1 2 3
# 8   4  
# 7 6 5
class Search:
    def __init__(self, type, puzzle, heuristic = None):
        self.type = int(type)
        self.root = Node(None, puzzle, 1, heuristic, type)
        self.nodesVisited = 0
    def search(self):
        print(self.type)
        if self.type == 1:
            print(self.DFS())
        elif self.type == 2:
            print(self.BFS())
        elif self.type == 3:
            print(self.BestFS())
        elif self.type == 4:
            print(self.AStar())
            
    def DFS(self):
        
        # root.printPuzzle()
        # root.generateSuccessors()
        # for child in root.children:
        #     child.printPuzzle()
        open = [self.root]
        closed = []
        while(len(open) > 0):
            x = open.pop()  
            
            
            if x.isGoal():
                self.tracePath(x)
                return "Goal reached, length of search path: " + str(x.depth)
            else:
                x.generateSuccessors()
                closed.append(x)
                for child in x.children:
                    if not self.isOnOpenOrClosed(open, closed, child.state):
                        open.append(child)
    def BFS(self):
        open = deque([self.root])
        closed = []
        
        while(len(open) > 0):
            x = open.popleft()
            self.nodesVisited += 1

            if x.isGoal():
                x.printPuzzle()
                self.tracePath(x)
                return "Goal reached, length of search path: " + str(x.depth)
            else:
                x.generateSuccessors()
                closed.append(x)
                for child in x.children:
                    if not self.isOnOpenOrClosed(open, closed, child.state):
                        open.append(child)
        return "Fail"

    def BestFS(self):
        open = deque([self.root])
        closed = []
        
        while(len(open) > 0):
            self.nodesVisited += 1

            x = open.popleft()
            closed.append(x)
            if x.isGoal():
                print("Goal reached, length of search path: " + str(x.depth))
                self.tracePath(x)
                return
            else:
                x.generateSuccessors()
                for child in x.children:
                    if not self.isOnOpenOrClosed(open, closed, child.state):
                        open.append(child)
                open = deque(sorted(open, key=lambda x: x.pathCost))

    def AStar(self):
        open = deque([self.root])
        closed = []
        
        while(len(open) > 0):
            self.nodesVisited += 1
            x = open.popleft()
            if x.isGoal():
                print("Goal reached, length of search path: " + str(x.depth))
                self.tracePath(x)
                return 
            else:
                closed.append(x)
                x.generateSuccessors()
                for child in x.children:
                    if not self.isOnOpenOrClosed(open, closed, child.state):
                        open.append(child)
                open = deque(sorted(open, key=lambda x: x.pathCost))

        
    def isOnOpenOrClosed(self,open, closed, puzzle):
        res = False
        for node in open:
            if node.state == puzzle:
                res = True
        for node in closed:
            if node.state == puzzle:
                res= True
        return res
    def tracePath(self, node):
        path = []
        while(node != None):
            path.append(node)
            node = node.parent
        print("Nodes visited " + str(self.nodesVisited))
        print("\nPath from start to goal:")
        for i in range(len(path)-1, -1, -1):
            print(
            """
            |
            |
            |
            V
            """)
            path[i].printPuzzle()
           
            
          
    
        
        

if __name__ == "__main__":
    start = [3,6,4,'B',1,2,8,7,5]
    type = input(
    """Enter search: 
        1 -> Depth First Search
        2 -> Breadth First Search
        3 -> Best First Search
        4 -> A Star Search
    """)
    if int(type) == 3 or int(type) == 4:
        heuristic = input("""
        Enter Heuristic:
            HD -> Hamming Distance 
            MD -> Manhattan Distance 
            PI -> Permutation Inversions
        """)
    else: 
        heuristic = None
    search = Search(type, start, heuristic)
    search.search()

    

    """
    heuristics
    ----------
        -> Hamming Distance -> HD
        -> Manhattan Distance -> MD
        -> Permutation Inversions -> PI
    """