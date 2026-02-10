from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main():
    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")

    deck = Deck()

    # Criar cartas
    spell = SpellCard("Lightning Bolt", 3, "Common", "damage")
    artifact = ArtifactCard("Mana Crystal", 2, "Rare", 3,
                            "Permanent: +1 mana per turn")
    creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    deck.add_card(spell)
    deck.add_card(artifact)
    deck.add_card(creature)

    print(f"Deck stats: {deck.get_deck_stats()}")

    print("\nDrawing and playing cards:")

    game_state = {"mana": 10, "targets": ["Enemy"]}

    for _ in range(3):
        card = deck.draw_card()
        if card:
            c_type = "Unknown"
            if isinstance(card, CreatureCard):
                c_type = "Creature"
            elif isinstance(card, SpellCard):
                c_type = "Spell"
            elif isinstance(card, ArtifactCard):
                c_type = "Artifact"

            print(f"\nDrew: {card.name} ({c_type})")

            try:
                if isinstance(card, CreatureCard):
                    res = card.play(game_state["mana"])
                else:
                    res = card.play(game_state)
                print(f"Play result: {res}")
            except Exception as e:
                print(f"Error: {e}")

    print(
        "\nPolymorphism in action: Same interface, different card behaviors!"
    )


if __name__ == "__main__":
    main()
