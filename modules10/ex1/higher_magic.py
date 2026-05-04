from collections.abc import Callable
from typing import Any


def spell_combiner(
    spell1: Callable[..., Any],
    spell2: Callable[..., Any]
) -> Callable[..., tuple[Any, Any]]:
    """Combine two spells into one that returns both results as a tuple"""
    return lambda *args, **kwargs: (
        spell1(*args, **kwargs),
        spell2(*args, **kwargs)
    )


def power_amplifier(
    base_spell: Callable[..., Any],
    multiplier: int
) -> Callable[..., Any]:
    """Return a new spell that multiplies the power before casting"""
    def amplified_spell(target: str, power: int) -> Any:
        return base_spell(target, power * multiplier)
    return amplified_spell


def conditional_caster(
    condition: Callable[..., bool],
    spell: Callable[..., Any]
) -> Callable[..., Any]:
    """Cast the spell only if the condition returns True"""
    return lambda *args, **kwargs: (
        spell(*args, **kwargs)
        if condition(*args, **kwargs)
        else "Spell fizzled"
    )


def spell_sequence(
    spells: list[Callable[..., Any]]
) -> Callable[..., list[Any]]:
    """Return a function that casts all spells in order"""
    return lambda *args, **kwargs: [s(*args, **kwargs) for s in spells]


if __name__ == "__main__":
    def fireball(target: str, power: int = 10) -> str:
        return f"Fireball hits {target} with {power} power"

    def heal(target: str, power: int = 10) -> str:
        return f"Heals {target} for {power} health"

    def lightning(target: str, power: int = 10) -> str:
        return f"Lightning strikes {target} for {power} damage"

    def is_dragon(target: str, *args: Any, **kwargs: Any) -> bool:
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

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, lightning])
    results = sequence("Orc", 15)
    for r in results:
        print(f"  {r}")
