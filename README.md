
![BuildStatus](https://github.com/IJbeasley/HW2-BFS/workflows/Assignment%20Tests/badge.svg) 

# Assignment 2
Breadth-first search

##  Description of Breadth-first search

Breadth-first search (bfs) is an algorithm for traversing a graph, or in other words, exploring its nodes and edges. This algorithm's approach to exploring a graph is to start at a given source node and then explore all unvisited neighboring nodes (frontier nodes) at the same step. This traversal approach means bfs visits nodes in order of their shortest distance from the source node.

Implementing this algorithm's prioritization of frontier nodes requires a linear data structure that performs operations in a 'First In, First Out'  (FIFO) manner, called a 'Queue.' This data structure is known as a queue because it functions analogously to real-world service queues (e.g. in supermarkets), where the people who first line up in a queue are the first served. Once nodes have entered the queue, the bfs algorithm considers them visited. 

## Description of search module

The search module in this repository contains functions to implement bfs algorithm on Graph class objects (class from networkx python package). 



# Assignment Tasks

## Coding Assessment
In search/graph.py:
* [x] Define the function bfs that takes in a graph, start node, and optional node and:
	* [x] If no end node is provided, returns a list of nodes in order of breadth-first search traversal from the given start node
	* [x] If an end node is provided and a path exists, returns a list of nodes in order of the shortest path to the end node
	* [x] If an end node is provided and a path does not exist, returns None

* Be sure that your code can handle possible edge cases, e.g.:
	* [x] running bfs traversal on an empty graph
	* [x] running bfs traversal on an unconnected graph
	* [x] running bfs from a start node that does not exist in the graph
	* [x] running bfs search for an end node that does not exist in the graph
	* [x] any other edge cases you can think of 

In test/test_bfs.py:
* [x] Write unit tests for breadth-first traversal and breadth-first search 
* [x] Test at least 2 possible edge cases (listed above)
    *  Include a test case that fails and raises an exception


## Software Development Assessment

* [x] Write unit tests (in the test_bfs.py file) for your breadth first search
* [x] Replace these instructions with a brief description of bfs in your forked repo
	
* [x] Automate Testing with a [Github Actions](https://docs.github.com/en/actions)
    * Ensure that the github actions complete the following:
        * runs pytest
* [x] Add "! [BuildStatus] (https://github.com/ < your-github-username > /HW2-BFS/workflows/HW2-BFS/badge.svg?event=push)" (update link and remove spaces) to the beginning of your readme file

