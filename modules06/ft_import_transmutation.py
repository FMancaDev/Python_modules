#! /usr/bin/env python3


import alchemy.elements  # full modeule import
from alchemy.elements import create_fire  # specific module import
from alchemy.elements import create_water, create_earth  # multiples imports
from alchemy.potions import healing_potions as hl  # aliased import
from alchemy.potions import strength_potion

if __name__ == "__main__":
    print("\n=== Import Transmutation Mastery ===\n")

    print("Method 1 - Full module import:")
    print("alchemy.elements.create_fire(): "
          f"{alchemy.elements.create_fire()}\n")

    print("Method 2 - Specific function import:")
    print(f"create_water(): {create_water()}\n")

    print("Method 3 - Aliased import:")
    print(f"heal: {hl()}\n")

    print("Method 4 - multiple imports:")
    print(f"create_eartrh(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {strength_potion()}")

    print("\nAll import transmutation methods mastered!")
