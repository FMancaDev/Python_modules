#! /usr/bin/env python3


import sys
import math


def to_tuple(args, is_args):
    if is_args:
        return tuple(int(arg) for arg in args)
    return tuple(int(arg) for arg in args.split(','))


def cal_distance(coords):
    print(f"Distance between (0, 0, 0) and {coords}: "
          f"{math.sqrt(sum(c**2 for c in coords)):.2f}\n")


def args_coords():
    try:
        if len(sys.argv) == 1:
            coords = (10, 20, 5)
        else:
            coords = to_tuple(sys.argv[1:4], True)
        print(f"Position created: {coords}")
        cal_distance(coords)
    except ValueError:
        print("Input arguments can only be numbers, not letters.\n")


def parse_strings(coord_list):
    for c in coord_list:
        try:
            coords = to_tuple(c, False)
            print(f'Parsing coordinates: "{c}"')
            print(f"Parsed position: {coords}")
            cal_distance(coords)
        except ValueError as e:
            print(f'Parsing invalid coordinates: "{c}"')
            print(f"Error parsing coordinates: {e}")
            print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")


def unpack_demonstration():
    coords = (3, 4, 0)
    x, y, z = coords
    print("\nUnpacking demonstration:")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}\n")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    args_coords()

    coord_strings = ["3,4,0", "abc,def,ghi"]
    parse_strings(coord_strings)

    unpack_demonstration()
