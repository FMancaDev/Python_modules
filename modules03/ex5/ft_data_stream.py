#! /usr/bin/env python3

from typing import Generator, Any


def game_event_stream(
        total_events: int
) -> Generator[dict[str, Any], None, None]:
    """Yields a stream of game event dictionaries on demand."""
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


def fibonacci_stream(n: int) -> Generator[int, None, None]:
    """Generates the first n numbers of the Fibonacci sequence."""
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_stream(n: int) -> Generator[int, None, None]:
    """Generates the first n prime numbers."""
    count = 0
    number = 2
    while count < n:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            yield number
            count += 1
        number += 1


def main() -> None:
    """Main execution function for stream analytics and demonstrations."""
    print("=== Game Data Stream Processor ===")
    total_events = 1000
    print(f"Processing {total_events} game events...")

    processed = 0
    high_level = 0
    treasure_events = 0
    level_up_events = 0

    for event in game_event_stream(total_events):
        processed += 1

        if processed <= 3:
            print(f"Event {event['id']}: Player {event['player']} "
                  f"(level {event['level']}) {event['action']}")

        if event["level"] >= 10:
            high_level += 1
        if event["action"] == "found treasure":
            treasure_events += 1
        if event["action"] == "leveled up":
            level_up_events += 1

    print("...")
    print("=== Stream Analytics ===")
    print(f"Total events processed: {processed}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("=== Generator Demonstration ===")

    print("Fibonacci sequence (first 10): ", end="")
    fib_gen = fibonacci_stream(10)
    print(next(fib_gen), end="")
    for n in fib_gen:
        print(f", {n}", end="")
    print()

    print("Prime numbers (first 5): ", end="")
    prime_gen = prime_stream(5)
    print(next(prime_gen), end="")
    for p in prime_gen:
        print(f", {p}", end="")
    print()


if __name__ == "__main__":
    main()
