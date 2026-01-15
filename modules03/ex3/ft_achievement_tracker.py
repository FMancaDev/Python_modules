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

print("=== Achievement Tracker System ===")
print("Player alice achievements:", alice)
print("Player bob achievements:", bob)
print("Player charlie achievements:", charlie)

print("=== Achievement Analytics ===")

# achivements únicos
all_achievements = alice.union(bob).union(charlie)
print("All unique achievements:", all_achievements)
print("Total unique achievements:", len(all_achievements))

# achivements comúns a todos os jogadores
common_all = alice.intersection(bob).intersection(charlie)
print("Common to all players:", common_all)

# achivements raros (só 1 jogador)
rare_achievements = (
    alice.difference(bob).difference(charlie)
    .union(bob.difference(alice).difference(charlie))
    .union(charlie.difference(alice).difference(bob))
)
print("Rare achievements (1 player):", rare_achievements)

alice_bob_common = alice.intersection(bob)
print("Alice vs Bob common:", alice_bob_common)

alice_unique = alice.difference(bob)
print("Alice unique:", alice_unique)

bob_unique = bob.difference(alice)
print("Bob unique:", bob_unique)
