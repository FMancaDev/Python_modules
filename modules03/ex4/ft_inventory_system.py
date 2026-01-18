#! /usr/bin/env python3

import sys


def build_inventory() -> dict[str, int]:
    """Parses command-line arguments to build an inventory dictionary."""
    inventory: dict[str, int] = dict()

    for arg in sys.argv[1:]:
        i = 0
        for c in arg:
            if c == ':':
                break
            i += 1

        name = arg[:i]
        qty = int(arg[i + 1:])
        inventory.update({name: qty})

    return inventory


def sort_by_quantity(inventory: dict[str, int]) -> list[str]:
    """
    Sorts inventory keys by quantity in descending order using bubble sort.
    """
    keys: list[str] = []
    for k in inventory.keys():
        keys += [k]

    n = len(keys)
    for i in range(n):
        for j in range(n - 1):
            if inventory[keys[j]] < inventory[keys[j + 1]]:
                keys[j], keys[j + 1] = keys[j + 1], keys[j]

    return keys


def main() -> None:
    """Main function to analyze and display inventory statistics."""
    inventory: dict[str, int] = build_inventory()

    total: int = 0
    for q in inventory.values():
        total += q

    sorted_keys: list[str] = sort_by_quantity(inventory)

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(inventory)}")

    print("\n=== Current Inventory ===")
    for k in sorted_keys:
        qty = inventory.get(k)
        if qty is not None:
            percent = (qty / total * 100) if total > 0 else 0
            print(f"{k}: {qty} units ({percent:.1f}%)")

    print("\n=== Inventory Statistics ===")
    if len(sorted_keys) > 0:
        most = sorted_keys[0]
        least = sorted_keys[-1]
        most_qty = inventory.get(most)
        least_qty = inventory.get(least)

        print(f"Most abundant: {most} ({most_qty} units)")
        print(f"Least abundant: {least} ({least_qty} unit)")

    print("\n=== Item Categories ===")
    moderate: dict[str, int] = dict()
    scarce: dict[str, int] = dict()

    for name, qty in inventory.items():
        if qty >= 5:
            moderate.update({name: qty})
        else:
            scarce.update({name: qty})

    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

    print("\n=== Management Suggestions ===")
    restock: list[str] = []
    for name, qty in inventory.items():
        if qty < 2:
            restock += [name]
    print(f"Restock needed: {restock}")

    print("\n=== Dictionary Properties Demo ===")
    keys_list: list[str] = []
    for k in inventory.keys():
        keys_list += [k]

    values_list: list[int] = []
    for v in inventory.values():
        values_list += [v]

    print(f"Dictionary keys: {keys_list}")
    print(f"Dictionary values: {values_list}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


if len(sys.argv) > 1:
    main()
