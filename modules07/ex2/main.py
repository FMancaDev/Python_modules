from ex2.EliteCard import EliteCard


def main():
    print("\n=== DataDeck Ability System ===\n")

    arcane_warrior = EliteCard("Arcane Warrior", 6, "Epic", 5, 10, 8)

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print("\nPlaying Arcane Warrior (Elite Card):\n")
    arcane_warrior.play({})

    print("Combat phase:")
    att_res = arcane_warrior.attack("Enemy")
    print(f"Attack result: {att_res}")

    def_res = arcane_warrior.defend(2)
    def_res["damage_blocked"] = 3
    print(f"Defense result: {def_res}")

    print("\nMagic phase:")
    spell_res = arcane_warrior.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print(f"Spell cast: {spell_res}")

    mana_res = arcane_warrior.channel_mana(3)
    print(f"Mana channel: {mana_res}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
