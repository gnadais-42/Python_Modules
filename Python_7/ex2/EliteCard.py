from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int,
                 rarity: str, att: int, hp: int, mana: int) -> None:
        super().__init__(name, cost, rarity)
        self._attack = att
        self._health = hp
        self._mana = mana
        self.spell_mana = 3

    def get_attack(self) -> int:
        return self._attack
    
    def get_health(self) -> int:
        return self._health

    def total_mana(self) -> int:
        return self._mana
    
    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name(),
            "mana_used": self.mana(),
            "effect": "Elite summoned to the battlefield"
        }

    def attack(self, target: Card) -> dict:
        return {
            "attacker": self.name(),
            "target": target.name(),
            "damage": self.get_attack(),
        }

    def defend(self, incoming_damage: int) -> dict:
        return {
            "defender": self.name(),
            "damage_taken": incoming_damage,
            "still_alive": incoming_damage < self.get_health()
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {
            "caster": self.name(),
            "spell_name": spell_name,
            "targets": [c.name() for c in targets],
            "mana_used": self.spell_mana
        }

    def channel_mana(self, amount: int) -> dict:
        return {
            "channeled": amount,
            "total_mana": self.total_mana()
        }

    def get_magic_stats(self) -> dict:
        return {
            "total_mana": self.total_mana(),
            "mana_per_spell": self.spell_mana
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.get_attack(),
            "health": self.get_health()
        }
