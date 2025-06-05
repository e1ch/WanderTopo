import pytest
from core.graph_engine import GraphEngine
from core.models import PlaceNode, PlaceEdge

class TestGraphEngine:
    """
    Test suite for the GraphEngine class.
    Tests the core functionality of the graph-based travel planning engine.
    """
    
    @pytest.fixture
    def graph_engine(self):
        """
        Fixture that provides a fresh GraphEngine instance for each test.
        
        Returns:
            GraphEngine: A new instance of the graph engine
        """
        return GraphEngine()
    
    def test_add_node(self, graph_engine):
        """
        Test adding a new node to the graph.
        
        Args:
            graph_engine (GraphEngine): The graph engine instance
        """
        node = PlaceNode(
            name="Test Place",
            lat=40.7128,
            lon=-74.0060,
            trust_score=0.8
        )
        graph_engine.add_node(node)
        assert len(graph_engine.graph.nodes) == 1
        
    def test_add_edge(self, graph_engine):
        """
        Test adding an edge between two nodes.
        
        Args:
            graph_engine (GraphEngine): The graph engine instance
        """
        node1 = PlaceNode(
            name="Place 1",
            lat=40.7128,
            lon=-74.0060,
            trust_score=0.8
        )
        node2 = PlaceNode(
            name="Place 2",
            lat=40.7589,
            lon=-73.9851,
            trust_score=0.7
        )
        
        graph_engine.add_node(node1)
        graph_engine.add_node(node2)
        
        edge = PlaceEdge(
            source=node1,
            target=node2,
            distance=2.5,
            travel_time=30
        )
        
        graph_engine.add_edge(edge)
        assert len(graph_engine.graph.edges) == 1 