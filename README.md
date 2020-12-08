# pysearch-visualiser
Visual Python implementation of different graph search algorithms. Implemented using PyGame.

Implemented algorithms: *Depth-First Search (DFS)*, *Breadth-First Search (BFS)*, *A\* Search*.

Needed libraries: PyGame.

# Controls
* Click/Drag Right mouse
 * First click: sets the start node
 * Second click: sets the target/end node
 * Subsequent clicks: sets the block/barrier nodes, i.e. nodes that can't be traversed
* Click/Drag Left mouse
 * Remove start/target/block node
* Press **Spacebar** key
 * Start the search from start to target node (only when both start and target nodes are set and search algorithm set)
* Press **Q** key
 * Quit the program (only when the program is not searching)
* Press **D** key
 * Set the search algorithm to _**Depth-First Search (DFS)**_
* Press **B** key
 * Set the search algorithm to _**Breadth-First Search (DFS)**_
* Press **A** key
 * Set the search algorithm to _**A* Search**_
* Press **Esc** key
 * Stop the search (only when the program is searching)
* Press **C** key
 * Clear everything
 
# How to use
1. Set the start node (right click)
1. Set the target node (right click)
1. Draw the barrier nodes (right click, draggable) *(Optional)*
1. Select the search algorithm for the search method (see Controls)
1. Press spacebar to start search
1. Watch the program run
1. Eventually, the program will draw a route from the target node to the start node


# Visual Legends
* Start node > Orange
* Target node > Turquoise
* Barrier node > Black
* Traversed node > Red
* Open node > Green
* Retracing node > Purple
