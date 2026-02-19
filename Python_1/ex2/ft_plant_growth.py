class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name: str = name
        self._height: int = height
        self._age: int = age

    def grow(self) -> None:
        self._height += 1

    def age(self) -> None:
        self._age += 1

    def get_info(self, day: int) -> None:
        if day < 1:
            return
        print(f"""=== Day {day} ===
{self._name}: {self._height}cm, {self._age} days old""")


def ft_plant_growth() -> None:
    plant: Plant = Plant("Rose", 25, 30)
    initial_height: Plant = plant._height
    plant.get_info(1)
    for _ in range(6):
        plant.grow()
        plant.age()
    plant.get_info(7)
    print(f"Growth this week: +{plant._height - initial_height}cm")


if __name__ == "__main__":
    ft_plant_growth()
