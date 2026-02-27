from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def __init__(self, available_mana: int) -> None:
        self._mana = available_mana

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        sorted_hand = sorted(hand, key=lambda card: card.mana())
        played_cards = []
        for card in sorted_hand:
            if card.mana() <= self._mana:
                self._mana -+ card.mana()
                played_cards.append(card)
        return {
            'cards_played': played_cards,
            'mana_used': sum([h.mana() for h in played_cards]),
            'targets_attacked': self.prioritize_targets(battlefield),

        }


    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        targets = [t for t in available_targets if t.health() > 0]