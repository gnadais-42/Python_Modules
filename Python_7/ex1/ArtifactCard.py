from ex0.Card import Card

class ArtifactCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, ability: str, durability: int) -> None:
        super().__init__(name, cost, rarity)
        self._ability = ability
        self._durability = durability

    def ability(self) -> str:
        return self._ability

    def durability(self) -> int:
        return self._durability

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name(),
            "mana_used": self.mana(),
            "ability": self.ability(),
            "duration": self.durability()
        }
    
    def activate_ability(self) -> dict:
        return {
            "ability": self.ability(),
            "duration": self.durability()
        }
