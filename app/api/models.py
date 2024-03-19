from pydantic import BaseModel
from typing import List, Optional


class DeliveryIn(BaseModel):
    name: str
    description: str
    count_users: int
    city: str
    restaurants_id: List[int]


class DeliveryOut(DeliveryIn):
    id: int


class DeliveryUpdate(DeliveryIn):
    name: Optional[str] = None
    description: Optional[str] = None
    count_users: Optional[int] = None
    city: Optional[str] = None
    restaurants_id: Optional[List[int]] = None