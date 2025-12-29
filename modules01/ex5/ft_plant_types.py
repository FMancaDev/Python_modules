#! /usr/bin/env python3

class Plant:
    def __init__(self, name, height: int = 0, age: int = 0):
        self.name = name
        self.height = height
        self.age = age

    def get_details(self):
        class_name = self.__class__.__name__
        return f"{self.name} ({class_name}): {self.height}cm, {self.age} days"


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def get_details(self):
        basic_details = super().get_details()
        return f"{basic_details}, {self.color} color"

    def bloom(self):
        print(f"{self.name} is blooming beautifully!\n")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def get_details(self):
        basic_details = super().get_details()
        return f"{basic_details}, {self.trunk_diameter}cm diameter"

    def produce_shade(self):
        print(f"{self.name} provides 78 square meters of shade\n")


class Vegetable(Plant):
    def __init__(self, name, height, age, vegetable):
        super().__init__(name, height, age)
        self.vegetable = vegetable

    def get_details(self):
        basic_deatails = super().get_details()
        return f"{basic_deatails}, {self.vegetable}"

    def harvest_season(self):
        return "summer harvest"

    def nutritional_value(self):
        print(f"{self.name} is rich in vitamin C\n")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")

    plant1 = Flower("Rose", 25, 30, "red")
    print(plant1.get_details())
    plant1.bloom()

    plant2 = Tree("Oak", 500, 1825, 50)
    print(plant2.get_details())
    plant2.produce_shade()

    plant3 = Vegetable("Tomato", 80, 90, "summer harvest")
    print(plant3.get_details())
    plant3.nutritional_value()
