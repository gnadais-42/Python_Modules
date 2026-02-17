def validate_ingredients(ingredients: str) -> str:
    ingredients_list = ingredients.split()
    for ingredient in ingredients_list:
        if ingredient.lower() not in ("fire", "water", "earth", "air"):
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
