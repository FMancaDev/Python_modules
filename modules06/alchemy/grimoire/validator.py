def validate_ingredients(ingredients: str) -> str:
    engredients = ["water", "earth", "air", "fire"]
    engredients_lst = ingredients.split()

    if all(i in engredients for i in engredients_lst):
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
