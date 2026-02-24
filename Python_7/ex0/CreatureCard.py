from Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self._attack = attack
        self._health = health
        if not self.validate_stats:
            raise ValueError("Card must have positive attack and health")
        self._type = "Creature"

    def attack(self) -> int:
        return self._attack

    def health(self) -> int:
        return self._health

    def type(self) -> str:
        return self._type

    def validate_stats(self) -> bool:
        return self.attack() > 0 and self.health() > 0

    def play(self, game_state: dict) -> dict:
        return {
            "name": self.name(),
            "mana_used": self.mana(),
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target) -> dict:
        return {
            "attacker": self.name(),
            "target": target.name(),
            "damage_dealt": self.attack(),
            "combat_resolved": self.attack() >= target.health()
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info["type"] = self.type()
        info["attack"] = self.attack()
        info["health"] = self.health()
        return info
