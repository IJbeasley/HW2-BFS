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

    def restricted_dfs(self, start, allowed_nodes, all_bfs_queues):
        """
        Depth first search algorithm to find the shortest path from start to end node
        """
        # Initialize stack
        stack = []

        # Traverse the path between start and end node - in reverse order
        all_bfs_queues.reverse()

        # push end node to stack
        stack.append(all_bfs_queues.pop(0)[0])

        # Initialize path
        path = []

        # Initalize current node
        current_node =  all_bfs_queues.pop(0)[0]

        while all_bfs_queues:
                
                path.append(stack)
                   
                # what are the neighbours of the current node
                N = [n for n in self.graph.neighbors(stack)]

                # of these neighbours, which were found in prior step of bfs
                N = [n for n in N if n in all_bfs_queues.pop(0)]

                #  of these neighbours, which have not been visited
                N = [n for n in N if n not in path]

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
        queue.append([start])
        # mark source node as visited
        visited.append(start)

        # Loop through nodes in graph, as long as end has not been visited
        while queue and end not in visited:
            # take the first node in queue, and find its neighbors
            v = queue.pop(0)
            N = [n for n in self.graph.neighbors(v)]
            all_bfs_queues.append([N])

            # for each neighbor, if it has not been visited, mark it as visited and add it to the queue
            for w   in N:
                if w not in visited and w not in queue:
                    visited.append(w)
                    queue.append(w)

        # If there's no end node input, return a list nodes with the order of BFS traversal
        if end is None:
            return visited
        else:
        # If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
            if end in visited:
                
                return self.restricted_dfs(start, visited, all_bfs_queues)

            else:
                return None


graph = nx.null_graph()

bfs(graph, 'A', 'F') # ['A', 'B', 'D', 'F']

    




