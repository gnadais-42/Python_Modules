from ex0.Card import Card

class SpellCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self._effect = effect

    def effect(self) -> str:
        return self._effect

    def play(self, game_state: dict) -> dict:
        try:
            if game_state["available_mana"] < self.mana():
                print("Not enough mana to play", self.name())
                return {}
        except KeyError:
            print("Invalid game state")
            return {}
        return {
            "card_played": self.name(),
            "mana_used": self.mana(),
            "effect": self.effect()
        }

    def resolve_effect(self, targets: list) -> dict:
        return {
            "effect": self.effect(),
            "targets": [t.name() for t in targets]
        }
