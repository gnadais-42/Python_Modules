from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str = "Unknown", power: int = 0) -> tuple[
                                                        Callable, Callable]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str = "Unknown", power: int = 0) -> int:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cast_conditionally(target: str = "Unknown", power: int = 0) -> str:
        return spell(target, power) if condition() else "Spell fizzled"
    return cast_conditionally


def spell_sequence(spells: list[Callable]) -> Callable:
    def cast_all(target: str = "Unknown", power: int = 0) -> list:
        return [spell(target, power) for spell in spells]
    return cast_all


def main() -> None:
    def fireball(target: str = "Unknown", power: int = 0) -> str:
        return f"Fireball hits {target} for {power} HP"

    def heal(target: str = "Unknown", power: int = 0) -> str:
        return f"Heals restores {target} for {power} HP"

    def true_condition() -> bool:
        return True

    def false_condition() -> bool:
        return False

    combined: Callable = spell_combiner(fireball, heal)
    amplified: Callable = power_amplifier(fireball, 3)
    good_spell: Callable = conditional_caster(true_condition, fireball)
    bad_spell: Callable = conditional_caster(false_condition, fireball)
    spells: list[Callable] = [fireball,
                              heal,
                              combined,
                              amplified,
                              good_spell,
                              bad_spell]
    all_spells: Callable = spell_sequence(spells)

    print("Testing spell combiner...")
    print("Combined spell result:", ", ".join(spell for spell in combined(
        target="Dragon", power=10
    )))

    print("\nTesting power amplifier...")
    print("Original:", fireball(target="Dragon", power=10), "\nAmplified:",
          amplified(target="Dragon", power=10))

    print("\nTesting conditional caster...")
    print("True condition:", good_spell(target="Dragon", power=10))
    print("False condition:", bad_spell(target="Dragon", power=10))

    casted_spells = all_spells(target="Dragon", power=10)
    print("\nTesting spell sequence...")
    print("Result of casting all spells:\n",
          "\n".join(str(x) for x in casted_spells), sep="")


if __name__ == "__main__":
    main()
