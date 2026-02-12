#! /usr/bin/env python3


import alchemy
from alchemy.transmutation.basic import lead_to_gold  # absolute import
from alchemy.transmutation.basic import stone_to_gem  # absolute import
from alchemy.transmutation.advanced import philosophers_stone, elixir_of_life

if __name__ == "__main__":
    print("\n=== Patthway Debate Mastery ===")

    print("\nTesting Absolute Imports (from basic.py)")
    print(f"lead_to_gold(): {lead_to_gold()}")
    print(f"stone_to_gem(): {stone_to_gem()}\n")

    print("Testing Relative Import (from advanced.py)")
    print(f"philosophers_stone(): {philosophers_stone()}")
    print(f"elixir_of_life(): {elixir_of_life()}")

    print("\nTesting Package Access:")
    print(
        "alchemy.transmutation.lead_to_gold(): "
        f"{alchemy.transmutation.lead_to_gold()}"
    )
    print(
        "alchemy.transmutation.philosophers_stone(): "
        f"{alchemy.transmutation.philosophers_stone()}\n"
    )

    print("Both pathways work! Absolute: clear, Relative: concise")
