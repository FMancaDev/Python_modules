#! /usr/bin/env python3

if __name__ == "__main__":
    from alchemy.grimoire.validator import validate_ingredients as val
    from alchemy.grimoire.spellbook import record_spell as rec

    print("\n=== Circular Breaking ===\n")

    print("testing ingredient validation:")
    print(f"validate_ingredients(\"fire air\"): {val('fire air')}")
    print(f"validate_ingredients(\"dragon scales\"): {val('dragon scales')}\n")

    print("Testing spell recording with validation")
    print(
        "record_spell(\"Fireball\", \"fire air\"): "
        f"{rec('Fireball', 'fire air')}"
    )
    print(
        "record_spell(\"Dark Magic\", \"shadow\"): "
        f"{rec('Dark Magic', 'shadow')}\n"
    )

    print("Testing late import technique:")
    print(f"record_spell(\"Lightning\", \"air\"): {rec('Lightning', 'air')}\n")

    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")
