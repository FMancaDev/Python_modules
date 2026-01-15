#! /usr/bin/env python3

import sys


def Score_Analytics():
    print("=== player Score Analytics ===\n")
    argc = len(sys.argv) - 1
    if argc < 1:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py"
            "<score1> <score2 ...>")
    else:
        try:
            score = []
            for arg in sys.argv[1:]:
                score.append(int(arg))
            print(f"Scores processed: {score}")
            print(f"Total players: {len(score)}")
            print(f"Total score: {sum(score)}")
            print(f"Average score: {sum(score) / len(score):.1f}")
            print(f"High score: {max(score)}")
            print(f"Low score: {min(score)}")
            print(f"Score range: {max(score) - min(score)}")
        except ValueError:
            print("erro try again")


if __name__ == "__main__":
    Score_Analytics()
