import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce a list of spell powers using the given operation"""
    if not spells:
        return 0
    ops: dict[str, Callable[..., Any]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }
    if operation not in ops:
        raise ValueError(f"Unknown operation: {operation}")
    return functools.reduce(ops[operation], spells)


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str]
) -> dict[str, Callable[..., Any]]:
    """Create three partial versions with power=50 and a fixed element"""
    elements = ["fire", "ice", "lightning"]
    return {
        f"{elem}_enchant": functools.partial(base_enchantment, 50, elem)
        for elem in elements
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Return the nth Fibonacci number using lru_cache for memoization"""
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """Return a singledispatch function handling int, str, and list spells"""
    @functools.singledispatch
    def dispatcher(arg: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register(int)
    def _(arg: int) -> str:
        return f"Damage spell: {arg} damage"

    @dispatcher.register(str)
    def _(arg: str) -> str:
        return f"Enchantment: {arg}"

    @dispatcher.register(list)
    def _(arg: list[Any]) -> str:
        return f"Multi-cast: {len(arg)} spells"

    return dispatcher


if __name__ == "__main__":
    print("Testing spell reducer...")
    powers = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(powers, 'add')}")
    print(f"Product: {spell_reducer(powers, 'multiply')}")
    print(f"Max: {spell_reducer(powers, 'max')}")

    print("\nTesting partial enchanter...")

    def base_enchant(power: int, element: str, target: str) -> str:
        return (
            f"{element.capitalize()} enchantment"
            f" on {target} with {power} power"
        )

    enchants = partial_enchanter(base_enchant)
    print(enchants["fire_enchant"]("Sword"))
    print(enchants["ice_enchant"]("Shield"))
    print(enchants["lightning_enchant"]("Bow"))

    print("\nTesting memoized fibonacci...")
    for i in [0, 1, 10, 15]:
        print(f"Fib({i}): {memoized_fibonacci(i)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")

    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch(["bolt", "heal", "shield"]))
    print(dispatch(3.14))
