import functools
import time
from collections.abc import Callable
from typing import Any


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator that prints and measures the execution time of a function"""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(
    min_power: int,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Decorator factory: reject calls where power
    argument is below min_power"""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if args and hasattr(args[0], '__dict__'):
                power = args[1] if len(args) > 1 else kwargs.get('power', 0)
            else:
                power = args[0] if args else kwargs.get('power', 0)
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(
    max_attempts: int,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Decorator factory: retry a failing function up to max_attempts times."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for i in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {i}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    """Guild that validates mage names and enforces minimum power"""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Return True if name is >= 3 chars with only letters/spaces"""
        return (
            len(name) >= 3
            and all(c.isalpha() or c.isspace() for c in name)
        )

    @power_validator(min_power=10)
    def cast_spell(self, power: int, spell_name: str) -> str:
        """Cast a spell if power meets the minimum requirement"""
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball_cast() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball_cast()
    print(f"Result: {result}")

    print("\nTesting retrying spell...")

    @retry_spell(max_attempts=3)
    def always_fails() -> str:
        raise RuntimeError("No mana")

    print(always_fails())

    _attempt: list[int] = [0]

    @retry_spell(max_attempts=3)
    def eventual_success() -> str:
        _attempt[0] += 1
        if _attempt[0] < 3:
            raise RuntimeError("Unstable")
        return "Waaaaaaagh spelled !"

    print(eventual_success())

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Aldric"))
    print(MageGuild.validate_mage_name("X2"))
    print(guild.cast_spell(15, "Lightning"))
    print(guild.cast_spell(5, "Lightning"))
