#! /usr/bin/env python3

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    print("Accessing Storage Vault: ancient\\_fragment.txt")
    try:
        file = open("ancient_fragment.txt", "r")
        print("Connection established...")
        print("\nRECOVERY DATA:")
        print(file.read())
        print("Data recovery complete. Storage unit disconnected.")
        file.close()
    except Exception:
        print("ERROR: Storage vault not found")
