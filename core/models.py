"""Domain models for the WanderTopo travel graph."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


@dataclass
class PlaceNode:
    """A point of interest (POI) in the travel graph.

    Attributes
    ----------
    id:
        Unique identifier used to reference the node in the graph.
    name:
        Human friendly name of the place.
    latitude:
        Geographic latitude in decimal degrees.
    longitude:
        Geographic longitude in decimal degrees.
    rating:
        Optional user rating or popularity score in the range ``0-5``.
    categories:
        Tags classifying the place (e.g. ``["restaurant", "museum"]``).
    metadata:
        Arbitrary extra information associated with this node.
    """

    id: str
    name: str
    latitude: float
    longitude: float
    rating: Optional[float] = None
    categories: List[str] = field(default_factory=list)
    metadata: Dict[str, str] = field(default_factory=dict)

    def coordinates(self) -> Tuple[float, float]:
        """Return geographic coordinates as a ``(lat, lon)`` tuple."""
        return self.latitude, self.longitude


@dataclass
class PlaceEdge:
    """Relationship between two :class:`PlaceNode` objects.

    Attributes
    ----------
    source_id:
        Identifier of the origin node.
    target_id:
        Identifier of the destination node.
    distance:
        Distance between the nodes in meters.
    weight:
        Relative strength or importance of the connection.
    relationship_type:
        Optional description of the relationship (e.g. ``"nearby"``).
    metadata:
        Arbitrary extra information associated with this edge.
    """

    source_id: str
    target_id: str
    distance: float
    weight: float = 1.0
    relationship_type: Optional[str] = None
    metadata: Dict[str, str] = field(default_factory=dict)

    def is_self_loop(self) -> bool:
        """Return ``True`` if the edge connects a node to itself."""
        return self.source_id == self.target_id
