from typing import Union, List
from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):
    def create_creature(self,
                        name_or_power: Union[str, int, None] = None) -> Card:
        if name_or_power == "Fire Dragon" or name_or_power == 5:
            return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        elif name_or_power == "Goblin Warrior" or name_or_power == 2:
            return CreatureCard("Goblin Warrior", 2, "Common", 2, 3)
        return CreatureCard("Goblin Grunt", 1, "Common", 1, 1)

    def create_spell(self,
                     name_or_power: Union[str, int, None] = None) -> Card:
        if name_or_power == "Fireball":
            return SpellCard("Fireball", 4, "Rare", "damage")
        return SpellCard("Lightning Bolt", 3, "Common", "damage")

    def create_artifact(self,
                        name_or_power: Union[str, int, None] = None) -> Card:
        return ArtifactCard("Mana Ring", 2, "Rare", 5,
                            "Permanent: +1 mana")

    def create_themed_deck(self, size: int) -> dict:
        deck: List[Card] = []
        deck.append(self.create_creature("Fire Dragon"))
        deck.append(self.create_creature("Goblin Warrior"))
        deck.append(self.create_spell("Lightning Bolt"))
        return {"deck": deck}

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }
