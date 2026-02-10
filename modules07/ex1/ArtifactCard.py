from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        available_mana = game_state.get("mana", 0)

        if not self.is_playable(available_mana):
            return {"error": "Not enough mana"}

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect
        }

    def activate_ability(self) -> dict:
        return {
            "artifact": self.name,
            "effect_triggered": self.effect,
            "durability_remaining": self.durability
        }
