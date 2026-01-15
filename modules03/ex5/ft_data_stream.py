#! /usr/bin/env python3

def game_event_stream(total_events):
    players = ["alice", "bob", "charlie", "diana"]
    actions = ["killed monster", "found treasure", "leveled up"]

    for i in range(total_events):
        player = players[i % len(players)]
        action = actions[i % len(actions)]
        level = (i * 3) % 20 + 1

        yield {
            "id": i + 1,
            "player": player,
            "level": level,
            "action": action
        }


def fibonacci_stream(n):
    a = 0
    b = 1

    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_stream(n):
    count = 0
    number = 2

    while count < n:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
        if is_prime:
            yield number
            count += 1
        number += 1


def main():
    print("=== Game Data Stream Processor ===\n")
    total_events = 1000
    print("Processing", total_events, "game events...\n")

    processed = 0
    high_level = 0
    treasure_events = 0
    level_up_events = 0

    for event in game_event_stream(total_events):
        processed += 1

        if processed <= 3:
            print(
                "Event", event["id"], ":",
                "Player", event["player"],
                "(level", event["level"], ")",
                event["action"]
            )

        if event["level"] >= 10:
            high_level += 1
        if event["action"] == "found treasure":
            treasure_events += 1
        if event["action"] == "leveled up":
            level_up_events += 1

    print("...\n")
    print("=== Stream Analytics ===")
    print("Total events processed:", processed)
    print("High-level players (10+):", high_level)
    print("Treasure events:", treasure_events)
    print("Level-up events:", level_up_events)
    print("\nMemory usage: Constant (streaming)")
    print("Processing time: Very fast")

    print("\n=== Generator Demonstration ===")

    print("Fibonacci sequence (first 10):", end=" ")
    for n in fibonacci_stream(10):
        print(n, end=", ")
    print()

    print("Prime numbers (first 5):", end=" ")
    for p in prime_stream(5):
        print(p, end=", ")
    print()


main()
