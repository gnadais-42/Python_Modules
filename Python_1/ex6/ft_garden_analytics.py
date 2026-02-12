class Plant:
    def __init__(self, name, height=0):
        self._name = name
        self._height = height

    def grow(self):
        self._height += 1
        print(f"{self._name} grew 1cm")

    def get_info(self):
        return f"{self._name}: {self._height}cm"

    def get_height(self):
        return self._height


class FloweringPlant(Plant):
    def __init__(self, name, height=0, color="red"):
        super().__init__(name, height)
        self._color = color
        self._blooming = True

    def bloom_info(self):
        return f"{self._color} flowers (blooming)" if self._blooming else "not blooming"

    def get_info(self):
        return f"{self._name}: {self._height}cm, {self.bloom_info()}"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height=0, color="yellow", prize_points=10):
        super().__init__(name, height, color)
        self._prize_points = prize_points

    def get_info(self):
        return f"{super().get_info()}, Prize points: {self._prize_points}"


class GardenManager:
    _total_gardens = 0
    _scores = {}

    class GardenStats:
        @staticmethod
        def count_plants(plants):
            return len(plants)

        @staticmethod
        def total_growth(plants):
            growth = 0
            for plant in plants:
                growth += plant.get_height()
            return growth

        @staticmethod
        def count_plant_types(plants):
            types = {"regular": 0, "flowering": 0, "prize": 0}
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    types["prize"] += 1
                elif isinstance(plant, FloweringPlant):
                    types["flowering"] += 1
                else:
                    types["regular"] += 1
            return types

    def __init__(self, gardener_name):
        self._gardener_name = gardener_name
        self._plants = []
        GardenManager._total_gardens += 1
        GardenManager._scores[self._gardener_name] = 0

    def add_plant(self, plant):
        self._plants.append(plant)
        print(f"Added {plant._name} to {self._gardener_name}'s garden")
        GardenManager._scores[self._gardener_name] += 50  # arbitrary score

    def grow_all(self):
        print(f"{self._gardener_name} is helping all plants grow...")
        for plant in self._plants:
            plant.grow()

    def report(self):
        print(f"=== {self._gardener_name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self._plants:
            print("-", plant.get_info())
        stats = GardenManager.GardenStats
        print(f"Plants added: {stats.count_plants(self._plants)}, Total growth: "
              f"{stats.total_growth(self._plants)}cm")
        types = stats.count_plant_types(self._plants)
        print(f"Plant types: {types['regular']} regular, {types['flowering']} flowering, "
              f"{types['prize']} prize flowers")

    @classmethod
    def create_garden_network(cls):
        print(f"Total gardens managed: {cls._total_gardens}")

    @staticmethod
    def validate_height(plant):
        return plant.get_height() >= 0

    @classmethod
    def print_scores(cls):
        print("Garden scores -", ", ".join(f"{name}: {score}" for name, score in cls._scores.items()))


# Demo / usage
def ft_garden_analytics():
    print("=== Garden Management System Demo ===")

    alice_garden = GardenManager("Alice")
    bob_garden = GardenManager("Bob")

    # Add plants
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    # Grow all plants
    alice_garden.grow_all()

    # Report
    alice_garden.report()
    print("Height validation test:", GardenManager.validate_height(oak))

    # Bob's garden
    bob_garden.add_plant(Plant("Pine", 50))
    bob_garden.add_plant(FloweringPlant("Lily", 20, "white"))

    # Scores and total gardens
    GardenManager.print_scores()
    GardenManager.create_garden_network()


if __name__ == "__main__":
    ft_garden_analytics()
