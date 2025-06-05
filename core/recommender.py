"""Recommender system for the WanderTopo travel graph."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional

from .models import PlaceEdge, PlaceNode


@dataclass
class Recommendation:
    """Represents a recommendation result."""

    node: PlaceNode
    score: float


class SimpleRecommender:
    """Provide basic recommendations using ratings and edge proximity.

    Parameters
    ----------
    nodes:
        Iterable of :class:`PlaceNode` objects available for recommendation.
    edges:
        Iterable of :class:`PlaceEdge` describing relationships between nodes.
    """

    _nodes: Dict[str, PlaceNode]
    _graph: Dict[str, List[PlaceEdge]]

    def __init__(self, nodes: Iterable[PlaceNode], edges: Iterable[PlaceEdge]) -> None:
        """Create a recommender instance and build an adjacency map."""
        self._nodes = {node.id: node for node in nodes}
        self._graph = {}
        for edge in edges:
            self._graph.setdefault(edge.source_id, []).append(edge)

    def recommend(
        self,
        current_node_id: str,
        *,
        top_k: int = 5,
        categories: Optional[Iterable[str]] = None,
    ) -> List[Recommendation]:
        """Return ``top_k`` recommended nodes.

        Recommendations are scored by combining node rating with
        edge weight and inverse distance. Only direct neighbors of
        ``current_node_id`` are considered.

        Parameters
        ----------
        current_node_id:
            Identifier of the node from which to search outward.
        top_k:
            Maximum number of results to return.
        categories:
            If provided, only nodes matching any of these categories
            will be considered.
        """
        if current_node_id not in self._graph:
            return []

        candidates = []
        for edge in self._graph[current_node_id]:
            node = self._nodes.get(edge.target_id)
            if node is None:
                continue
            if categories and not set(node.categories).intersection(categories):
                continue
            rating_score = node.rating or 0
            proximity_score = edge.weight / (1.0 + edge.distance)
            score = rating_score * 2 + proximity_score
            candidates.append(Recommendation(node=node, score=score))

        candidates.sort(key=lambda rec: rec.score, reverse=True)
        return candidates[:top_k]
