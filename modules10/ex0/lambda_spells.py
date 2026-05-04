from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Sort artifacts by power level in descending order"""
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(
    mages: list[dict[str, Any]], min_power: int
) -> list[dict[str, Any]]:
    """Filter mages with power >= min_power"""
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Add '* ' prefix and ' *' suffix to each spell name"""
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    """Calculate max, min, and average power using lambdas"""
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}
    powers: list[int] = list(map(lambda m: m['power'], mages))
    return {
        'max_power': max(powers),
        'min_power': min(powers),
        'avg_power': round(sum(powers) / len(powers), 2)
    }


if __name__ == "__main__":
    print("\nTesting artifact sorter...")
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'}
    ]
    sorted_arts = artifact_sorter(artifacts)
    print(f"{sorted_arts[0]['name']} ({sorted_arts[0]['power']} power) "
          f"comes before {sorted_arts[1]['name']} "
          f"({sorted_arts[1]['power']} power)")

    print("\nTesting power filter...")
    mages = [
        {'name': 'Aldric', 'power': 75, 'element': 'fire'},
        {'name': 'Zara', 'power': 45, 'element': 'ice'},
        {'name': 'Oryn', 'power': 90, 'element': 'lightning'}
    ]
    strong_mages = power_filter(mages, 70)
    print(f"Mages with power >= 70: {[m['name'] for m in strong_mages]}")

    print("\nTesting spell transformer...")
    transformed = spell_transformer(["fireball", "heal", "shield"])
    print(" ".join(transformed))

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(f"Max: {stats['max_power']}, Min: {stats['min_power']}, "
          f"Avg: {stats['avg_power']}")
