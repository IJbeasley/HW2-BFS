# write tests for bfs
import pytest
import networkx as nx
from search import Graph
#import matplotlib.pyplot as plt
#import matplotlib.pyplot as plt
#import scipy

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    
    #test_graph = nx.read_adjlist("data/tiny_network.adjlist", create_using=nx.DiGraph, delimiter=";")
    test_graph = Graph("data/tiny_network.adjlist")
    print(type(test_graph))
    
    test_graph = nx.subgraph(test_graph, ["Charles Chiu", "33242416", "Atul Butte"])
    #print(type(test_graph))

    # test bfs traversal - which is done when end=None
  
    
    test_bfs_result = test_graph.bfs(start = "Charles Chiu", end = None)
    #print(type(test_bfs_result))
    #plt.figure()
    #test_graph = nx.read_adjlist(test_graph, create_using=nx.DiGraph, delimiter=";")
    # nx.draw(test_graph, with_labels=True)
    # 
    # plt.savefig("graph_plot.png", format="PNG", dpi=300)  # Save with high resolution
    # plt.close() 

    # expected bfs traversal
    bfs_traversal = ["Charles Chiu", "33242416", "Atul Butte"]
 
    assert test_bfs_result == bfs_traversal, "bfs traversal was not done correctly"

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

    test_graph = Graph("data/citation_network.adjlist")
    #test_graph = nx.read_adjlist("data/citation_network.adjlist", create_using=nx.DiGraph, delimiter=";")
    test_graph = test_graph.subgraph(["Elad Ziv", "Jimmie Ye", "Dara Torgerson", "28366442", "28461288"])
    
    # print(type(test_graph))
    # plt.figure()
    #test_graph = nx.read_adjlist(test_graph, create_using=nx.DiGraph, delimiter=";")
    # nx.draw(test_graph, with_labels=True)
    # 
    # plt.savefig("graph_plot.png", format="PNG", dpi=300)  # Save with high resolution
    # plt.close()
    
    # Test bfs, find the shortest path between two nodes
    bfs_result = test_graph.bfs(start = "Dara Torgerson", end = "Jimmie Ye")

    shortest_path = ["Dara Torgerson","28366442", "Jimmie Ye"]

    #assert bfs == shortest_path, "bfs did not return the shortest path between two nodes"

    pass



def test_empty_graph_bfs():
    """
    Test bfs correctly raises an error on an empty graph (saved as data/empty_graph.adjlist)
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
    Test bfs correctly raises an error when the start node is not in the graph
    """

    test_graph = Graph("data/tiny_network.adjlist")
    
    try: 
      
      test_graph.bfs(start = 'Tony Capra')
      assert False, "start node is not in graph, which should have raised an error"
      
    except ValueError as e:
      
      assert str(e) == "Provided start node is not in graph", "start node is not in graph, which should have raised a different error"


def test_unconnected_bfs():
    """
    Test that bfs correctly returns None when there is no path between two nodes, using an unconnected graph
    """
    # make the unconnected graph
    # number of nodes in graph
    n = 2
    unconnected_graph = nx.empty_graph(n)
    nx.write_adjlist(unconnected_graph, "data/unconnected_graph.adjlist")

    test_graph = Graph("data/unconnected_graph.adjlist")

    bfs = test_graph.bfs(start = '0', end = '1')

    assert bfs == None, "bfs should return None when there is no path between two nodes"
