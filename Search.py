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
        self.root = Node(None, puzzle, 0, heuristic, int(type))
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
                self.tracePath(x, x.depth, len(closed))
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
            if x.isGoal():
                x.printPuzzle()
                self.tracePath(x, x.depth, len(closed))
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

            x = open.popleft()
            closed.append(x)
        
            if x.isGoal():
                print("Goal reached, length of search path: " + str(x.depth))
                self.tracePath(x, x.depth, len(closed))
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
            x = open.popleft()
            if x.isGoal():
                self.tracePath(x, x.depth, len(closed))
                return 
            else:
                closed.append(x)
                x.generateSuccessors()
                for child in x.children:
                    if not self.isOnOpenOrClosed(open, closed, child.state, "Astar"):
                        open.append(child)
                    else:
                        existingNeighbour = self.findNodeOnOpenOrClosedList(open, child.state)
                        if existingNeighbour is None:
                            pass
                        elif child.f_value < existingNeighbour.f_value:
                            existingNeighbour.f_value = child.f_value
                            existingNeighbour.parent = child.parent
                        
                    
                open = deque(sorted(open, key=lambda x: x.f_value))

        
    def isOnOpenOrClosed(self,open, closed, puzzle, type = None):
        res1 = False
        res2 = False
        for node in open:
            if node.state == puzzle:
                res1 = True
        for node in closed:
            if node.state == puzzle:
                res2 = True
        if type == "Astar":
    
            return res1 and res2
        else:
            return res1 or res2


    def findNodeOnOpenOrClosedList(self, list, puzzle):
        for node in list:
            if node.state == puzzle:
                return node
        return None


    def tracePath(self, node, depth, length):
        path = []
        while(node != None):
            path.append(node)
            node = node.parent
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
        print("Nodes visited " + str(length))
        print("Goal reached, length of soluton path: " + str(depth))



        

if __name__ == "__main__":
    start = [5,1,4,7,'B',6,3,8,2]
    type = input(
    """Enter search: 
        1 -> Depth First Search
        2 -> Breadth First Search
        3 -> Best First Search
        4 -> A Star Search
    (Enter either 1 2 3 or 4): """)
    if int(type) == 3 or int(type) == 4:
        heuristic = input("""
        Enter Heuristic:
            HD -> Hamming Distance 
            MD -> Manhattan Distance 
            PI -> Permutation Inversions
            A1 -> My Custom heuristic from Theory Assignment 1
            IH -> Inadmissable Heuristic
        (Enter either HD, MD, PI, A1, or IH): """)
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