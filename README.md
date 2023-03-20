# COMP472-8Puzzle

*It is assumed that goal state is:*
    
    1 2 3
    8 0 4
    7 6 5     
#### Usage
Run `main.py` with the puzzle as string of digits (using B as the blank tile), the type of search algorithm - `DFS`, `BFS`, `BestFS`, `Astar` and the heuristic:  `HD`  = Hamming Distance, `MD` = Manhattan Distance, `PI`  = Permutation Inversions, 
	              `A1`  = (linear conflict + manhattan distance) or `None` if the search is uninformed (DFS, BFS)
#### Ex
```
Python3 main.py 2831647B5 Astar MD
Python3 main.py 2831647B5 BFS None

```
