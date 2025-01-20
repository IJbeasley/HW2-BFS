# write tests for bfs
import pytest
import networkx as nx
from search import graph

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    pass

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    pass


def test_empty_graph_bfs():
    """
    """
    test_graph = nx.null_graph()

    try:
        bfs(test_graph, 'A', 'B')
        assert False, "bfs should raise an exception for an empty graph"
    except ValueError as e:
        assert str(e) == "Graph is empty or no graph is provided", "Empty graph should raise a different value error"

