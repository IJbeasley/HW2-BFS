import networkx as nx
from typing import List, Union

class Graph:
    """
    Class to contain a graph and your bfs function
    
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def subgraph(self, nodes: List):
        """
        Returns a subgraph of the graph with on the provided nodes.
        Wrapper around nx.subgraph which enables the resulting subgraph to also have the Graph class. 
        
        Args:
          nodes (list): A list of node names for the subgraph.
          
        Returns:
          Graph: A new Graph object containing the subgraph.
        """
        # Get the subgraph
        nx_graph = self.graph.subgraph(nodes).copy()
        
        # Initalise subgraph as Graph object
        subgraph_obj = Graph.__new__(Graph)
        subgraph_obj.graph = nx_graph
        
        return subgraph_obj

    def bfs_shortestpath(self, start, end, 
                         all_bfs_queues: List[List[str]]
                         ) -> List[str]:
        """
        Find the shortest path from start to end using the results from
        bfs traversal. 
        
        Specifically, it starts from the end node, finds the neighbours of this node
        and follows the bfs traversal path in reverse of the first neighbour that it hasn't visited. 
        
        Args:
          Required: 
            start: Name of start node
            end: Name of end node 
            all_bfs_queues: List of queues (List[str]) obtained from bfs traversal
            
        """
        # Initialize stack
        stack = []
        # push end node to stack
        stack.append(end)
        
        # Initialize queues (remove last queue, and then reverse)
        all_bfs_queues.pop()
        # Traverse the path between start and end node - in reverse order
        all_bfs_queues.reverse()
        
        # Use undirected graph so can traverse graph in reverse order
        undir_graph = nx.to_undirected(self.graph)

        # Initialize path
        path = []
        

        # for each 
        while all_bfs_queues:
          

                path.append(stack)
                   
                # find the neighbours of the current node
                N = [n for n in undir_graph.neighbors(stack[0])]
                

                # if any of these neighbours where found in the prior bfs step
                # then select these neighbours
                # otherwise, recursively try the prior steps
                # until neighbours are found in prior bfs steps
                while True:
                     last_queue = all_bfs_queues.pop(0)

                     if any(n in last_queue for n in N):

                        N = [n for n in N if n in last_queue]
                        
                        break
                      
                #  keep neighbours which have not been visited
                N = [n for n in N if n not in path]
                

                # Update stack
                stack = [N[0]]
                
        path.append([start])
        path.reverse()
        path = [item for sublist in path for item in sublist]

        return path


    def bfs(self, start, end=None) -> Union[List[str], None]:
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

        # Check - if graph is empty
        if self.graph is None or len(self.graph.nodes) == 0: 
            raise ValueError("Graph is empty or no graph is provided")

        # Check if start node exists, and is in graph
        if start is None or start not in self.graph.nodes:
            raise ValueError("Provided start node is not in graph")
          
        # Check that if end is provided, then it is in graph: 
        if end is not None and end not in self.graph.nodes:
            raise ValueError("Provided end node is not in graph")

        # Initialize queue
        queue = []      
        # push source node to queue
        queue.append(start)

        # add a tracking list of all queues
        all_bfs_queues = [[start]]

        # Initialize list of visited nodes
        visited = []
        # mark source node as visited
        visited.append(start)
        


        # Loop through nodes in graph, as long as end has not been visited
        while queue and end not in visited:
            # take the first node in queue, and find its neighbors
            v = queue.pop(0)
            N = [n for n in self.graph.neighbors(v)]
            all_bfs_queues.append(N)

            # for each neighbor, if it has not been visited, mark it as visited and add it to the queue
            for w in N:
                if w not in visited and w not in queue:
                    visited.append(w)
                    queue.append(w)



        # If there's no end node input, return a list nodes with the order of BFS traversal
        if end is None:
          
            return visited
          
        else:
          
        # If there is an end node input and a path exists, 
        # return a list of nodes with the order of the shortest path
            if end in visited:
                
                return self.bfs_shortestpath(start, end, all_bfs_queues)
        # If a path between the start node and end node does not exist
        # return None
            else:
                return None


    




