def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    try:
        if plant_name is None:
            raise ValueError("Plant name cannot be empty!\n")
        elif water_level > 10:
            raise ValueError(f"Water level {water_level}"
                             "is too high (max 10)\n")
        elif water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)\n")
        elif sunlight_hours > 12:
            raise ValueError(f"Sunlight hours {sunlight_hours}"
                             "is too high (max 12)\n")
        elif sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours}"
                             "is too low (min 2)\n")
        print(f"Plant '{plant_name}' is healthy!\n")
    except ValueError as e:
        print(f"Error: {e}")


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    check_plant_health("tomato", 3, 8)
    print("Testing empty plant name...")
    check_plant_health(None, 3, 8)
    print("Testing bad water level...")
    check_plant_health("tomato", 15, 8)
    print("Testing bad sunlight hours...")
    check_plant_health("tomato", 3, 0)
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
