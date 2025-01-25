# write tests for bfs
import pytest
import networkx as nx
from search import Graph

def test_bfs_traversal():
    """
    Unit test for a breadth-first traversal. 
    Checks that all required nodes are being traversed.
    """
    
    test_graph = Graph("data/tiny_network.adjlist")
    
    # select a subgraph of this graph to test bfs traversal on: 
    # unconnected components shouldn't be observed in test
    test_subgraph = nx.subgraph(test_graph, ["Charles Chiu", "Atul Butte",  "Steven Altschuler", "Lani Wu", "31395880","33242416", # connected component
                                          "34946850", "34943926" #unconnected component
                                          ])

    # test bfs traversal - which is done when end=None in the bfs function
    test_bfs_result = test_subgraph.bfs(start = "Charles Chiu", end = None)

    # Compare bfs travels with true / expected bfs traversal
    true_bfs_traversal = ["Charles Chiu", "33242416", "Atul Butte","31395880", "Steven Altschuler", "Lani Wu"]
    
    assert len(test_bfs_result) == len(true_bfs_traversal), "BFS traversal didn't search all required nodes"
 
    assert test_bfs_result == true_bfs_traversal, "BFS traversal order was correct"


def test_bfs():
    """
    Unit test for your breadth-first search here to find the shortest path.
    
    Checks that providing two connected nodes in a subgraph of the 'citation_network.adjlist' file 
    to the bfs function returns the shortest path between them.

    """

    test_graph = Graph("data/citation_network.adjlist")
    
    # select a subgraph of this graph to test on: 
    test_subgraph = test_graph.subgraph(["Elad Ziv", "Jimmie Ye", "Dara Torgerson", "28366442", "28461288"])
    
    # Get bfs function to find the shortest path between two nodes
    bfs_result = test_subgraph.bfs(start = "Dara Torgerson", end = "Jimmie Ye")
    
    # Compare found shortest path with true shortest path
    true_shortest_path = ["Dara Torgerson","28366442", "Jimmie Ye"]
    
    assert bfs_result == true_shortest_path, "bfs did not return the shortest path between two nodes"


def test_unconnected_nodes_bfs():
    """
        
    An additional unit test for nodes that are not connected in a
    subgraph of the 'citation_network.adjlist' file 
    
    Should return None.
    """
    
    test_graph = Graph("data/citation_network.adjlist")
    
    bfs_result = test_graph.bfs(start = "Elad Ziv", end = "31803040")
    
    assert bfs_result == None, "bfs should return None when there is no path between two nodes"


def test_unconnected_graph_bfs():
    """
    An additional unit test for nodes that are not connected. 
    Tests that bfs correctly returns None when there is no path between two nodes, 
    using an entirely unconnected graph.
    
    """
    # make the unconnected graph
    # number of nodes in graph
    n = 2
    unconnected_graph = nx.empty_graph(n)
    nx.write_adjlist(unconnected_graph, "data/unconnected_graph.adjlist")

    test_graph = Graph("data/unconnected_graph.adjlist")

    bfs = test_graph.bfs(start = '0', end = '1')

    assert bfs == None, "bfs should return None when there is no path between two nodes"


def test_empty_graph_bfs():
    """
    Unit test to check that bfs correctly raises an error
    when it is applied to an empty graph (saved as data/empty_graph.adjlist)
    """
    
    # this is how the empty graph was made + saved 
    empty_graph = nx.null_graph() 
    nx.write_adjlist(empty_graph, "data/empty_graph.adjlist")
    
    empty_graph = Graph("data/empty_graph.adjlist")
    

    try:
      
        empty_graph.bfs(start = 'Martin Kampmann')
        assert False, "bfs should raise an exception for an empty graph"
        
    except ValueError as e:
      
        assert str(e) == "Graph is empty or no graph is provided", "Empty graph should raise a different value error"


def test_bad_start_node_bfs(): 

    """
    Unit test to check bfs correctly raises an error when the provided start node is not in the graph
    """

    test_graph = Graph("data/tiny_network.adjlist")
    
    try: 
      
      test_graph.bfs(start = 'Tony Capra')
      assert False, "start node is not in graph, which should have raised an error"
      
    except ValueError as e:
      
      assert str(e) == "Provided start node is not in graph", "start node is not in graph, which should have raised a different error"




def test_bad_end_node_bfs(): 

    """
    Unit test to check bfs correctly raises an error when the start node is not in the graph
    """

    test_graph = Graph("data/tiny_network.adjlist")
    
    try: 
      
      test_graph.bfs(start = 'Lani Wu', end = 'Tony Capra')
      assert False, "Provided end node is not in graph, which should have raised an error"
      
    except ValueError as e:
      
      assert str(e) == "Provided end node is not in graph", "End node is not in graph, which should have raised a different error"



