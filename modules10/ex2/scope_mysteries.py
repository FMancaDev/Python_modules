from collections.abc import Callable
from typing import Dict, Any


def mage_counter() -> Callable[[], int]:
    """Closure que mantém um contador independente[cite: 275, 279]."""
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    """Acumula poder entre chamadas sucessivas[cite: 281, 282]."""
    total = initial_power

    def accumulator(power: int) -> int:
        nonlocal total
        total += power
        return total
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    """Cria funções de encantamento específicas[cite: 286, 287]."""
    return lambda item_name: f"{enchantment_type} {item_name}"


def memory_vault() -> Dict[str, Callable[..., Any]]:
    """Sistema de memória privada via closure[cite: 291, 295]."""
    vault: Dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        return vault.get(key, "Memory not found")

    return {"store": store, "recall": recall}
