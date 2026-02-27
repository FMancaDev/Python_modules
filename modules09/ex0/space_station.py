from pydantic import BaseModel, Field, ValidationError
from Typing import Optional, Any
from Datetime import Datetime

class SpaceStation(BaseModel):
    station_str: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field()
    power_level: floar = Field()
    oxygen_level: float = Field()
    last_maintenance: Datetime = Field()
    is_operational: bool = Field(default=True)
    notes: Optional = Field = ()


def main():
    try:
        print("Space Station Data Validation")
        print("========================================")
        print("Valid station created:")
