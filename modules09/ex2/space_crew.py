from enum import Enum
from pydantic import BaseModel, Field, ValidationError
from typing import Optional
from datetime import datetime


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    menber_id: str = Field(min_length=3)
    name: str = Field()
    rank: Rank = Field()
    age: int = Field(ge=18, le=80)
    specialization: str = Field()
