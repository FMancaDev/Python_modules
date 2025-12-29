#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name: str, height=0, age=0) -> None:
        self.name = name
        self.height = height
        self.age = age
        print(f"Plant created: {self.name}")

    # getter
    def get_height(self):
        return self.height

    def get_age(self):
        return self.age

    # setters
    def set_height(self, height):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age):
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.age = age
            print(f"Age updated: {age} days [OK]\n")


if __name__ == "__main__":
    print("=== Garden Security System ===")

    plant1 = SecurePlant("Rose")

    plant1.set_height(25)
    plant1.set_age(30)

    plant1.set_height(-5)

    print("\n ======================== \n")

    plant2 = SecurePlant("Tulipa")

    plant2.set_height(44)
    plant2.set_age(58)

    plant2.set_height(10)

    print(
        f"\nCurrent plant: {plant1.name}"
        "({plant1.get_height()}cm, {plant1.get_age()} days)"
    )
