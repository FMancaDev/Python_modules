from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


def main():
    print("\n=== DataDeck Game Engine ===\n")

    engine = GameEngine()
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print("Configuring Fantasy Card Game...")
    engine.configure_engine(factory, strategy)
    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")

    supported = factory.get_supported_types()
    print(f"Available types: {supported}")

    print("\nSimulating aggressive turn...")
    result = engine.simulate_turn()

    hand_str = ", ".join(result["hand_display"])
    print(f"Hand: [{hand_str}]")

    print("\nTurn execution:")
    exec_res = result["execution_result"]
    print(f"Strategy: {exec_res['strategy']}")
    print(f"Actions: {exec_res['actions']}")

    print("\nGame Report:")
    print(engine.get_engine_status())

    print(
        "\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!"
    )


if __name__ == "__main__":
    main()
