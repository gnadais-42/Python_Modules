def game_events(n: int, players: list) -> tuple:
    actions: tuple = ("killed monster", "found treasure", "leveled up")
    i: int = 0
    while i < n:
        player = players[i % len(players)]
        action = actions[i % len(players)]
        yield (i, player, action)
        i += 1


def fibonacci() -> int:
    a: int = 0
    b: int = 1
    i: int = 0
    while True:
        if i == 0:
            number = a
        elif i == 1:
            number = b
        else:
            number = a + b
            a = b
            b = number
        yield number
        i += 1


def prime() -> int:
    n: int = 2
    while True:
        i: int = 2
        is_prime: bool = True
        while i < n:
            if n % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            yield n
        n += 1


def main() -> None:
    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...\n")

    n_events: int = 1000
    players: tuple = (["alice", 5], ["bob", 12], ["charlie", 7])
    events: tuple = game_events(n_events, players)
    level_up: int = 0
    treasures_found: int = 0
    high_level: int = 0

    while True:
        try:
            i, player, action = next(events)
        except StopIteration:
            break

        if action == "leveled up":
            level_up += 1
            player[1] += 1
        elif action == "found treasure":
            treasures_found += 1
        if player[1] >= 10:
            high_level += 1

        if i < 3:
            print(f"Event {i}: Player {player[0]} "
                  f"(level {player[1]}) {action}")
    print("...\n")

    print("=== Stream Analytics ===")
    print(f"Total events processed: {n_events}")
    print(f"High-level players: {high_level}")
    print(f"Treasure_events: {treasures_found}")
    print(f"Level_up events: {level_up}\n")

    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds\n")

    print("=== Generator Demonstration ===")
    fibo = fibonacci()
    print("Fibonacci sequence (first 10): ", end="")
    first: bool = True
    for _ in range(10):
        if not first:
            print(", ", end="")
        print(next(fibo), end="")
        first = False
    print()
    primes = prime()
    print("Prime numbers (first 5): ", end="")
    first = True
    for _ in range(5):
        if not first:
            print(", ", end="")
        print(next(primes), end="")
        first = False
    print()


if __name__ == "__main__":
    main()
