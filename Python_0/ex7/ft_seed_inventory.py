def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    if unit not in ("packets", "grams", "area"):
        print("Unknown unit type")
        return
    print(f"{seed_type.capitalize()} seeds: ", end="")
    if unit == "packets":
        print(f"{quantity} packets available")
    elif unit == "grams":
        print(f"{quantity} grams total")
    else:
        print(f"covers {quantity} square meters")
