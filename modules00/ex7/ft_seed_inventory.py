#! /usr/bin/env python3

def ft_seed_inventory(seed_name: str, quantity: int, unit: str) -> None:
    clean_name = seed_name.capitalize()
    if unit == "packets":
        print(f"{clean_name} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{clean_name} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{clean_name} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type.")
