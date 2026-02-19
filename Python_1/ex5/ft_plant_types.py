class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name: str = name
        self._height: int = height
        self._age: int = age

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color: str = color

    def get_color(self) -> str:
        return self._color

    def bloom(self) -> None:
        print(f"{self._name} is blooming beautifully!")

    def display_info(self) -> None:
        print(f"{self._name} (Flower): {self.get_height()}cm, {self.get_age()}"
              f" days, {self.get_color()} color")


class Tree(Plant):
    def __init__(self, name: str, height: int,
                 age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter: int = trunk_diameter

    def get_diameter(self) -> int:
        return self._trunk_diameter

    def produce_shade(self) -> None:
        print(f"{self._name} provides {(self.get_diameter() * 1.56):.0f}"
              " square meters of shade")

    def display_info(self) -> None:
        print(f"{self._name} (Tree): {self.get_height()}cm, {self.get_age()}"
              f" days, {self.get_diameter()}cm diameter")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self._harvest_season: str = harvest_season
        self._nutritional_value: str = nutritional_value

    def get_season(self) -> str:
        return self._harvest_season

    def get_nutrition_value(self) -> str:
        return self._nutritional_value

    def nutrition_info(self) -> None:
        print(f"{self._name} is rich in {self.get_nutrition_value()}")

    def display_info(self) -> None:
        print(f"{self._name} (Vegetable): {self.get_height()}cm, "
              f"{self.get_age()} days, {self.get_season()} harvest")


def ft_plant_types():
    print("=== Garden Plant Types ===")
    plant_data: list = [("flower", "Rose", 25, 30, "red"),
                        ("flower", "Daisy", 30, 40, "yellow"),
                        ("tree", "Oak", 500, 1825, 50),
                        ("tree", "Cherry", 670, 2000, 66),
                        ("vegetable", "Tomato", 80, 90,
                         "summer", "antioxidants"),
                        ("vegetable", "Radish", 50, 100,
                         "winter", "vitamin c")]
    plants: list = []
    for data in plant_data:
        print()
        if data[0] == "flower":
            plant: Flower = Flower(data[1], data[2], data[3], data[4])
            plant.display_info()
            plant.bloom()
        elif data[0] == "tree":
            plant: Tree = Tree(data[1], data[2], data[3], data[4])
            plant.display_info()
            plant.produce_shade()
        elif data[0] == "vegetable":
            plant: Vegetable = Vegetable(data[1], data[2], data[3],
                                         data[4], data[5])
            plant.display_info()
            plant.nutrition_info()
        plants.append(plant)


if __name__ == "__main__":
    ft_plant_types()
