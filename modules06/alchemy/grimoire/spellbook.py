def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    valid = validate_ingredients(ingredients)

    if valid.split("-")[1].strip() == "VALID":
        return f"Spell recorded: {spell_name} ({valid})"
    else:
        return f"Spell rejected: {spell_name} ({valid})"
