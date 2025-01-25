
![BuildStatus](https://github.com/IJbeasley/HW2-BFS/workflows/Assignment%20Tests/badge.svg) 

# Assignment 2
Breadth-first search

##  Description of Breadth-first search

Breadth-first search (bfs) is an algorithm for traversing a graph, or in other words, exploring its nodes and edges. This algorithm's approach to exploring a graph is to start at a given source node and then explore all unvisited neighboring nodes (frontier nodes) at the same step. This traversal approach means bfs visits nodes in order of their shortest distance from the source node.

Implementing this algorithm's prioritization of frontier nodes requires a linear data structure that performs operations in a 'First In, First Out'  (FIFO) manner, called a 'Queue.' This data structure is known as a queue because it functions analogously to real-world service queues (e.g. in supermarkets), where the people who first line up in a queue are the first served. Once nodes have entered the queue, the bfs algorithm considers them visited. 

## Description of search module and bfs function

The search module in this repository contains functions to implement bfs algorithm on Graph class objects obtained by reading .adjlist files (using the networkx package)

The bfs function in this module performs breadth-first search traversal from the provided source (start) node, and if requested finds the shortest path from this source node to a provided end node, where it exists. 

```
bfs(self, start, end=None) -> Union[List[str], None] 

        """
        Perform breadth-first search traversal, and if requested find the shortest path. 

        If there is no end node provided, this functions return a list nodes in the order of BFS traversal.
        
        If there is an end node input, then: 
          if path exists between the start and end node, a list of nodes with the order of the shortest path is returned.
          
          Otherwise if there is no path between the start and end node, None is returned. 
          
        Args:
          Required: 
            start: Name of start node
          
          Optional: 
            end: Name of end node 

        """
```
