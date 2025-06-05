"""Domain models for the WanderTopo travel graph."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple


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
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validate attribute values after initialization."""
        if not -90 <= self.latitude <= 90:
            raise ValueError(f"latitude {self.latitude!r} out of range")
        if not -180 <= self.longitude <= 180:
            raise ValueError(f"longitude {self.longitude!r} out of range")
        if self.rating is not None and not 0 <= self.rating <= 5:
            raise ValueError(f"rating {self.rating!r} must be between 0 and 5")

    def coordinates(self) -> Tuple[float, float]:
        """Return geographic coordinates as a ``(lat, lon)`` tuple."""
        return self.latitude, self.longitude

    def to_dict(self) -> Dict[str, Any]:
        """Serialize this node to a dictionary for storage or transport."""
        return {
            "id": self.id,
            "name": self.name,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "rating": self.rating,
            "categories": list(self.categories),
            "metadata": dict(self.metadata),
        }


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
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Ensure distance and weight are valid."""
        if self.distance < 0:
            raise ValueError("distance must be non-negative")
        if self.weight <= 0:
            raise ValueError("weight must be positive")

    def is_self_loop(self) -> bool:
        """Return ``True`` if the edge connects a node to itself."""
        return self.source_id == self.target_id

    def reversed_edge(self) -> "PlaceEdge":
        """Return a new edge with source and target swapped."""
        return PlaceEdge(
            source_id=self.target_id,
            target_id=self.source_id,
            distance=self.distance,
            weight=self.weight,
            relationship_type=self.relationship_type,
            metadata=dict(self.metadata),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize this edge to a dictionary."""
        return {
            "source_id": self.source_id,
            "target_id": self.target_id,
            "distance": self.distance,
            "weight": self.weight,
            "relationship_type": self.relationship_type,
            "metadata": dict(self.metadata),
        }
