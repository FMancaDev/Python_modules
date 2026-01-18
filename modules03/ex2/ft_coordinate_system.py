#! /usr/bin/env python3

import sys
import math


def to_tuple(data: list[str], from_argv: bool = False) -> tuple[int]:
    """Creates a tuple from a list or a string."""
    if from_argv:
        return tuple(int(x) for x in data)
    else:
        return tuple(int(x) for x in data.split(','))


def cal_distance(coords: tuple[int]) -> None:
    """Calculates and prints the Euclidean distance."""
    total_squares = 0.0
    for c in coords:
        total_squares += c ** 2
    distance = math.sqrt(total_squares)
    print(f"Distance between (0, 0, 0) and {coords}: {distance:.2f}")


def args_coords() -> None:
    """Handles coordinate creation from command-line arguments."""
    try:
        if len(sys.argv) == 1:
            coords = (10, 20, 5)
        else:
            coords = to_tuple(sys.argv[1:4], from_argv=True)
        print(f"\nPosition created: {coords}")
        cal_distance(coords)
    except ValueError:
        print("Input arguments can only be numbers.\n")


def parse_strings(coord_list: list[str]) -> None:
    """Parses a list of coordinate strings and calculates distances."""
    for c in coord_list:
        try:
            coords = to_tuple(c, from_argv=False)
            print(f'\nParsing coordinates: "{c}"')
            print(f"Parsed position: {coords}")
            cal_distance(coords)
        except ValueError as e:
            print(f'\nParsing invalid coordinates: "{c}"')
            print(f"Error parsing coordinates: {e}")
            print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")


def unpack_demonstration() -> None:
    """Demonstrates tuple unpacking functionality."""
    coords = (3, 4, 0)
    x, y, z = coords
    print("\nUnpacking demonstration:")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    args_coords()
    coord_strings = ["3,4,0", "abc,def,ghi"]
    parse_strings(coord_strings)
    unpack_demonstration()
