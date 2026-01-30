from .basic import lead_to_gold
from ..potions import healing_potions


def philosophers_stone() -> str:
    return (
        f"Philosopher’s stone created using "
        f" {lead_to_gold()} and {healing_potions()}"
    )


def elixir_of_life() -> str:
    return "Elixir of life: eternal youth achieved!"
