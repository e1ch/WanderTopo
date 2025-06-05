"""Graph builder and manager for WanderTopo."""

from __future__ import annotations

from collections import defaultdict
from heapq import heappop, heappush
from typing import Dict, Iterable, List, Optional, Tuple

from .models import PlaceEdge, PlaceNode


class GraphEngine:
    """Manage a graph of :class:`PlaceNode` instances and their connections."""

    def __init__(self) -> None:
        self._nodes: Dict[str, PlaceNode] = {}
        self._edges: Dict[str, List[PlaceEdge]] = defaultdict(list)

    def add_node(self, node: PlaceNode) -> None:
        """Add a new node to the graph.

        Parameters
        ----------
        node:
            The :class:`PlaceNode` to add.

        Raises
        ------
        ValueError
            If a node with the same ``id`` already exists.
        """
        if node.id in self._nodes:
            raise ValueError(f"node {node.id!r} already exists")
        self._nodes[node.id] = node

    def remove_node(self, node_id: str) -> None:
        """Remove a node and all connected edges from the graph."""
        if node_id in self._nodes:
            del self._nodes[node_id]
            self._edges.pop(node_id, None)
            for edges in self._edges.values():
                edges[:] = [e for e in edges if e.target_id != node_id]

    def add_edge(self, edge: PlaceEdge) -> None:
        """Add an edge connecting two existing nodes.

        Parameters
        ----------
        edge:
            The :class:`PlaceEdge` to add.

        Raises
        ------
        KeyError
            If ``source_id`` or ``target_id`` does not reference a known node.
        """
        if edge.source_id not in self._nodes:
            raise KeyError(f"unknown source node {edge.source_id!r}")
        if edge.target_id not in self._nodes:
            raise KeyError(f"unknown target node {edge.target_id!r}")
        self._edges[edge.source_id].append(edge)

    def remove_edge(self, source_id: str, target_id: str) -> None:
        """Remove a directed edge from the graph."""
        edges = self._edges.get(source_id)
        if not edges:
            return
        self._edges[source_id] = [e for e in edges if e.target_id != target_id]

    def neighbors(self, node_id: str) -> Iterable[PlaceNode]:
        """Yield all neighbor nodes connected to ``node_id``."""
        for edge in self._edges.get(node_id, []):
            target = self._nodes.get(edge.target_id)
            if target:
                yield target

    def shortest_path(
        self, source_id: str, target_id: str
    ) -> Optional[Tuple[float, List[str]]]:
        """Return the shortest path using edge ``distance`` as cost.

        Parameters
        ----------
        source_id:
            Starting node identifier.
        target_id:
            Destination node identifier.

        Returns
        -------
        Optional[Tuple[float, List[str]]]
            A pair of ``(total_distance, [node_ids])`` representing the path.
            Returns ``None`` if ``source_id`` or ``target_id`` does not exist or
            if no path is found.
        """
        if source_id not in self._nodes or target_id not in self._nodes:
            return None

        queue: List[Tuple[float, str, List[str]]] = [(0.0, source_id, [source_id])]
        visited: Dict[str, float] = {source_id: 0.0}

        while queue:
            dist, current_id, path = heappop(queue)
            if current_id == target_id:
                return dist, path
            for edge in self._edges.get(current_id, []):
                next_id = edge.target_id
                new_dist = dist + edge.distance
                if new_dist < visited.get(next_id, float("inf")):
                    visited[next_id] = new_dist
                    heappush(queue, (new_dist, next_id, path + [next_id]))
        return None
