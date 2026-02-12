class Plant:
    def __init__(self, name, height, age):
        self._name = name
        self._height = height
        self._age = age

    def grow(self):
        self._height += 1

    def age(self):
        self._age += 1

    def get_info(self, day):
        if day < 1:
            return
        print(f"""=== Day {day} ===
{self._name}: {self._height}cm, {self._age} days old""")


def ft_plant_growth():
    plant = Plant("Rose", 25, 30)
    initial_height = plant._height
    plant.get_info(1)
    for _ in range(6):
        plant.grow()
        plant.age()
    plant.get_info(7)
    print(f"Growth this week: +{plant._height - initial_height}cm")
