from pydantic import Field, ValidationError, BaseModel, model_validator
from datetime import datetime
from enum import Enum
from typing import Self

class Rank(Enum):
    cadet: str = "cadet"
    officer: str = "officer"
    lieutenant: str = "lieutenant"
    captain: str = "captain"
    commander: str = "commander"

    def __str__(self):
        return self.value


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True

    def __str__(self) -> str:
        return f"{self.name} ({self.rank}) - {self.specialization}"


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def check_id(self) -> Self:
        if not self.mission_id.startswith('M'):
            raise ValueError('Mission ID must start with "M"')
        return self
    
    @model_validator(mode='after')
    def check_commader_or_captain(self) -> Self:
        for member in self.crew:
            if member.rank == Rank.captain or member.rank == Rank.commander:
                return self
        raise ValueError("Must have at least one Commander or Captain")
    
    @model_validator(mode='after')
    def check_duration(self) -> Self:
        if self.duration_days > 365:
            experienced: int = 0
            for member in self.crew:
                experienced += 1 if member.years_experience >= 5 else 0
            if experienced < len(self.crew) / 2:
                raise ValueError("Long missions (> 365 days) need 50% experienced crew (5+ years)")
        return self
    
    @model_validator(mode='after')
    def check_active_members(self) -> Self:
        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")
        return self
    

def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")

    try:
        mission_valid = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            budget_millions=2500,
            crew=[CrewMember(
                    member_id="CM-0",
                    name="Sarah Connor",
                    rank=Rank.commander,
                    age=29,
                    specialization="Mission Command",
                    years_experience=8
                ),
                CrewMember(
                    member_id="CM-1",
                    name="John Smith",
                    rank=Rank.lieutenant,
                    age=26,
                    specialization="Navigation",
                    years_experience=6
                ),
                CrewMember(
                    member_id="CM-2",
                    name = "Alice Johnson",
                    rank = Rank.officer,
                    age=25,
                    specialization="Engineering",
                    years_experience=3
                )
            ]
        )
        print(
            "Mission:", mission_valid.mission_name,
            "\nID:", mission_valid.mission_id,
            "\nDestination:", mission_valid.destination, "days",
            "\nBudget:", mission_valid.budget_millions, "M",
            "\nCrew size:", len(mission_valid.crew),
        )
        print("Crew members:")
        for member in mission_valid.crew:
            print("-", member)
    except ValidationError as e:
        print(e)
    print("\n=========================================")
    try:
        mission_invalid = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            budget_millions=2500,
            crew=[CrewMember(
                    member_id="CM-0",
                    name="Sarah Connor",
                    rank=Rank.commander,
                    age=29,
                    specialization="Mission Command",
                    years_experience=8
                ),
                CrewMember(
                    member_id="CM-1",
                    name="John Smith",
                    rank=Rank.lieutenant,
                    age=26,
                    specialization="Navigation",
                    years_experience=6
                ),
                CrewMember(
                    member_id="CM-2",
                    name = "Alice Johnson",
                    rank = Rank.officer,
                    age=25,
                    specialization="Engineering",
                    years_experience=3
                ),
                CrewMember(
                    member_id="CM-3",
                    name = "whatever",
                    rank = Rank.officer,
                    age=25,
                    specialization="whatever",
                    years_experience=3,
                    is_active=False
                )
            ]
        )
    except ValidationError as e:
        print(f"Expected validation error:\n{e.errors()[0]["msg"]}")


if __name__ == "__main__":
    main()