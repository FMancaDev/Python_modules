#! /usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1

    def age_up(self):
        self.age += 1

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"


plant1 = Plant("Rose", 25, 30)

inicial_height = plant1.height

print("=== Day 1 ===")
print(plant1.get_info())

dias_a_passar = 6
i = 0

while i < dias_a_passar:
    plant1.grow()
    plant1.age_up()
    i += 1

print("=== Day 7 ===")
print(plant1.get_info())

crescimento = plant1.height - inicial_height
print(f"Growth this week: +{crescimento}cm")
