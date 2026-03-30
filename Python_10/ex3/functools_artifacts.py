from functools import reduce, partial, singledispatch, lru_cache
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    funcs: dict[str, callable] = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min
    }
    if operation not in funcs:
        raise ValueError(f"Not a valid operation ({operation})")
    return reduce(funcs.get(operation), spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        "fire_enchant": partial(base_enchantment, element="fire", power=50),
        "ice_enchant": partial(base_enchantment, element="ice", power=50),
        "lightning_enchant":
        partial(base_enchantment, element="lightning", power=50)
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @singledispatch
    def dispatch(spell: any) -> str:
        return f"Casting spell: {spell}"

    @dispatch.register
    def _(spell: int) -> str:
        return f"Dealing {spell} damage"

    @dispatch.register
    def _(spell: str) -> str:
        return f"Enchanting with {spell}"

    @dispatch.register
    def _(spells: list) -> str:
        results = [dispatch(spell) for spell in spells]
        return "\n".join(results)

    return dispatch


def main() -> None:
    def base_enchantment(power: int, element: str, target: any) -> str:
        return f"Enchanting {target} with {power} power and {element} element"

    print("Testing spell reducer...")
    try:
        spells: list[int] = [2, 1, 7, 4, 2]
        operations: list[str] = [
            "add",
            "multiply",
            "max",
            "min"
        ]
        print("Data:", spells)
        for operation in operations:
            print(f"{operation}: {spell_reducer(spells, operation)}".title())
    except ValueError as e:
        print(e)

    enchantments: dict[str, callable] = partial_enchanter(base_enchantment)
    print("\nTesting partial enchanter...")
    for enchant in enchantments:
        print(f"Using {enchant}:", enchantments[enchant](target="Sword"))

    print("\nTesting memoized fibonacci...")
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))

    dispatcher: callable = spell_dispatcher()
    dispatching: list[any] = [
        4,
        "Double attack",
        [10, "Holy light"]
    ]
    print("\nTesting spell dispatcher...")
    for spell in dispatching:
        print(dispatcher(spell))


if __name__ == "__main__":
    main()
