# pysearch-visualiser
Visual Python implementation of different graph search algorithms. Implemented using PyGame.

Implemented algorithms: *Depth-First Search (DFS)*, *Breadth-First Search (BFS)*, *A\* Search*.

Needed libraries: *PyGame*

# Controls
* Click/Drag left mouse
    * First click: sets the start node
    * Second click: sets the target/end node
    * Subsequent clicks: sets the block/barrier nodes, i.e. nodes that can't be traversed
* Click/Drag right mouse
    * Remove start/target/block node
* Press **Spacebar** key
    * Start the search from start to target node (only when both start and target nodes are set and search algorithm set)
* Press **D** key
    * Set the search algorithm to _**Depth-First Search (DFS)**_
* Press **B** key
    * Set the search algorithm to _**Breadth-First Search (DFS)**_
* Press **A** key
    * Set the search algorithm to _**A* Search**_
* Press **Backspace** key
    * Stop the search (only when the program is searching)
* Press **C** key
    * Clear everything (only when the program is not searching)
* Press **Escape** key
    * Quit the program
 
# How to use
1. Run the _*Main.py*_ file to start the program
2. Set the start node (left click)
3. Set the target node (left click)
4. Draw the barrier nodes (left click, draggable) *(Optional)*
5. Clear start, target or a barrier node (right click) *(Optional)*
6. Select the search algorithm for the search method (see Controls)
7. Press spacebar to start search
8. Watch the program run
9. Eventually, the program will draw a route from the target node to the start node


# Visual Legends
* Start node > Orange
* Target node > Turquoise
* Barrier node > Black
* Traversed node > Red
* Open node > Green
* Retracing node (shows route from start to target nodes) > Purple
