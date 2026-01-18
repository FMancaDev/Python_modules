#! /usr/bin/env python3

alice = set([
    "first_kill",
    "level_10",
    "treasure_hunter",
    "speed_demon"
])

bob = set([
    "first_kill",
    "level_10",
    "boss_slayer",
    "collector"
])

charlie = set([
    "level_10",
    "treasure_hunter",
    "boss_slayer",
    "speed_demon",
    "perfectionist"
])

print("=== Achievement Tracker System ===\n")
print("Player alice achievements:", alice)
print("Player bob achievements:", bob)
print("Player charlie achievements:", charlie)

print("\n=== Achievement Analytics ===")

# unique achivements
all_achievements: set[str] = alice.union(bob).union(charlie)
print("All unique achievements:", all_achievements)
print("Total unique achievements:", len(all_achievements))

# comuns achivements
common_all: set[str] = alice.intersection(bob).intersection(charlie)
print("\nCommon to all players:", common_all)

# rare achivements
rare_achievements: set[str] = (
    alice.difference(bob).difference(charlie)
    .union(bob.difference(alice).difference(charlie))
    .union(charlie.difference(alice).difference(bob))
)
print("Rare achievements (1 player):", rare_achievements)

alice_bob_common: set[str] = alice.intersection(bob)
print("\nAlice vs Bob common:", alice_bob_common)

alice_unique: set[str] = alice.difference(bob)
print("Alice unique:", alice_unique)

bob_unique: set[str] = bob.difference(alice)
print("Bob unique:", bob_unique)
