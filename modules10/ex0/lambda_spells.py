from typing import List, Dict


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """sorte artifact power-level in descending order using lambda"""
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Filters mages with power greater than or equal to min_power."""
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Adds markers to spell names using map and lambda."""
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """Calculates max, min, and average power using lambdas and built-ins."""
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

    powers = list(map(lambda m: m['power'], mages))
    max_p = max(powers, key=lambda p: p)
    min_p = min(powers, key=lambda p: p)
    avg_p = round(sum(powers) / len(powers), 2)

    return {
        'max_power': max_p,
        'min_power': min_p,
        'avg_power': avg_p
    }


if __name__ == "__main__":
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'}
    ]
    print("Testing artifact sorter...")
    sorted_arts = artifact_sorter(artifacts)
    for art in sorted_arts:
        print(f"{art['name']} ({art['power']} power)")

    spells = ["fireball", "heal"]
    print("\nTesting spell transformer...")
    print(" ".join(spell_transformer(spells)))

    mages = [
        {'name': 'Aria', 'power': 80},
        {'name': 'Tyron', 'power': 100}
    ]
    print("\nTesting mage stats...")
    print(mage_stats(mages))
