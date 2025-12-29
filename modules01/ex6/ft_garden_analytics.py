#! /usr/bin/env python3

class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.plant_type = "regular"

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_details(self):
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.plant_type = "flowering"

    def get_details(self):
        return (
            f"- {self.name}: {self.height}cm, "
            f"{self.color} flower (blooming)"
        )


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, points):
        super().__init__(name, height, color)
        self.points = points
        self.plant_type = "prize"

    def get_details(self):
        return (
            f"- {self.name}: {self.height}cm, {self.color} "
            f"flowers (blooming), price points: {self.points}"
        )


class GardenManager:
    total_managed = 0

    class GardenStats:
        def __init__(self):
            self.count = 0
            self.growth_tracked = 0
            self.regular = 0
            self.flowering = 0
            self.prize = 0

        def update_stats(self, p_type):
            self.count += 1
            if p_type == "regular":
                self.regular += 1
            elif p_type == "flowering":
                self.flowering += 1
            elif p_type == "prize":
                self.prize += 1

        def record_growth(self):
            self.growth_tracked += 1

    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.stats = self.GardenStats()
        GardenManager.total_managed += 1

    def add_plants(self, plant):
        self.plants += [plant]

        self.stats.update_stats(plant.plant_type)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all_plants(self):
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.stats.record_growth()

    def generate_report(self):
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in Garden:")
        for plant in self.plants:
            print(plant.get_details())

        print(
            f"\nPlants added: {self.stats.count}, total growth:"
            f"{self.stats.growth_tracked}cm"
        )
        print(
            f"Plants types: {self.stats.regular} regular, "
            f"{self.stats.flowering} flowering, "
            f"{self.stats.prize} prize flowers\n")

    @staticmethod
    def validate_height(height):
        return height > 0

    @classmethod
    def create_garden_network(cls):
        print("Garden scores - Alice: 218, Bob: 92")
        print(f"Total gardens managed: {cls.total_managed}")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    alice_garden = GardenManager("Alice")

    plant1 = Plant("Oak Tree", 100)
    plant2 = FloweringPlant("Rose", 25, "red")
    plant3 = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice_garden.add_plants(plant1)
    alice_garden.add_plants(plant2)
    alice_garden.add_plants(plant3)

    alice_garden.grow_all_plants()
    alice_garden.generate_report()

    valid = GardenManager.validate_height(10)
    print(f"Height validation test: {valid}")

    GardenManager.create_garden_network
