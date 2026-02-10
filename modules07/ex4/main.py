from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    print("\n=== DataDeck Tournament Platform ===\n")

    platform = TournamentPlatform()

    print("Registering Tournament Cards...\n")
    dragon = TournamentCard("dragon_001", "Fire Dragon", 5, "Legendary",
                            7, 5, 1200)
    wizard = TournamentCard("wizard_001", "Ice Wizard", 4, "Epic",
                            5, 4, 1150)

    platform.register_card(dragon)
    platform.register_card(wizard)

    print(f"{dragon.name} (ID: {dragon.card_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {dragon.rating}")
    print(f"- Record: {dragon.wins}-{dragon.losses}")

    print(f"{wizard.name} (ID: {wizard.card_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {wizard.rating}")
    print(f"- Record: {wizard.wins}-{wizard.losses}")

    print("\nCreating tournament match...")
    result = platform.create_match("dragon_001", "wizard_001")
    print(f"Match result: {result}")

    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for entry in leaderboard:
        print(entry)

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
