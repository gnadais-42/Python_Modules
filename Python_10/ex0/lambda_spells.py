def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x.get("power", 0), reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x.get("power", 0) >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_mage = max(mages, key=lambda x: x.get("power", 0), default=None)
    min_mage = min(mages, key=lambda x: x.get("power", 0), default=None)
    total = sum(map(lambda x: x.get("power", 0), mages))
    return {
        "max_power": max_mage.get("power", 0) if max_mage else 0,
        "min_power": min_mage.get("power", 0) if min_mage else 0,
        "avg_power": round(total / len(mages) if mages else 0.0, 2)
    }


def main() -> None:
    mages: list[dict] = [
        {"name": "Eldrin Moonshade", "power": 10, "element": "fire"},
        {"name": "Thalvior the Arcane", "power": 20, "element": "water"},
        {"name": "Morwen Starwhisper", "power": 30, "element": "earth"}
    ]
    artifacts: list[dict] = [
        {"name": "Flamebringer Sword", "power": 85, "type": "weapon"},
        {"name": "Aegis Shield", "power": 70, "type": "armor"},
        {"name": "Ring of Shadows", "power": 60, "type": "accessory"},
        {"name": "Staff of Storms", "power": 90, "type": "weapon"},
        {"name": "Helm of Insight", "power": 65, "type": "armor"}
    ]
    spells: list[str] = [
        "Arcane Burst",
        "Frost Nova",
        "Shadow Veil",
        "Thunder Lash",
        "Ember Strike",
        "Celestial Bind"
    ]
    sorted_arti: list[dict] = artifact_sorter(artifacts)
    filtered_mages: list[dict] = power_filter(mages, 15)
    transformed_spells: list[str] = spell_transformer(spells)
    stats: dict = mage_stats(mages)
    print("Testing artifact sorter...")
    print((f"{sorted_arti[0]['name']} ({sorted_arti[0]['power']} power) "
           f"comes before {sorted_arti[1]['name']}"
           f"({sorted_arti[1]['power']} power)")
          if len(sorted_arti) >= 2 else "Provide a larger artifact list")

    print("\nTesting power filter...")
    print("Mages with power greater than or equal to 15:")
    print(", ".join(mage.get("name", "Unknown") for mage in filtered_mages))

    print("\nTesting spell transformer...")
    print(" ".join(transformed_spells))

    print("\nTesting mage stats...")
    print("Max power:", stats.get("max_power", 0),
          "\nMin power:", stats.get("min_power", 0),
          "\nAvg power:", stats.get("avg_power", 0))


if __name__ == "__main__":
    main()
