#! /usr/bin/env python3

import sys

def score_analytics():
    print("=== Player Score Analytics ===\n")
    args = sys.argv[1:]
    if len(args) < 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    try:
        score = []
        for arg in args:
            score += [int(arg)]
        print(f"Scores processed: {score}")
        print(f"Total players: {len(score)}")
        print(f"Total score: {sum(score)}")
        print(f"Average score: {sum(score) / len(score):.1f}") 
        print(f"High score: {max(score)}")
        print(f"Low score: {min(score)}")
        print(f"Score range: {max(score) - min(score)}")
    except ValueError:
        print("Error: Please provide valid integer scores.")

if __name__ == "__main__":
    score_analytics()
