from enum import Enum
from datetime import datetime
from typing import List
from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission_safety(self) -> 'SpaceMission':
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        has_leader = any(
            m.rank in [Rank.captain, Rank.commander] for m in self.crew)
        if not has_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            exp_members = [m for m in self.crew if m.years_experience >= 5]
            if len(exp_members) < len(self.crew) / 2:
                raise ValueError(
                    "Long missions need 50% experienced crew (5+ years)"
                )

        # All crew members must be active
        if not all(m.is_active for m in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main():
    print("Space Mission Crew Validation")
    print("=" * 41)

    try:
        crew_data = [
            {"member_id": "C01", "name": "Sarah Connor", "rank": "commander",
             "age": 45, "specialization": "Mission Command",
             "years_experience": 20},
            {"member_id": "C02", "name": "John Smith", "rank": "lieutenant",
             "age": 30, "specialization": "Navigation", "years_experience": 7},
            {"member_id": "C03", "name": "Alice Johnson", "rank": "officer",
             "age": 25, "specialization": "Engineering", "years_experience": 3}
        ]
        valid_mission = {
            "mission_id": "M2026_MARS",
            "mission_name": "Mars Colony Establishment",
            "destination": "Mars",
            "launch_date": "2026-06-15T10:00:00",
            "duration_days": 900,
            "budget_millions": 2500.0,
            "crew": crew_data
        }

        mission = SpaceMission(**valid_mission)
        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for m in mission.crew:
            print(f"- {m.name} ({m.rank.value}) - {m.specialization}")

    except ValidationError as e:
        print(f"Unexpected error: {e}")

    print("=" * 41)

    # testes invalidos
    print("\nExpected validation error:")
    try:
        SpaceMission(
            mission_id="M_FAIL",
            mission_name="Unsafe Mission",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=10,
            budget_millions=100.0,
            crew=[{
                "member_id": "C99", "name": "Trainee", "rank": "cadet",
                "age": 19, "specialization": "Janitor", "years_experience": 0
            }]
        )
    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
