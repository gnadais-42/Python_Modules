class Plant:
    def __init__(self, name, height):
        self._name = name
        self._height = height
        self._age = age
        self._growth = 0

    def name():
        return self._name()

    def get_height(self):
        return self._height

    def grow(self):
        print(f"{self.name()} grew 1 cm")
        self._growth += 1
        self._height += 1

    def display_info(self):
        print(f"- {self.name()}: ({self._height}cm")

class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        self._name = name
        self._height = height
        self._age = age
        self._color = color

    def get_color(self):
        return self._color

    def display_info(self):
              print(f"- {self.name()}: {self.get_height()}cm, "
                    f"{self.get_color()} flowers (blooming)")

class PrizeFlower(FLoweringPlant):
    def __init__(self, name, height, color, points):
        self._name = name
        self._height = height
        self._age = age
        self._color = color
        self._points = points

    def get_points(self):
        return self._points

    def display_info(self):
              print(f"- {self.name()}: {self.get_height()}cm, "
                    f"{self.get_color()} flowers (blooming), "
                    f"Prize points: {self.get_points()}")

class GardenManager:
    _total_gardens = 0
    
    def __init__(self, name):
        self._name = name
        self._plants = []

    def get_name(self):
        return self._name

    class GardenStats:
        @staticmethod
        def total_growth(garden)






