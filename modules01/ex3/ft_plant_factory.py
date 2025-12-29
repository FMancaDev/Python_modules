#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        return f"{self.name}: ({self.height}cm, {self.age} days old)"


values = [
   ["Rose", 25, 30],
   ["Oak", 200, 365],
   ["Cactus", 5, 90],
   ["Sunflower", 80, 45],
   ["Fern", 15, 120],
   ["teste", -2147483648, 2147483647],
   ["42_school", 2147483649, None],
   ["", 0, 0]
]

print("=== Plant factory Output ===")

count = 0

for data in values:
    new_plant = Plant(data[0], data[1], data[2])
    print(f"Created: {new_plant.get_info()}")
    count += 1
print("")
print(f"Total plants created: {count}")
