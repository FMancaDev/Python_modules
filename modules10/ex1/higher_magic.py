def spell_combiner(spell1: callable, spell2: callable) -> callable:
    """Return a new function that calls both spells and returns a tuple"""
    def combined(*args, **kwargs):
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    """Return a new function that multiplies the base spell result"""
    def amplified(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier
    return amplified


def conditional_caster(condition: callable, spell: callable) -> callable:
    """Return a function that only casts spell if condition is True"""
    def cast(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return cast


def spell_sequence(spells: list[callable]) -> callable:
    """Return a function that casts all spells"""
    """and returns a list of results"""
    def sequence(*args, **kwargs):
        return [spell(*args, **kwargs) for spell in spells]
    return sequence


if __name__ == "__main__":
    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon")
    print(f"Combined spell result: {result[0]}, {result[1]}")

    def damage(target: str) -> int:
        return 10

    print("\nTesting power amplifier...")
    mega = power_amplifier(damage, 3)
    print(f"Original: {damage('enemy')}, Amplified: {mega('enemy')}")

    print("\nTesting conditional caster...")
    def is_enemy(t): return t == "Dragon"
    fire_if_enemy = conditional_caster(is_enemy, fireball)
    print(fire_if_enemy("Dragon"))
    print(fire_if_enemy("Ally"))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal])
    print(sequence("Goblin"))
