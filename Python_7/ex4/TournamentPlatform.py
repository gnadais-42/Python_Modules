from ex4.TournamentCard import TournamentCard

class TournamentPlatform:

    def __init__(self) -> None:
        self._cards: dict[str, TournamentCard] = {}
        self._matches_played: int = 0

    def register_card(self, card: TournamentCard) -> str:
        card_id = f"{card.name().lower().replace(' ', '_')}_{len(self._cards)+1}"
        self._cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self._cards.get(card1_id)
        card2 = self._cards.get(card2_id)

        if not card1 or not card2:
            return {"error": "Invalid card IDs"}

        stats1 = card1.get_combat_stats()
        stats2 = card2.get_combat_stats()

        if stats1["attack"] >= stats2["attack"]:
            winner = card1
            loser = card2
        else:
            winner = card2
            loser = card1

        winner.update_wins(1)
        loser.update_losses(1)

        self._matches_played += 1

        return {
            "winner": winner.name(),
            "loser": loser.name(),
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating(),
        }

    def get_leaderboard(self) -> list:
        return sorted(
            self._cards.values(),
            key=lambda card: card.calculate_rating(),
            reverse=True,
        )

    def generate_tournament_report(self) -> dict:
        if not self._cards:
            return {}

        avg_rating = sum(
            card.calculate_rating() for card in self._cards.values()
        ) // len(self._cards)

        return {
            "total_cards": len(self._cards),
            "matches_played": self._matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active",
        }