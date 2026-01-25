#! /usr/bin/env python3

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    print("Initializing new storage unit: new_discovery.txt")
    try:
        file = open("new_discovery.txt", "w")
        print("Storage unit created successfully...\n")

        print("Inscribing preservation data...")
        content: str = \
            "{[}ENTRY 001{]} New quantum algorithm discovered\n" \
            "{[}ENTRY 002{]} Efficiency increased by 347%\n" \
            "{[}ENTRY 003{]} Archived by Data Archivist trainee"
        file.write(content)
        print(content)

        print("\nData inscription complete. Storage unit sealed.")
        print(
            "Archive 'new_discovery.txt' ready for long-term preservation."
        )
        file.close()
    except Exception:
        print("ERROR: Could not create storage vault")
