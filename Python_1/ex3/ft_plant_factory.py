class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name: str = name
        self._height: int = height
        self._age: int = age

    def display_info(self) -> None:
        print(f"{self._name}, ({self._height}cm, {self._age} days)")


def ft_plant_factory() -> None:
    plant_data: list = [("Rose", 25, 30),
                        ("Oak", 200, 365),
                        ("Cactus", 5, 90),
                        ("Sunflower", 80, 45),
                        ("Fern", 15, 120)]
    plants = []
    print("===Plant Factory Output===")
    count: int = 0
    for data in plant_data:
        plant: Plant = Plant(data[0], data[1], data[2])
        plants.append(plant)
        count += 1
        print("Created: ", end="")
        plant.display_info()
    print(f"\nTotal plants created: {count}")


if __name__ == "__main__":
    ft_plant_factory()
