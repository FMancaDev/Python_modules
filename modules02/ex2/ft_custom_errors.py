#! /usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def kill_tomato_plant():
    raise PlantError("The tomato plant is wilting!")


def empty_water_tank():
    raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        kill_tomato_plant()
    except PlantError as erro:
        print(f"Caught PlantError: {erro}\n")

    print("Testing waterError...")
    try:
        empty_water_tank()
    except WaterError as erro:
        print(f"Caught WaterErro: {erro}\n")

    print("Testing catching all garden errors...")
    try:
        kill_tomato_plant()
    except PlantError as erro:
        print(f"Caught a garden error: {erro}")
    try:
        empty_water_tank()
    except WaterError as erro:
        print(f"Caught a garden error: {erro}")
