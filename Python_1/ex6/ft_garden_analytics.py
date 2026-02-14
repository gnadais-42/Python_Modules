class Plant:
    def __init__(self, name, height):
        self._name = name
        self._height = height
        self._growth = 0

    def name(self):
        return self._name

    def get_height(self):
        return self._height

    def growth(self):
        return self._growth

    def grow(self):
        print(f"{self.name()} grew 1 cm")
        self._growth += 1
        self._height += 1

    def display_info(self):
        print(f"- {self.name()}: ({self._height})cm")

class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self._color = color

    def get_color(self):
        return self._color

    def display_info(self):
              print(f"- {self.name()}: {self.get_height()}cm, "
                    f"{self.get_color()} flowers (blooming)")

class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, points):
        super().__init__(name, height, color)
        self._points = points

    def get_points(self):
        return self._points

    def display_info(self):
              print(f"- {self.name()}: {self.get_height()}cm, "
                    f"{self.get_color()} flowers (blooming), "
                    f"Prize points: {self.get_points()}")

class GardenManager:
    _gardens = []
    
    def __init__(self, name):
        self._name = name
        self._plants = []

    def name(self):
        return self._name

    def plants(self):
        return self._plants

    def add_plant(self, plant):
        self._plants.append(plant)
        print(f"Added {plant.name()} to {self.name()}'s garden")

    @classmethod
    def create_garden_network(cls, garden_list):
        for garden in garden_list:
            cls._gardens.append(garden)

    @classmethod
    def gardens(cls):
        return cls._gardens

    class GardenStats:
        @staticmethod
        def total_growth(garden):
            total = 0
            for plant in garden._plants:
                total += plant.growth()
            return total

        @staticmethod
        def total_height(garden):
            total = 0
            for plant in garden._plants:
                total += plant.get_height()
            return total

        @staticmethod
        def info(garden):
            print(f"Plants added: {len(garden.plants())},",
                  "Total growth:", 
                  GardenManager.GardenStats.total_growth(garden))

    def grow_all(self):
        print(f"{self.name()} is helping all plants grow...")
        for plant in self.plants():
            plant.grow()

    def report(self):
        print(f"=== {self.name()}'s Garden Report ===")
        for plant in self.plants():
            plant.display_info()

    def score(self):
        total = 0
        for plant in self.plants():
            if isinstance(plant, PrizeFlower):
                total += plant.get_points()
        return total

    @classmethod
    def all_scores(cls):
        print("Garden scores - ", end="")
        first = True
        for garden in cls.gardens():
            if not first:
                print(", ", end="")
            print(f"{garden.name()}: {garden.score()}", end="")
            first = False
        print()


print("=== Garden Management System Demo ===\n")
manager = GardenManager
Alice = GardenManager("Alice")
Bob = GardenManager("Bob")
manager.create_garden_network([Alice, Bob])
Alice.add_plant(Plant("Oak Tree", 101))
Alice.add_plant(FloweringPlant("Rose", 26, "red"))
Alice.add_plant(PrizeFlower("Sunflower", 51, "yellow", 10))
print()
Alice.grow_all()
print()
Alice.report()
print()
manager.GardenStats.info(Alice)
Alice.all_scores()
print("Total gardens managed:", len(GardenManager.gardens()))




