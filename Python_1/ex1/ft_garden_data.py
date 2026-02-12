class Plant:
    def __init__(self, name, height, age):
        self._name = name
        self._height = height
        self._age = age


def ft_garden_data():
    plant1 = Plant("Margarida", 100, 35)
    plant2 = Plant("Malmequer", 20, 7)

    print(f"""=== Garden Plant Registry ===
{plant1.name}: {plant1.height} cm, {plant1.age} days old
{plant2.name}: {plant2.height} cm, {plant2.age} days old""")
