from typing import List, Dict


def artifact_sorter(artifacts: List[Dict]) -> List[Dict]:
    """Ordena artefactos por poder decrescente."""
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: List[Dict], min_power: int) -> List[Dict]:
    """Filtra mages com poder >= min_power."""
    # filter devolve um iterador - converter para list
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: List[str]) -> List[str]:
    """Adiciona prefixo e sufixo aos feitiços."""
    # map devolve um iterador - converter para list
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: List[Dict]) -> Dict:
    """Calcula estatísticas usando lambdas."""
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

    # Extai os poderes para ser usado varias vezes
    powers = list(map(lambda m: m['power'], mages))

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

    print("\nTesting spell transformer...")
    transformed = spell_transformer(["fireball", "heal", "shield"])
    print(" ".join(transformed))
