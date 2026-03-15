import time


def spell_timer(func):
    def wrapper(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - t0:.3f}s")
        return result
    return wrapper


def power_validator(min_power):
    def decorator(func):
        def wrapper(*args, **kwargs):
            power = args[2] if len(args) > 2 else kwargs.get("power", 0)
            if power < min_power:
                return "Insufficient power"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print("Retrying spell...")
            return "Spell failed"
        return wrapper
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name):
        return len(name) >= 3 and name.replace(" ", "").isalpha()

    @power_validator(10)
    def cast_spell(self, spell, power):
        return f"Cast {spell} with power {power}"


guild = MageGuild()
print(guild.cast_spell("Fireball", 15))
print(guild.cast_spell("Spark", 5))
