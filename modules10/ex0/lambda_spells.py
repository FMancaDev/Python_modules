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

    max_power =
