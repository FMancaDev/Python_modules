from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        # Extrai mana do dicionario, padrao 0 se nao existir
        available_mana = game_state.get("mana", 0)

        if not self.is_playable(available_mana):
            return {"error": "Not enough mana"}

        effect_desc = self.effect_type
        if self.effect_type == "damage":
            effect_desc = f"Deal {self.cost} damage to target"

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect_desc
        }

    def resolve_effect(self, targets: list) -> dict:
        return {
            "effect_type": self.effect_type,
            "targets": targets,
            "status": "resolved"
        }
