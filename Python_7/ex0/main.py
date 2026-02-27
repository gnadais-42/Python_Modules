from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")
    try:
        dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        warrior = CreatureCard("Goblin Warrior", 2, "Common", 3, 2)
    except Exception as e:
        print(f"Error: {e}")
        return
    print("CreatureCard Info:", dragon.get_card_info(), sep="\n", end="\n\n")
    game_state = {"available_mana": 6}
    print(f"Playing {dragon.name()} with {game_state['available_mana']} mana available:")
    playable = dragon.is_playable(game_state['available_mana'])
    print("Playable:", playable)
    if playable:
        print("Play result:", dragon.play(game_state), end="\n\n")
        print(f"{dragon.name()} attacks {warrior.name()}:")
        print("Attack result:", dragon.attack_target(warrior))
    print("\nTesting insufficient mana (3 available)")
    print("Playable:", dragon.is_playable(3))
    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
