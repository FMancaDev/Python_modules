from typing import Dict, List
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.participants: Dict[str, TournamentCard] = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        if isinstance(card, TournamentCard):
            self.participants[card.card_id] = card
            return f"Registered {card.name}"
        return "Registration failed"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        c1 = self.participants.get(card1_id)
        c2 = self.participants.get(card2_id)

        if not c1 or not c2:
            return {"error": "Card not found"}

        self.matches_played += 1

        winner = None
        loser = None

        if c1.attack_val >= c2.attack_val:
            winner = c1
            loser = c2
        else:
            winner = c2
            loser = c1

        # Atualizar Stats
        winner.update_wins(1)
        loser.update_losses(1)

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating()
        }

    def get_leaderboard(self) -> List[str]:
        sorted_cards = sorted(
            self.participants.values(),
            key=lambda c: c.rating,
            reverse=True
        )
        board = []
        for i, card in enumerate(sorted_cards, 1):
            info = f"{i}. {card.name} - Rating: {card.rating} " \
                   f"({card.wins}-{card.losses})"
            board.append(info)
        return board

    def generate_tournament_report(self) -> dict:
        total_rating = sum(c.rating for c in self.participants.values())
        count = len(self.participants)
        avg = int(total_rating / count) if count > 0 else 0

        return {
            "total_cards": count,
            "matches_played": self.matches_played,
            "avg_rating": avg,
            "platform_status": "active"
        }
