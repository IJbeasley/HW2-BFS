# write tests for bfs
import pytest
import networkx as nx
from search import Graph

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """

    test_graph = Graph("data/tiny_network.adjlist")
    # test bfs traversal - which is done when end=None
    bfs_traversal = test_graph.bfs(start = 'Martin Kampmann', end = None)

    print(bfs_traversal)

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
    
    # make + save empty graph for testing: 
    # empty_graph = nx.null_graph() 
    # nx.write_adjlist(empty_graph, "data/empty_graph.adjlist")
    
    empty_graph = Graph("data/empty_graph.adjlist")
    

    try:
      
        empty_graph.bfs(start = 'Martin Kampmann')
        assert False, "bfs should raise an exception for an empty graph"
        
    except ValueError as e:
      
        assert str(e) == "Graph is empty or no graph is provided", "Empty graph should raise a different value error"


def test_bad_start_node_bfs(): 

    """
    """
    test_graph = Graph("data/tiny_network.adjlist")
    
    try: 
      
      test_graph.bfs(start = 'Tony Capra')
      assert False, "start node is not in graph, which should have raised an error"
      
    except ValueError as e:
      
      assert str(e) == "Provided start node is not in graph", "start node is not in graph, which should have raised a different error"
