from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from random import choice
from enum import Enum


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self._creatures = ['dragon', 'goblin']
        self._spells = ['fireball']
        self._artifacts = ['mana_ring']


    def create_creature(self,
                        name_or_power:
                        str | int | None = None) -> Card:
        stats = choice(list(Creatures)).value
        return CreatureCard(
            name_or_power,
            stats[0],
            stats[1],
            stats[2],
            stats[3]
        )

    def create_spell(self,
                     name_or_power:
                     str | int | None = None) -> Card:
        stats = choice(list(Spells)).value
        return SpellCard(
            name_or_power,
            stats[0],
            stats[1],
            stats[2]
        )

    def create_artifact(self,
                        name_or_power:
                        str | int | None = None) -> Card:
        stats = choice(list(Artifacts)).value
        return ArtifactCard(
            name_or_power,
            stats[0],
            stats[1],
            stats[2],
            stats[3]
        )

    def create_themed_deck(self, size: int) -> dict:
        final = {
            "Creatures": [],
            "Spells": [],
            "Artifacts": []
        }
        if not isinstance(size, int):
            return final
        actions = [
            ("Creatures", lambda: self.create_creature(choice(self._creatures))),
            ("Spells" ,lambda: self.create_spell(choice(self._spells))),
            ("Artifacts", lambda: self.create_artifact(choice(self._artifacts))),
        ]
        for _ in range(size):
            category, func = choice(actions)
            card = func()
            final[category].append(card)
        return final


    def get_supported_types(self) -> dict:
        return {
            'creatures': self._creatures,
            'spells': self._spells,
            'artifacts': self._artifacts
        }


class Creatures(Enum):
    COMMON: int = (1, "Common", 2, 2)
    UNCOMMON = (2, "Uncommon", 3, 4)
    RARE = (3, "Rare", 4, 5)
    LEGENDARY = (4, "Legendary", 6, 6)


class Spells(Enum):
    COMMON = (1, "Common", "Deal 2 damage")
    UNCOMMON = (2, "Uncommon", "Deal 3 damage")
    RARE = (3, "Rare", "Deal 5 damage")
    LEGENDARY = (4, "Legendary", "Deal 8 damage")


class Artifacts(Enum):
    COMMON = (1, "Common", "1 Mana per turn", 3)
    UNCOMMON = (2, "Uncommon", "2 Mana per turn", 3)
    RARE = (3, "Rare", "3 Mana per turn", 4)
    LEGENDARY = (4, "Legendary", "5 Mana per turn", 5)
