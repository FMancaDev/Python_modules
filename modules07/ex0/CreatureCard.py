from ex0.Card import Card


class AttackError(Exception):
    pass


class HealthError(Exception):
    pass


class CreatureCard(Card):
    def __init__(self, name, cost, rarity, attack, health) -> None:
        super().__init__(name, cost, rarity)

        if attack < 0:
            raise AttackError("[Invalid attack] - must be higher than 0")
        if health < 0:
            raise HealthError("[Invalid health] - must be higher than 0")

        self.attack = attack
        self.health = health

    def play(self, available_mana: int) -> dict:
        if not self.is_playable(available_mana):
            return {"error": "Not enough mana"}

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({
            "type": "Creature",
            "attack": self.attack,
            "health": self.health,
        })
        return info

    def attack_target(self, target) -> dict:
        combat = target.health <= self.attack

        return {
            "attack": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat": combat
        }
