import functools
import time


def spell_timer(func: callable) -> callable:
    """Decorator that measures and prints function execution time"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:
    """Decorator factory that validates power level >= min_power"""
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if args and hasattr(args[0], '__dict__'):
                power = kwargs.get('power', args[2] if len(args) > 2 else 0)
            else:
                power = kwargs.get('power', args[0] if args else 0)
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    """Decorator that retries a function up to max_attempts on exception"""
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    """Guild of mages with validation and spell casting capabilities"""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Return True if name has >= 3 chars and only letters/spaces"""
        return (
            len(name) >= 3
            and all(c.isalpha() or c.isspace() for c in name)
        )

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell if power is sufficient"""
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    print("Testing spell timer...")
    result = fireball()
    print(f"Result: {result}")

    print("\nTesting retry decorator...")
    attempt_count = [0]

    @retry_spell(max_attempts=3)
    def unstable_spell():
        attempt_count[0] += 1
        if attempt_count[0] < 3:
            raise RuntimeError("Spell unstable!")
        return "Stable spell cast!"

    print(unstable_spell())

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Merlin"))
    print(MageGuild.validate_mage_name("X2"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))
