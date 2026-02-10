import random
from typing import List, Optional
from ex0.Card import Card


class Deck:
    def __init__(self):
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        if isinstance(card, Card):
            self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for i, card in enumerate(self.cards):
            if card.name == card_name:
                self.cards.pop(i)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Optional[Card]:
        if not self.cards:
            return None
        # Remove do topo (indice 0) para ordem de chegada
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        total = len(self.cards)
        creatures = 0
        spells = 0
        artifacts = 0
        total_cost = 0

        for card in self.cards:
            total_cost += card.cost
            c_type = card.__class__.__name__
            if c_type == "CreatureCard":
                creatures += 1
            elif c_type == "SpellCard":
                spells += 1
            elif c_type == "ArtifactCard":
                artifacts += 1

        avg = (total_cost / total) if total > 0 else 0.0

        return {
            "total_cards": total,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": float(round(avg, 1))
        }
