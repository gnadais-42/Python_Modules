from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation\n"
          "=========================================")
    print("Valid station created:")
    ss1 = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime.now()
    )
    print(
        "ID:", ss1.station_id,
        "\nName:", ss1.name,
        "\nCrew:", ss1.crew_size,
        "\nPower:", ss1.power_level,
        "\nOxygen:", ss1.oxygen_level,
        "\nLast maintenance:", ss1.last_maintenance,
        "\nStatus:", "Operational" if ss1.is_operational else "Not operational"
    )
    print("\n===================================")
    try:
        ss2 = SpaceStation(
            station_id="ISS001",
        name="International Space Station",
        crew_size=0,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime.now()
        )
    except ValidationError as e:
        print(f"Expected validation error:\n{e.errors()[0]['msg']}")
    return


if __name__ == "__main__":
    main()