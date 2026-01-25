#! /usr/bin/env python3

def crisis_handler(filename: str) -> None:
    try:
        if filename == "standard_archive.txt":
            print(f"\nROUTINE ACCESS: Attempting access to '{filename}'...")
        else:
            print(f"\nCRISIS ALERT: Attempting access to '{filename}'...")

        with open(filename, "r") as file:
            content = file.read()
            print(f"SUCCESS: Archive recovered - ``{content}''")
            print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis handled, system stable")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    files_to_test: list[str] = [
        "lost_archive.txt",
        "classified_vault.txt",
        "standard_archive.txt"
    ]

    for filename in files_to_test:
        crisis_handler(filename)

    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
