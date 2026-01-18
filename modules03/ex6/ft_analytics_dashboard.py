#! /usr/bin/env python3


def main() -> None:
    """Executes the analytics dashboard logic using comprehensions."""
    print("=== Game Analytics Dashboard ===\n")

    data: list[tuple[str, int]] = [
        ("alice", 2300),
        ("bob", 1800),
        ("charlie", 2150),
        ("diana", 2050)
    ]
    players: list[str] = [item[0] for item in data]
    scores: list[int] = [item[1] for item in data]
    active_players: list[str] = ["alice", "bob", "charlie"]
    regions: list[str] = ["north", "east", "central", "north", "east"]

    achievements: list[tuple[str, str]] = [
        ("alice", "first_kill"),
        ("alice", "level_10"),
        ("alice", "boss_slayer"),
        ("bob", "first_kill"),
        ("bob", "level_10"),
        ("charlie", "first_kill"),
        ("charlie", "level_10"),
        ("charlie", "boss_slayer"),
        ("charlie", "master_explorer"),
        ("diana", "first_kill"),
    ]

    print("\n=== List Comprehension Examples ===")

    high_scorers: list[str] = [name for name, score in data if score > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    doubled_scores: list[int] = [score * 2 for score in scores]
    print(f"Scores doubled: {doubled_scores}")

    active: list[str] = [p for p in players if p in active_players]
    print(f"Active players: {active}")

    print("\n=== Dict Comprehension Examples ===")

    player_scores: dict[str, int] = {name: score for name, score in data}
    print(f"Player scores: {player_scores}")

    score_categories: dict[str, int] = {
        "high": len([s for s in scores if s >= 2000]),
        "medium": len([s for s in scores if 1500 <= s < 2000]),
        "low": len([s for s in scores if s < 1500]),
    }
    print(f"Score categories: {score_categories}")

    achievement_counts: dict[str, int] = {
        p: len([a for a in achievements if a[0] == p])
        for p in players
    }
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Examples ===")

    unique_players: set[str] = {p for p in players}
    print(f"Unique players: {sorted(list(unique_players))}")

    unique_achievements: set[str] = {a[1] for a in achievements}
    print(f"Unique achievements: {sorted(list(unique_achievements))}")

    active_regions: set[str] = {r for r in regions}
    print(f"Active regions: {sorted(list(active_regions))}")

    print("\n=== Combined Analysis ===")

    total_players: int = len(players)
    total_unique_achievements: int = len(unique_achievements)
    average_score: float = sum(scores) / len(scores)

    max_val: int = max([player_scores[p] for p in player_scores])
    top_player: str = [
        p for p in player_scores if player_scores[p] == max_val
    ][0]
    top_score: int = player_scores[top_player]
    top_achievements: int = achievement_counts[top_player]

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {average_score}")
    print(f"Top performer: {top_player} ({top_score} points, "
          f"{top_achievements} achievements)")


if __name__ == "__main__":
    main()
