import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def subgraph(self, nodes):
        """

        """
        nx_graph = self.graph.subgraph(nodes).copy()
        subgraph_obj = Graph.__new__(Graph)
        subgraph_obj.graph = nx_graph
        return subgraph_obj

    def bfs_traversal_shortestpath(self, start, end, all_bfs_queues):
        """
        Takes the queues from breadth first search traversal, to find a shortest path
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
                     if any(N in all_bfs_queues.pop(0) for N in all_bfs_queues[0]):
                        N = [n for n in all_bfs_queues[0] if n in all_bfs_queues.pop(0)]
                        break

                #  keep neighbours which have not been visited
                N = [n for n in N if n not in path]

                # Update stack
                stack = N.pop(0)
                
        path.append(start)

        return path


    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """

        # Check - if graph is empty
        if self.graph is None or len(self.graph.nodes) == 0: 
            raise ValueError("Graph is empty or no graph is provided")

        # Check if start node exists, and is in graph
        if start is None or start not in self.graph.nodes:
            raise ValueError("Provided start node is not in graph")

        # Initialize queue
        queue = []

        # add a tracking list of all queues
        all_bfs_queues = [[start]]

        # Initialize list of visited nodes
        visited = []
        # push source node to queue
        queue.append(start)
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
                
                return self.bfs_traversal_shortestpath(start, end, all_bfs_queues)
        # If a path between the start node and end node does not exist
        # return None
            else:
                return None


    




