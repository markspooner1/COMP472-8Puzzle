from Search import *

if __name__ == "__main__":
    start = [5, 1, 4, 7, 'B', 6, 3, 8, 2]
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
            A1 -> My Custom heuristic from Theory Assignment 1 (linear conflict + manhattan distance)
            IH -> Inadmissable Heuristic
        (Enter either HD, MD, PI, A1, or IH): """)
    else: 
        heuristic = None
    search = Search(type, start, heuristic)
    search.search()