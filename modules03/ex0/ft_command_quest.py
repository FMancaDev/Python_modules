#! /usr/bin/env python3

import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    argc = len(sys.argv)
    if argc < 2:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    if argc >= 2:
        print(f"Arguments received: {argc - 1}")
        j = 1
        while j < argc:
            print(f"Argument {j}: {sys.argv[j]}")
            j += 1
    print(f"Total arguments: {argc}")
