from functools import wraps
from collections.abc import Callable
import time


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            if "power" in kwargs:
                power = kwargs["power"]
            elif len(args) >= 3:
                power = args[2]
            else:
                power = args[0]
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")

        start: float = time.perf_counter()
        result = func(*args, **kwargs)
        end: float = time.perf_counter()

        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print("Spell failed, retrying... "
                          f"attempt {i}/{max_attempts}")
            try:
                return func(*args, **kwargs)
            except Exception:
                return "Spell casting failed after " \
                    f"{max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        for char in name:
            if not char.isalpha() and not char == " ":
                return False
        return len(name) >= 3

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    @retry_spell(3)
    def input_number() -> int:
        return int(input("Please insert a number: "))

    print("Testing spell timer...")
    result1: str = fireball()
    print("Result:", result1)

    print("\nTesting retrying spell...")
    result2: int | str = input_number()
    print(result2)

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print("Gandalf the Grey:",
          MageGuild.validate_mage_name("Gandalf the Grey"))
    print("M3G4TRON:", MageGuild.validate_mage_name("M3G4TRON"))
    print("Testing Lightning with power 15: ")
    print(guild.cast_spell("Lightning", 15))
    print("Testing Ice with power 8: ")
    print(guild.cast_spell("Ice", 8))


if __name__ == "__main__":
    main()
