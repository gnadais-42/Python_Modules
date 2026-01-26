class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def test_PlantError():
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato is wilting!")
    except PlantError as e:
        print(f"Caught a PlantError: {e}\n")


def test_WaterError():
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught a WaterError: {e}\n")


def test_GardenError():
    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}\n")


def test_custom_errors():
    print("=== Custom Garden Errors Demo===\n")
    test_PlantError()
    test_WaterError()
    test_GardenError()
    print("All custom error types work correctly!")
