def mage_counter() -> callable:
    x: int = 0

    def call() -> int:
        nonlocal x
        x += 1
        return x
    return call


def spell_accumulator(initial_power: int) -> callable:
    def accumulate(increment: int) -> int:
        nonlocal initial_power
        initial_power += increment
        return initial_power
    return accumulate


def enchantment_factory(enchantment_type: str) -> callable:
    def enchant(item: str) -> str:
        return f"{enchantment_type} {item}"
    return enchant


def memory_vault() -> dict[str, callable]:
    memory: dict[str, int] = {}

    def store(key: str, value: int) -> None:
        memory[key] = value

    def recall(key: str) -> int:
        return memory.get(key, "Memory not found")

    return {"store": store,
            "recall": recall}


def main() -> None:
    counter: callable = mage_counter()
    base_accumulation: int = 4
    accumulator: callable = spell_accumulator(base_accumulation)
    flaming_factory: callable = enchantment_factory("Flaming")
    frozen_factory: callable = enchantment_factory("Frozen")
    vault: dict[str, callable] = memory_vault()

    print("Testing mage counter...")
    for i in range(1, 4):
        print(f"Call {i}:", counter())

    print("\nTesting spell accumulator...")
    print("Base value:", base_accumulation)
    print("After accumulating 5:", accumulator(5))
    print("After another 3:", accumulator(3))

    print("\nTesting enchantment factory...")
    print(flaming_factory("Sword"))
    print(frozen_factory("Shield"))

    print("\nTesting memory vault...")
    print("Adding 3 bananas to the vault")
    vault["store"]("banana", 3)
    print("Accessing number of bananas in vault:", vault["recall"]("banana"))
    print("Accessing number of apples in vault:", vault["recall"]("apple"))


if __name__ == "__main__":
    main()
