import pytest
from pathlib import Path
import sys

# Ensure project root is on the Python path when running tests directly
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from core.graph_engine import GraphEngine
from core.models import PlaceNode, PlaceEdge


@pytest.fixture
def graph_engine() -> GraphEngine:
    """Return a fresh GraphEngine for each test."""
    return GraphEngine()


def test_add_node(graph_engine: GraphEngine) -> None:
    node = PlaceNode(
        id="1",
        name="Test Place",
        latitude=40.7128,
        longitude=-74.0060,
    )
    graph_engine.add_node(node)
    assert "1" in graph_engine._nodes
    assert graph_engine._nodes["1"].name == "Test Place"


def test_add_edge(graph_engine: GraphEngine) -> None:
    node1 = PlaceNode(id="1", name="Place 1", latitude=0.0, longitude=0.0)
    node2 = PlaceNode(id="2", name="Place 2", latitude=1.0, longitude=1.0)
    graph_engine.add_node(node1)
    graph_engine.add_node(node2)

    edge = PlaceEdge(source_id="1", target_id="2", distance=2.5)
    graph_engine.add_edge(edge)

    assert edge in graph_engine._edges["1"]


def test_shortest_path(graph_engine: GraphEngine) -> None:
    a = PlaceNode(id="1", name="A", latitude=0.0, longitude=0.0)
    b = PlaceNode(id="2", name="B", latitude=0.0, longitude=1.0)
    c = PlaceNode(id="3", name="C", latitude=0.0, longitude=2.0)

    for node in (a, b, c):
        graph_engine.add_node(node)

    graph_engine.add_edge(PlaceEdge(source_id="1", target_id="2", distance=1))
    graph_engine.add_edge(PlaceEdge(source_id="2", target_id="3", distance=1))

    result = graph_engine.shortest_path("1", "3")
    assert result == (2, ["1", "2", "3"])

