class PlantError(Exception):
    pass


def water_plants(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant not in ("tomato", "lettuce", "carrots"):
                raise PlantError
            print(f"Watering {plant}")
    except PlantError:
        print(f"Error: Cannot water {plant} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)\n")


def test_watering_system():
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Testing with error...")
    water_plants(["tomato", None, "carrots"])
    print("Cleanup always happens, even with errors!")
