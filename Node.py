# Max children is 4
# Once we find a goal state, need to be able to track back
class Node:
    def __init__(self, children, parent, state, depth, pathCost):
        self.children = []
        self.parent = parent
        self.state = state
        self.depth = depth
        self.pathCost = pathCost


        