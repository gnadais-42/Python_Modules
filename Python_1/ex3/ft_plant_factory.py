class Plant:
    def __init__(self, name, height, age):
        self._name = name
        self._height = height
        self._age = age

    def display_info(self):
        print(f"{self._name}, ({self._height}cm, {self._age} days)")


def ft_plant_factory():
    plant_data = [("Rose", 25, 30),
                  ("Oak", 200, 365),
                  ("Cactus", 5, 90),
                  ("Sunflower", 80, 45),
                  ("Fern", 15, 120)]
    plants = []
    print("===Plant Factory Output===")
    count = 0
    for data in plant_data:
        plant = Plant(data[0], data[1], data[2])
        plants.append(plant)
        count += 1
        print("Created: ", end="")
        plant.display_info()
    print(f"\nTotal plants created: {count}")
