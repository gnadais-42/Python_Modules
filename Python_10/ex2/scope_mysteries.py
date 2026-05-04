from collections.abc import Callable


def mage_counter() -> Callable:
    x: int = 0

    def call() -> int:
        nonlocal x
        x += 1
        return x
    return call


def spell_accumulator(initial_power: int) -> Callable:
    def accumulate(increment: int) -> int:
        nonlocal initial_power
        initial_power += increment
        return initial_power
    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item: str) -> str:
        return f"{enchantment_type} {item}"
    return enchant


def memory_vault() -> dict[str, Callable]:
    memory: dict[str, int] = {}

    def store(key: str, value: int) -> None:
        memory[key] = value

    def recall(key: str) -> int:
        return memory.get(key, "Memory not found")

    return {"store": store,
            "recall": recall}


def main() -> None:
    counter1: Callable = mage_counter()
    counter2: Callable = mage_counter()
    base_accumulation: int = 4
    accumulator: Callable = spell_accumulator(base_accumulation)
    flaming_factory: Callable = enchantment_factory("Flaming")
    frozen_factory: Callable = enchantment_factory("Frozen")
    vault: dict[str, Callable] = memory_vault()

    print("Testing mage counters...")
    for i in range(1, 4):
        print(f"\033[32mCall {i} on counter1:", counter1())
    for i in range(1, 6):
        print(f"\033[33mCall {i} on counter2:", counter2())

    print("\033[37m\nTesting spell accumulator...")
    print("Base value:", base_accumulation)
    print("After accumulating 5:", accumulator(5))
    print("After another 3:", accumulator(3))

    print("\nTesting enchantment factory...")
    print("\033[31m" + flaming_factory("Sword"))
    print("\033[34m" + frozen_factory("Shield"))

    print("\033[37m\nTesting memory vault...")
    print("Store 'secret' = 42")
    vault["store"]('secret', 42)
    print("Recall 'secret':", vault["recall"]("secret"))
    print("Recall 'unknown':", vault["recall"]("unknown"))


if __name__ == "__main__":
    main()
