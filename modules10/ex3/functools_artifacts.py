import functools
import operator


def spell_reducer(spells, operation):
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    return functools.reduce(ops[operation], spells)


def partial_enchanter(base_enchantment):
    enchants = {}
    for e in ["fire", "ice", "lightning"]:
        enchants[e + "_enchant"] = functools.partial(
            base_enchantment, power=50, element=e)
    return enchants


@functools.lru_cache()
def memoized_fibonacci(n):
    if n < 2:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher():
    @functools.singledispatch
    def dispatcher(arg):
        return "Unknown"

    @dispatcher.register(int)
    def _(arg):
        return "Damage spell: " + str(arg)

    @dispatcher.register(str)
    def _(arg):
        return "Enchantment: " + arg

    return dispatcher


# Teste
print("Reduced:", spell_reducer([10, 20, 30], "add"))
print("Fib(50):", memoized_fibonacci(50))
