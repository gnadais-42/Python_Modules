from functools import wraps
from typing import Callable, TypeVar, ParamSpec
import time

P = ParamSpec("P")
T = TypeVar("T")


def power_validator(min_power: int) -> Callable[P, T]:
    def decorator(func: Callable[P, T]) -> Callable[P, T]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            power = args[0]
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def spell_timer(func: Callable[P, T]) -> Callable[P, T]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        print(f"Casting {func.__name__}...")

        start: float = time.perf_counter()
        result: T = func(*args, **kwargs)
        end: float = time.perf_counter()

        print(f"Spell completed in {end - start} seconds")
        return result
    return wrapper


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: Callable[P, T]) -> Callable[P, T]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
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
        return len(name >= 3)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    @spell_timer
    def test_function() -> None:
        print("Sleeping for a second....")
        time.sleep(1)

    @power_validator(4)
    def test_spell(power, something) -> str:
        return f"Test spell function with power {power}"

    @retry_spell(3)
    def test_retry() -> int:
        return int(input("Please insert a number: "))

    print(test_retry())


if __name__ == "__main__":
    main()
