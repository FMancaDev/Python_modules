#! /usr/bin/env python3

def garden_operations(value_type) -> None:
    """
    Forcing Errors conditions to be caught on test
    """
    if value_type == "bad_input":
        int("non-numeric string")
    elif value_type == "ZeroDivisionError":
        print(10 / 0)
    elif value_type == "FileNotFoundError":
        open("ola.txt")
    elif value_type == "KeyError":
        my_car = {}
        print(my_car["Invalid_Key"])


def test_error_types() -> None:
    """
    Test Errors conditions made manually
    """
    print("=== Garden Error Types Demo ===\n")

    print("Testing ValueError...")
    try:
        garden_operations("bad_input")
    except ValueError as erro:
        print(f"[caught ValueError]: {erro}\n")

    print("Testing ZeroDivisionError...")
    try:
        garden_operations("ZeroDivisionError")
    except ZeroDivisionError as erro:
        print(f"[caught ZeroDivisionError]: {erro}\n")

    print("Testing FileNotFoundError...")
    try:
        garden_operations("FileNotFoundError")
    except FileNotFoundError as erro:
        print(f"[caught FileNotFoundError]: {erro}\n")

    print("Testing KeyError...")
    try:
        garden_operations("KeyError")
    except KeyError as erro:
        print(f"[caught KeyError]: {erro}\n")

    print("Testing multiple errors together...")
    try:
        garden_operations("error_name")
    except (ValueError, ZeroDivisionError, KeyError, FileNotFoundError):
        print("caught an error, but program continues!")

    print("\nAll error types tested successfuly!")


if __name__ == "__main__":
    test_error_types()
