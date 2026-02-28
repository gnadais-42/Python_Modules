from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


def main() -> None:
    print("=== DataDeck Game Engine ===\n")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy(available_mana=6)

    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print("Factory:", factory.__class__.__name__)
    print("Strategy:", strategy.get_strategy_name())
    print("Available types:", factory.get_supported_types())

    print("\nSimulating aggressive turn...\n")

    result = engine.simulate_turn()

    print("Turn execution:")
    print({
        "cards_played": [c for c in result["cards_played"]],
        "mana_used": result["mana_used"],
        "targets_attacked": result["targets_attacked"],
    })

    print("\nGame Report:")
    print(engine.get_engine_status())


if __name__ == "__main__":
    main()