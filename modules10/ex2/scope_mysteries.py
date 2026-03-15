from typing import Callable, Dict, Any


def mage_counter() -> Callable[[], int]:
    """Counts how many times the function was called."""
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    """Accumulates power over time."""
    total = initial_power

    def accumulator(power: int):
        nonlocal total
        total += power
        return total
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    """Creates a specific type of enchantment function."""
    def enchanter(item_name: str):
        return f"{enchantment_type} {item_name}"
    return enchanter


def memory_vault() -> Dict[str, Callable]:
    """Private storage system using closures."""
    vault = {}
    return {
        "store": lambda k, v: vault.update({k: v}),
        "recall": lambda k: vault.get(k, "Memory not found")
    }


if __name__ == "__main__":
    count = mage_counter()
    print(f"Count 1: {count()}, Count 2: {count()}")
    flame = enchantment_factory("Flaming")
    print(flame("Sword"))
