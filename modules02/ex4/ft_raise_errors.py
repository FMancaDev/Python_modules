#! /usr/bin/env python3

def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int):
    try:
        if plant_name == "" or plant_name is None:
            raise ValueError("Error: Plant name cannot be empty!")
        if water_level < 1:
            raise ValueError(f"Error: water level {water_level}"
                             " is too level (min 1)")
        elif water_level > 10:
            raise ValueError(f"Error: water level {water_level}"
                             " is too high (max 10)")
        if sunlight_hours < 2:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours}"
                             "is too low (min 2)")
        elif sunlight_hours > 12:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours}"
                             "is too high (max 12)")
        print(f"Plant '{plant_name}' is healthy!")
    except ValueError as erro:
        print(f"{erro}")


def test_plant_checks():
    print("=== Garden Plant Health Checker ===\n")

    good_values = [
        ["tomato", 5, 12],
        ["banana", 10, 7],
        ["couves", 1, 4]
    ]
    print("Testing good values")
    for item in good_values:
        check_plant_health(item[0], item[1], item[2])

    print("\nTesting empty plant name...")
    check_plant_health("", 5, 8)

    print("\ntesting bad water level...")
    check_plant_health("bom_dia", 12, 5)

    print("\nTesting bad sunlight hours...")
    check_plant_health("boa_tarde", 6, 13)

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
