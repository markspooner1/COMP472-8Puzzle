from Search import *
import argparse
parser = argparse.ArgumentParser(description="Enter puzzle, search type, and heuristic")
parser.add_argument("puzzle",type=list ,help="Enter puzzle as a string of numbers ex: 2831647B5")
parser.add_argument("type", type=str,help="Enter search type: DFS -> Depth First Search, BFS -> Breadth First Search, BestFS -> Best First Search, Astar -> A Star Search")
parser.add_argument("heuristic", type=str,help="Enter Heuristic: HD -> Hamming Distance, MD -> Manhattan Distance, PI -> Permutation Inversions, A1 -> (linear conflict + manhattan distance), IH -> Inadmissable Heuristic")
args = parser.parse_args()
if __name__ == "__main__":
    start = args.puzzle
    type = args.type
    heuristic = args.heuristic
    for i in range(len(start)):
        if start[i] != "B":
            start[i] = int(start[i])
    
    search = Search(type, start,  heuristic)
    search.search()