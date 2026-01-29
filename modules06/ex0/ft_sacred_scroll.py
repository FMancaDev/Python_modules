#! /usr/bin/env python3

import alchemy
import alchemy.elements

if __name__ == "__main__":
    print("=== Sacred Scroll Mastery: ===\n")

    print("Testing direct module access:")

    print("alchemy.elements.create_fire(): "
          f"{alchemy.elements.create_fire()}")

    print("alchemy.elements.create_water(): "
          f"{alchemy.elements.create_water()}")

    print("alchemy.elements.create_earth(): "
          f"{alchemy.elements.create_earth()}")

    print("alchemy.elements.create_air(): "
          f"{alchemy.elements.create_air()}")

    print("\nTesting package-level access (controlled by __init__.py):")
    try:
        print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    except AttributeError as erro:
        print(f"[Error]: {erro}")

    try:
        print(f"alchemy.create_water(): {alchemy.create_water()}")
    except AttributeError as erro:
        print(f"[Erro]: {erro}")

    try:
        print(f"alchemy.create_earth(): {alchemy.create_earth()}")
    except AttributeError as erro:
        print(f"[Erro] {erro}")

    try:
        print(f"alchemy.create_air(): {alchemy.create_air()}")
    except AttributeError as erro:
        print(f"[Eroo] {erro}\n")

    print("Package metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")
