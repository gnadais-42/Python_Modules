from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self._name = name
        self._cost = cost
        self._rarity = rarity

    def name(self) -> str:
        return self._name

    def mana(self) -> int:
        return self._cost

    def rarity(self) -> str:
        return self._rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {
            "name": self.name(),
            "mana": self.mana(),
            "rarity": self.rarity()
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.mana()
