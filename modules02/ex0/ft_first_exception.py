#! /usr/bin/env python3

def check_temperature(temp_str: str) -> None:
    print(f"Testing temperature: {temp_str}")
    try:
        tmp = int(temp_str)
        if tmp >= 0 and tmp <= 40:
            print(f"Temperature {tmp}°C is perfect for plants!\n")
        elif tmp >= 100:
            print(f"Error: {tmp}°C is too hot for plants (max 40°C)\n")
        elif tmp < 0:
            print(f"Error: {tmp}°C is too cold for plants (min 0°C)\n")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")


def test_temperature_input():
    print("=== Garden Temperature Checker ===\n")

    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    check_temperature("100", "-50")
    check_temperature("")


if __name__ == "__main__":
    test_temperature_input()
