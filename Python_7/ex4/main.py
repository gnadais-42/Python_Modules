from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===\n")

    platform = TournamentPlatform()

    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7, 5)
    wizard = TournamentCard("Ice Wizard", 4, "Rare", 5, 6)

    id1 = platform.register_card(dragon)
    id2 = platform.register_card(wizard)

    print("Registered Cards:")
    print(id1, dragon.get_tournament_stats())
    print(id2, wizard.get_tournament_stats())

    print("\nCreating tournament match...\n")

    result = platform.create_match(id1, id2)
    print("Match result:", result)

    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for position, card in enumerate(leaderboard, start=1):
        print(
            f"{position}. {card.name()} - Rating: "
            f"{card.calculate_rating()} "
            f"({card.get_rank_info()['wins']}-"
            f"{card.get_rank_info()['losses']})"
        )

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")


if __name__ == "__main__":
    main()