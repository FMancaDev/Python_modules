#! /usr/bin/env python3

import sys

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    try:
        id = input("Input Stream active. Enter archivist ID: ")
        stats = input("Input Stream active. Enter status report: ")
    except KeyboardInterrupt:
        print("\nError: keyboard interrupt, try again", file=sys.stderr)
    else:
        print(f"\n{{[}}STANDARD{{]}} Archive status from {id}: {stats}")
        print(
            "{[}ALERT{]} System diagnostic: Communication channels verified",
            file=sys.stderr
        )
        print("{[}STANDARD{]} Data transmission complete\n")

        print("Three-channel communication test successful.")
