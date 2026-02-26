from random import shuffle
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class Deck:
    def __init__(self) -> None:
        self._deck = []

    def deck(self):
        return self._deck
    
    def add_card(self, card: Card) -> None:
        self.deck().append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.deck():
            if card.name() == card_name:
                self.deck().remove(card)
                return True
        return False

    def shuffle(self) -> None:
        shuffle(self.deck())

    def draw_card(self) -> Card:
        return self.deck().pop(0)
    
    def get_deck_stats(self) -> dict:
        state = {
            "total_cards": 0,
            "creatures": 0,
            "spells": 0,
            "artifacts": 0,
        }
        t_mana = 0
        for card in self.deck():
            state["total_cards"] += 1
            t_mana += card.mana()
            if isinstance(card, CreatureCard):
                state["creatures"] += 1
            elif isinstance(card, SpellCard):
                state["spells"] += 1
            elif isinstance(card, ArtifactCard):
                state["artifacts"] += 1
        state["avg_cost"] = round(t_mana / state["total_cards"], 1) 
        return state