def mage_counter() -> callable:
    """Return a closure that counts how many times it has been called"""
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> callable:
    """Return a closure that accumulates power starting from initial_power"""
    total = initial_power

    def add_power(amount: int) -> int:
        nonlocal total
        total += amount
        return total

    return add_power


def enchantment_factory(enchantment_type: str) -> callable:
    """Return a function that applies the enchantment to an item name"""
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict[str, callable]:
    """Return a dict with 'store' and 'recal' functions sharing privat state"""
    vault = {}

    def store(key: str, value) -> None:
        vault[key] = value

    def recall(key: str):
        return vault.get(key, "Memory not found")

    return {'store': store, 'recall': recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter = mage_counter()
    for i in range(1, 4):
        print(f"Call {i}: {counter()}")

    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(100)
    print(f"After +50: {accumulator(50)}")
    print(f"After +30: {accumulator(30)}")

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault['store']('spell', 'Fireball')
    print(vault['recall']('spell'))
    print(vault['recall']('unknown'))
