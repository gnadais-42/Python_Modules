from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
    ) -> None:
        super().__init__(name, cost, rarity)

        self._attack = attack
        self._health = health

        self._wins = 0
        self._losses = 0
        self._rating = 1200

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name(),
            "mana_used": self.mana(),
            "effect": "Tournament card enters arena",
        }

    def attack(self, target: Card) -> dict:
        return {
            "attacker": self.name(),
            "target": target.name(),
            "damage": self._attack,
        }

    def defend(self, incoming_damage: int) -> dict:
        alive = incoming_damage < self._health
        return {
            "defender": self.name(),
            "damage_taken": incoming_damage,
            "still_alive": alive,
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self._attack,
            "health": self._health,
        }

    def calculate_rating(self) -> int:
        return self._rating

    def update_wins(self, wins: int) -> None:
        self._wins += wins
        self._rating += 16 * wins

    def update_losses(self, losses: int) -> None:
        self._losses += losses
        self._rating -= 16 * losses

    def get_rank_info(self) -> dict:
        return {
            "rating": self._rating,
            "wins": self._wins,
            "losses": self._losses,
        }

    def get_tournament_stats(self) -> dict:
        return {
            "name": self.name(),
            **self.get_rank_info(),
            **self.get_combat_stats(),
        }