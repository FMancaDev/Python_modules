#! /usr/bin/env python3

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    try:
        print("Initiating secure vault access...")

        with open("data.txt", "r") as file:
            print("Vault connection established with failsafe protocols")
            print("\nSECURE EXTRACTION:")
            print(file.read())

        with open("data.txt", "w") as file:
            print("\nSECURE PRESERVATION:")
            file.write("[CLASSIFIED] New security protocols archived")

        with open("data.txt", "r") as file:
            print(file.read())

        print("\nVault automatically sealed upon completion")
        print("All vault operations completed with maximum security.")

    except Exception as erro:
        print(f"ERROR: {erro}")
