from ex3.GameStrategy import GameStrategy
from ex3.CardFactory import CardFactory


class GameEngine:
    def __init__(self) -> None:
        self._factory: CardFactory | None = None
        self._strategy: GameStrategy | None = None
        self._hand: list = []
        self._battlefield: list = self._generate_dummy_targets()
        self._turns_simulated: int = 0
        self._total_damage: int = 0

    def _generate_dummy_targets(self) -> list:
        class DummyTarget:
            def __init__(self, name: str, health: int):
                self._name = name
                self._health = health

            def health(self):
                return self._health

            def __repr__(self):
                return self._name

        return [
            DummyTarget("Enemy Goblin", 3),
            DummyTarget("Enemy Orc", 5),
            DummyTarget("Enemy Player", 20),
        ]

    def configure_engine(
        self,
        factory: CardFactory,
        strategy: GameStrategy
    ) -> None:
        self._factory = factory
        self._strategy = strategy

        deck_dict = factory.create_themed_deck(3)

        self._hand = (
            deck_dict["Creatures"]
            + deck_dict["Spells"]
            + deck_dict["Artifacts"]
        )

    def simulate_turn(self) -> dict:
        if not self._strategy:
            raise ValueError("Strategy not configured.")

        result = self._strategy.execute_turn(
            self._hand,
            self._battlefield
        )

        self._turns_simulated += 1

        damage = 0
        for card in result["cards_played"]:
            if hasattr(card, "attack"):
                try:
                    damage += card.attack()
                except Exception:
                    pass

        self._total_damage += damage

        return result

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self._turns_simulated,
            "strategy_used": (
                self._strategy.get_strategy_name()
                if self._strategy else None
            ),
            "total_damage": self._total_damage,
            "cards_created": len(self._hand)
        }