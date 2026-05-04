import functools
import operator
from collections.abc import Callable
from typing import List, Dict, Any


def spell_reducer(spells: List[int], operation: str) -> int:
    """Reduz poderes; retorna 0 se vazio ou lida com erros[cite: 340, 345, 346]."""
    if not spells:
        return 0
    ops = {"add": operator.add, "multiply": operator.mul, 
           "max": max, "min": min}
    if operation not in ops:
        raise ValueError(f"Unknown operation: {operation}")
    return functools.reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable[[int, str, str], str]) -> Dict[str, Callable]:
    """Cria versões parciais com poder 50 e elemento fixo[cite: 347, 349, 350]."""
    elements = ["fire", "ice", "lightning"]
    return {
        f"{elem}_enchant": functools.partial(base_enchantment, 50, elem)
        for elem in elements
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Cálculo de Fibonacci com memoization via lru_cache[cite: 351, 352]."""
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """Sistema de despacho único baseado no tipo[cite: 359, 360, 362]."""
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
    def _(arg: list) -> str:
        return f"Multi-cast: {len(arg)} spells"

    return dispatcher
