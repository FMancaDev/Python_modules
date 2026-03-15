def spell_combiner(spell1, spell2):
    def combined(*args, **kwargs):
        return spell1(*args, **kwargs), spell2(*args, **kwargs)
    return combined


def power_amplifier(spell, multiplier):
    def amplified(*args, **kwargs):
        return spell(*args, **kwargs) * multiplier
    return amplified


def conditional_caster(condition, spell):
    def caster(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return caster


def spell_sequence(spells):
    def sequence(*args, **kwargs):
        results = []
        for s in spells:
            results.append(s(*args, **kwargs))
        return results
    return sequence


# Teste
def fball(x):
    return f"Fireball {x}"


def heal(x):
    return f"Heal {x}"


def mult(x):
    return x * 2


combo = spell_combiner(fball, heal)
amp = power_amplifier(mult, 3)

print("Combo:", combo("Dragon"))
print("Amp:", amp(10))
