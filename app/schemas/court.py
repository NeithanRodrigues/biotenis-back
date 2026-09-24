from decimal import Decimal
from typing import Optional
from pydantic import BaseModel

class CourtIn(BaseModel):
    number: int 
    description: Optional[str] = None 
    price_per_hour: Decimal 

class CourtOut(BaseModel):
    number: int
    description: Optional[str] = None
    price_per_hour: Decimal
