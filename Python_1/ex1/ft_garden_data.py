class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name: str = name
        self._height: str = height
        self._age: str = age


def ft_garden_data() -> None:
    plant1: Plant = Plant("Margarida", 100, 35)
    plant2: Plant = Plant("Malmequer", 20, 7)

    print(f"""=== Garden Plant Registry ===
{plant1._name}: {plant1._height} cm, {plant1._age} days old
{plant2._name}: {plant2._height} cm, {plant2._age} days old""")


if __name__ == "__main__":
    ft_garden_data()
