from collections.abc import Callable
from typing import List, Tuple, Any


def spell_combiner(spell1: Callable[..., Any],
                   spell2: Callable[..., Any]) -> Callable[..., Tuple[Any, Any]]:
    """combina dois feiticos num Tuple"""
    return lambda *args, **kwargs: (spell1(*args, **kwargs),
                                    spell2(*args, **kwargs))


def power_amplifier(base_spell: Callable[..., Any],
                    multiplier: int) -> Callable[..., Any]:
    """multiplica o poder do feitiço"""
    def amplified_spell(target: str, power: int) -> Any:
        return base_spell(target, power * multiplier)
    return amplified_spell


def conditional_caster(condition: Callable[..., bool],
                       spell: Callable[..., Any]) -> Callable[..., Any]:
    """executa o feitico apenas se fo True"""
    return lambda *args, **kwargs: spell(*args, **kwargs) \
        if condition(*args, **kwargs) else "Spell fizzled"


def spell_sequence(spells: List[Callable[..., Any]]) -> Callable[..., List[Any]]:
    """executa os feitiços em ordem"""
    return lambda *args, **kwargs: [s(*args, **kwargs) for s in spells]


if __name__ == "__main__":
    def fireball(target: str, power: int = 10) -> str:
        return f"Fireball hits {target} with {power} power"

    def heal(target: str, power: int = 10) -> str:
        return f"Heals {target} for {power} health"

    def is_dragon(target: str, *args, **kwargs) -> bool:
        return target.lower() == "dragon"

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    res_f, res_h = combined("Dragon", 20)
    print(f"Combined spell result: {res_f}, {res_h}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: {fireball('Target', 10)}")
    print(f"Amplified: {mega_fireball('Target', 10)}")

    print("\nTesting conditional caster...")
    dragon_spell = conditional_caster(is_dragon, fireball)
    print(f"Target Dragon: {dragon_spell('Dragon', 50)}")
    print(f"Target Goblin: {dragon_spell('Goblin', 50)}")
