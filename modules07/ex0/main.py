from ex0 import CreatureCard

if __name__ == "__main__":
    print("\n=== DataDeck Card Foundation ===\n")

    try:
        dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        goblin = CreatureCard("Goblin Warrior", 4, "Common", 2, 3)

        print("Testing Abstract Base Class Design:\n")

        print("CreatureCard Info:")
        print(f"{dragon.get_card_info()}\n")

        print("Playing Fire Dragon with 6 mana available:")
        print(f"Playable: {dragon.is_playable(6)}")
        print(f"play result: {dragon.play(6)}\n")

        print("Fire Dragon attacks Goblin Warrior:")
        print(f"Attack result: {dragon.attack_target(goblin)}\n")

        print("Testing insufficient mana (3 available):")
        print(f"Playable: {dragon.is_playable(3)}\n")

        print("Abstract pattern successfully demonstrated!")

    except Exception as erro:
        print(f"[ERROR]: {erro}")
