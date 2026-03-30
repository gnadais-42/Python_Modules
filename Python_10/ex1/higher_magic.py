def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined() -> tuple:
        return (spell1(), spell2())
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplified() -> int:
        return base_spell() * multiplier
    return amplified


def conditional_caster(condition: callable, spell: callable) -> callable:
    def cast_conditionally() -> str:
        return spell() if condition() else "Spell fizzled"
    return cast_conditionally


def spell_sequence(spells: list[callable]) -> callable:
    def cast_all() -> list:
        return [spell() for spell in spells]
    return cast_all


def main() -> None:
    def fire(target: str = "Dragon") -> str:
        return f"Fire hits {target}"

    def heal(target: str = "Dragon") -> str:
        return f"Heals {target}"

    def fireball(damage: int = 10) -> int:
        return damage

    def true_condition() -> bool:
        return True

    def false_condition() -> bool:
        return False

    spells = [fire, heal, fireball, true_condition, false_condition]

    combined: callable = spell_combiner(fire, heal)
    amplified: callable = power_amplifier(fireball, 3)
    good_spell: callable = conditional_caster(true_condition, fire)
    bad_spell: callable = conditional_caster(false_condition, fire)
    all_spells: callable = spell_sequence(spells)

    print("Testing spell combiner...")
    print("Combined spell result:", ", ".join(spell for spell in combined()))

    print("\nTesting power amplifier...")
    print(f"Original: {fireball()}, Amplified: {amplified()}")

    print("\nTesting conditional caster...")
    print("True condition:", good_spell())
    print("False condition:", bad_spell())

    print("\nTesting spell sequence...")
    print("Result of casting all spells:", all_spells())


if __name__ == "__main__":
    main()
