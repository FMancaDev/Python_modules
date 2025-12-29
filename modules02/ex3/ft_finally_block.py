#! /usr/bin/env python3

def water_plants(plant_list):
    print("Opening watering system")
    error = False
    try:
        for plant in plant_list:
            if plant is None:
                print(f"Error: cannot water '{plant}' - invalid plant!")
                error = True
                break
            print(f"watering {plant}")
    finally:
        print("Closing watering system (cleanup)")
    if not error:
        print("Watering completed successfuly!")


def test_watering_system():
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])

    print("\nTesting with error...")
    water_plants(["tomato", None])

    print("\nCleanup always happens, even with error!")


if __name__ == "__main__":
    test_watering_system()
