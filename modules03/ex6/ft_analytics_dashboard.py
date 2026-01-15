#! /usr/bin/env python3

def main():
    print("=== Game Analytics Dashboard ===\n")

    # Sample data
    players = ["alice", "bob", "charlie", "diana"]
    scores = [2300, 1800, 2150, 2050]
    active_players = ["alice", "bob", "charlie"]
    regions = ["north", "east", "central", "north", "east"]

    achievements = [
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

    high_scorers = [players[i] for i in range(len(scores)) if scores[i] > 2000]
    print("High scorers (>2000):", high_scorers)

    doubled_scores = [score * 2 for score in scores]
    print("Scores doubled:", doubled_scores)

    active = [player for player in players if player in active_players]
    print("Active players:", active)

    print("\n=== Dict Comprehension Examples ===")

    player_scores = {players[i]: scores[i] for i in range(len(players))}
    print("Player scores:", player_scores)

    score_categories = {
        "high": len([s for s in scores if s >= 2000]),
        "medium": len([s for s in scores if 1500 <= s < 2000]),
        "low": len([s for s in scores if s < 1500]),
    }
    print("Score categories:", score_categories)

    achievement_counts = {
        player: len([a for a in achievements if a[0] == player])
        for player in players
    }
    print("Achievement counts:", achievement_counts)

    print("\n=== Set Comprehension Examples ===")

    unique_players = {player for player in players}
    print("Unique players:", unique_players)

    unique_achievements = {a[1] for a in achievements}
    print("Unique achievements:", unique_achievements)

    active_regions = {region for region in regions}
    print("Active regions:", active_regions)

    print("\n=== Combined Analysis ===")

    total_players = len(players)
    total_unique_achievements = len(unique_achievements)
    average_score = sum(scores) / len(scores)

    top_player = max(player_scores, key=player_scores.get)
    top_score = player_scores[top_player]
    top_achievements = achievement_counts[top_player]

    print("Total players:", total_players)
    print("Total unique achievements:", total_unique_achievements)
    print("Average score:", average_score)
    print(
        "Top performer:",
        top_player,
        "(",
        top_score,
        "points,",
        top_achievements,
        "achievements )"
    )


main()
