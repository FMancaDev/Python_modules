import functools
import time
from collections.abc import Callable
from typing import Any


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    """Mede tempo de execução com 3 casas decimais[cite: 410, 413]."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Valida se o primeiro argumento (power) é suficiente[cite: 416, 418, 419]."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = args[0] if args else kwargs.get('power', 0)
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Tenta executar a função até max_attempts vezes[cite: 422, 424, 426]."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for i in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... (attempt {i}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Valida nome (>=3 caracteres, apenas letras/espaços)[cite: 428, 430]."""
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, power: int, spell_name: str) -> str:
        """Instância validada pelo power_validator[cite: 431, 432, 433]."""
        return f"Successfully cast {spell_name} with {power} power"
