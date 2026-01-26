class GardenError(Exception):
    pass


class SunlightError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(self, name, water_level, sunlight_hours):
        self._name = name
        self._water_level = water_level
        self._sunlight_hours = sunlight_hours

    def get_name(self):
        return self._name

    def get_water_level(self):
        return self._water_level

    def get_sunlight_hours(self):
        return self._sunlight_hours


class GardenManager:
    plants = []

    @classmethod
    def add_plants(cls, plant_list):
        try:
            for plant in plant_list:
                if plant.get_name() is None:
                    raise ValueError("Plant name cannot be empty!")
                cls.plants.append(plant)
                print(f"Added {plant.get_name()} successfully")
            print()
        except ValueError as e:
            print(f"Error adding plant: {e}\n")

    @classmethod
    def water_plants(cls):
        print("Opening watering system")
        try:
            for plant in cls.plants:
                if plant.get_name() is None:
                    raise ValueError("Cannot water None - invalid plant!")
                print(f"Watering {plant.get_name()} - success")
        except ValueError as e:
            print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)\n")

    @staticmethod
    def check_water_level(plant):
        level = plant.get_water_level()
        if level < 1:
            raise WaterError(f"Water level {level} is too low (min 1)")
        elif level > 10:
            raise WaterError(f"Water level {level} is too high (max 10)")

    @staticmethod
    def check_sunlight_hours(plant):
        hours = plant.get_sunlight_hours()
        if hours < 2:
            raise SunlightError(f"Sunlight hours {hours} is too low (min 2)")
        elif hours > 12:
            raise SunlightError(f"Sunlight hours {hours} is too high (max 12)")

    @classmethod
    def check_plant_health(cls):
        try:
            for plant in cls.plants:
                cls.check_water_level(plant)
                cls.check_sunlight_hours(plant)
                print(f"{plant.get_name()}: healthy "
                      f"water: {plant.get_water_level()}, "
                      f"sun: {plant.get_sunlight_hours()}")
            print()
        except GardenError as e:
            print(f"Error checking {plant.get_name()}: {e}\n")


def test_garden_management():
    print("=== Garden Management System ===\n")
    manager = GardenManager()
    plant_list = [Plant("tomato", 5, 8),
                  Plant("lettuce", 15, 9),
                  Plant(None, 3, 10)]
    print("Adding plants to garden...")
    manager.add_plants(plant_list)
    print("Watering plants...")
    manager.water_plants()
    print("Checking plant health...")
    manager.check_plant_health()
    print("Testing error recovery...")
    try:
        raise WaterError("Not enough water in the tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...\n")

    print("Garden management system test complete!")


test_garden_management()





