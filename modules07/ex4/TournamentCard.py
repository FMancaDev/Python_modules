from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, card_id: str, name: str, cost: int, rarity: str,
                 attack_val: int, health_val: int, initial_rating: int = 1200):
        super().__init__(name, cost, rarity)
        self.card_id = card_id
        self.attack_val = attack_val
        self.health = health_val
        self.max_health = health_val
        self.rating = initial_rating
        self.wins = 0
        self.losses = 0

    def play(self, game_state: dict) -> dict:
        return {
            "card": self.name,
            "action": "Enters tournament arena",
            "mana_cost": self.cost
        }

    # Combatable
    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "damage": self.attack_val,
            "target": str(target)
        }

    def defend(self, incoming_damage: int) -> dict:
        self.health -= incoming_damage
        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "remaining_health": self.health
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_val,
            "health": self.health
        }

    # Rankable
    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, count: int = 1) -> None:
        self.wins += count
        self.rating += (16 * count)

    def update_losses(self, count: int = 1) -> None:
        self.losses += count
        self.rating -= (16 * count)

    def get_rank_info(self) -> dict:
        return {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }

    def get_tournament_stats(self) -> dict:
        return {
            "id": self.card_id,
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}"
        }
