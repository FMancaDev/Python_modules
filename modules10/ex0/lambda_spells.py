def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sort magical artifacts by power level (descending)"""
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Filter mages by minimum power level."""
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Transform spell names by adding '* ' prefix and ' *' suffix"""
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """Calculate power statistics across all mages"""
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}
    powers = list(map(lambda m: m['power'], mages))
    return {
        'max_power': max(powers, key=lambda x: x),
        'min_power': min(powers, key=lambda x: x),
        'avg_power': round(
            sum(map(lambda x: x, powers)) / len(powers), 2
        ),
    }


if __name__ == "__main__":
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'orb'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'staff'},
        {'name': 'Shadow Cloak', 'power': 67, 'type': 'armor'},
    ]
    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(
        f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} power)"
        f" comes before"
        f" {sorted_artifacts[1]['name']} "
        f"({sorted_artifacts[1]['power']} power)"
    )

    mages = [
        {'name': 'Alex', 'power': 75, 'element': 'fire'},
        {'name': 'Jordan', 'power': 45, 'element': 'ice'},
        {'name': 'Riley', 'power': 90, 'element': 'lightning'},
    ]
    print("\nTesting power filter (min 70)...")
    filtered = power_filter(mages, 70)
    print([m['name'] for m in filtered])

    spells = ['fireball', 'heal', 'shield']
    print("\nTesting spell transformer...")
    print(' '.join(spell_transformer(spells)))

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(stats)
