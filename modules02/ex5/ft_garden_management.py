#! /usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WatterError(GardenError):
    pass


class HealthError(GardenError):
    pass


class GardenManager:
    def __init__(self):
        self.plants = {}

    def add_plant(self, name, water, sun):
        if not name:
            raise PlantError("Plant name cannot be empty!\n")
        if water < 0 or sun < 0:
            raise PlantError("Imvalid plant values")

        self.plants[name] = {"water": water, "sun": sun}
        print("Added", name, "successfully")

    def wwater_plants(self):
        print("Opening watering system")
        try:
            if not self.plants:
                raise WatterError("No plants to water")

            for name in self.plants:
                self.plants[name]["water"] += 1
                print("Watering", name, "- success")
        finally:
            print("Closing watering system (cleanup)\n")

    def check_health(self, name):
        if name not in self.plants:
            raise HealthError("Plant does not exist")

        water = self.plants[name]["water"]
        sun = self.plants[name]["sun"]

        if water > 10:
            raise HealthError(
                "Water level " + str(water) + " is too high (max 10)\n"
            )
        print(name + ": healthy (water:", water, ", sun:", sun, ")")


if __name__ == "__main__":
    print("=== Garden Management Sysem ===\n")

    manager = GardenManager()

    print("Adding plants to garden...")
    try:
        manager.add_plant("cenoura", 5, 8)
        manager.add_plant("alface", 15, 6)
        manager.add_plant("", 3, 4)
    except PlantError as erro:
        print("Error adding plant:", erro)

    print("Watering plants...")
    try:
        manager.wwater_plants()
    except WatterError as erro:
        print("Water error:", erro)

    print("Checking plant health...")
    try:
        manager.check_health("cenoura")
    except HealthError as erro:
        print("Error checking cenoura:", erro)
    try:
        manager.check_health("alface")
    except HealthError as erro:
        print("Error checking cenoura:", erro)

    print("Testing error recovery...")
    try:
        raise GardenError("Not enough water is tank")
    except GardenError as erro:
        print("Caught GardenError:", erro)
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")
