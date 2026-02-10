from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return sorted(available_targets, key=lambda x: "Player" in x,
                      reverse=True)

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        current_mana = 5
        cards_played = []
        damage_dealt = 0
        mana_used = 0
        targets = ["Enemy Player"]

        sorted_hand = sorted(hand, key=lambda card: card.cost)

        for card in sorted_hand:
            if card.cost <= current_mana:
                current_mana -= card.cost
                mana_used += card.cost
                cards_played.append(card.name)

                if hasattr(card, 'attack'):
                    damage_dealt += card.attack
                elif hasattr(card, 'effect_type') \
                        and card.effect_type == "damage":
                    damage_dealt += card.cost

        return {
            "strategy": self.get_strategy_name(),
            "actions": {
                "cards_played": cards_played,
                "mana_used": mana_used,
                "targets_attacked": targets,
                "damage_dealt": damage_dealt
            }
        }
