from ex2.EliteCard import EliteCard

def main():
    hero = EliteCard("Arcane Warrior", 6, "Rare", 5, 7, 7)
    enemy = EliteCard("Enemy", 2, "common", 3, 3, 3)
    en1 = EliteCard("Enemy1", 2, "common", 3, 3, 3)
    en2 = EliteCard("Enemy2", 2, "common", 3, 3, 3)


    print("=== DataDeck Ability System ===\n")
    print("""EliteCard capabilities:
- Card: ['play', 'get_card_info', 'is_playable']
- Combatable: ['attack', 'defend', 'get_combat_stats']
- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']\n""")
    print("Playing Arcane Warrior (Elite Card):\n")
    print("Combat phase:")
    print("Attack result:", hero.attack(enemy))
    print("Defense_result:", hero.defend(3))
    print()
    print("Magic phase:")
    print("Spell cast:", hero.cast_spell("Fireball", [en1, en2]))
    print("Mana channel:", hero.channel_mana(3))
    print("\nMultiple interface implementation successful")


if __name__ == "__main__":
    main()
