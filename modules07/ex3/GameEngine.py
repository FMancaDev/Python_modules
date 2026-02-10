from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self):
        self.factory = None
        self.strategy = None
        self.turn_count = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        if not self.factory or not self.strategy:
            return {"error": "Engine not configured"}

        self.turn_count += 1

        deck_data = self.factory.create_themed_deck(3)
        hand = deck_data.get("deck", [])
        self.cards_created += len(hand)

        battlefield = []
        turn_result = self.strategy.execute_turn(hand, battlefield)

        actions = turn_result.get("actions", {})
        self.total_damage += actions.get("damage_dealt", 0)

        return {
            "hand_display": [f"{c.name} ({c.cost})" for c in hand],
            "execution_result": turn_result
        }

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turn_count,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
