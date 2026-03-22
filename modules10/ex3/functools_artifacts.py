import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce spell powers using the specified operation"""
    ops = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': lambda a, b: a if a > b else b,
        'min': lambda a, b: a if a < b else b,
    }
    if not spells or operation not in ops:
        return 0
    return functools.reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    """Create partial aplications for fire, ice, and lightning enchantments"""
    return {
        'fire_enchant': functools.partial(
            base_enchantment, power=50, element='fire'
        ),
        'ice_enchant': functools.partial(
            base_enchantment, power=50, element='ice'
        ),
        'lightning_enchant': functools.partial(
            base_enchantment, power=50, element='lightning'
        ),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Return the nth Fibonacci number using memoization"""
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    """Create a singledispatch spell system for different input types"""
    @functools.singledispatch
    def cast(target):
        return f"Unknown spell type for {target}"

    @cast.register(int)
    def _(target: int):
        return f"Damage spell dealing {target} damage"

    @cast.register(str)
    def _(target: str):
        return f"Enchantment applied to {target}"

    @cast.register(list)
    def _(target: list):
        return [f"Multi-cast on {t}" for t in target]

    return cast


if __name__ == "__main__":
    spells = [10, 20, 30, 40]
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting partial enchanter...")

    def base_enchant(target: str, power: int, element: str) -> str:
        return f"{element.capitalize()} enchant on {target} with {power} power"

    enchanters = partial_enchanter(base_enchant)
    print(enchanters['fire_enchant'](target='Sword'))
    print(enchanters['ice_enchant'](target='Shield'))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(50))
    print(dispatcher("Dragon"))
    print(dispatcher(["Goblin", "Orc"]))
