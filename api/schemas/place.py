from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class PlaceBase(BaseModel):
    """
    Base schema for place data.
    
    Attributes:
        name (str): Name of the location
        lat (float): Latitude coordinate
        lon (float): Longitude coordinate
        trust_score (float): Normalized trust score (0-1)
    """
    name: str
    lat: float = Field(..., ge=-90, le=90)
    lon: float = Field(..., ge=-180, le=180)
    trust_score: float = Field(..., ge=0, le=1)

class PlaceCreate(PlaceBase):
    """
    Schema for creating a new place.
    Extends PlaceBase with additional creation fields.
    """
    category: str
    description: Optional[str] = None
    tags: List[str] = []

class PlaceResponse(PlaceBase):
    """
    Schema for place response data.
    Extends PlaceBase with additional response fields.
    """
    id: str
    created_at: datetime
    updated_at: datetime
    category: str
    description: Optional[str]
    tags: List[str]

    class Config:
        orm_mode = True 