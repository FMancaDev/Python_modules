from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    """Return a closure that counts how many times it has been called"""
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    """Return a closure that accumulates power starting from initial_power"""
    total = initial_power

    def accumulator(power: int) -> int:
        nonlocal total
        total += power
        return total

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    """Return a function that applies the given enchantment to an item"""
    return lambda item_name: (
        f"{enchantment_type} {item_name}"
    )


def memory_vault() -> dict[str, Callable[..., Any]]:
    """Return a dict with 'store' and 'recall' closures"""
    vault: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        return vault.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    acc = spell_accumulator(100)
    print(f"Base 100, add 20: {acc(20)}")
    print(f"Base 100, add 30: {acc(30)}")

    print("\nTesting enchantment factory...")
    flame = enchantment_factory("Flaming")
    frost = enchantment_factory("Frozen")
    print(flame("Sword"))
    print(frost("Shield"))

    print("\nTesting memory vault...")
    mv = memory_vault()
    mv["store"]("secret", 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {mv['recall']('secret')}")
    print(f"Recall 'unknown': {mv['recall']('unknown')}")
