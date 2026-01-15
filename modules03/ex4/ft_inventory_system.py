#! /usr/bin/env python3


def create_item(name, category, rarity, quantity, value):
    return {
        "name": name,
        "category": category,
        "rarity": rarity,
        "quantity": quantity,
        "value": value
    }


def inventory_value(inventory):
    total = 0
    for item in inventory.values():
        total += item["quantity"] * item["value"]
    return total


def item_count(inventory):
    count = 0
    for item in inventory.values():
        count += item["quantity"]
    return count


def categories_summary(inventory):
    categories = {}
    for item in inventory.values():
        category = item["category"]
        categories[category] = categories.get(category, 0) + item["quantity"]
    return categories


def print_inventory(player, inventory):
    print("=== " + player + "'s Inventory ===")
    for item in inventory.values():
        total = item["quantity"] * item["value"]
        print(
            item["name"] + " (" + item["category"] +
            ", " + item["rarity"] + "): "
            + str(item["quantity"]) + "x @ "
            + str(item["value"]) + " gold each = "
            + str(total) + " gold"
        )

    value = inventory_value(inventory)
    count = item_count(inventory)
    categories = categories_summary(inventory)

    print("\nInventory value:", value, "gold")
    print("Item count:", count, "items")

    cat_output = []
    for k, v in categories.items():
        cat_output.append(k + "(" + str(v) + ")")
    print("Categories:", ", ".join(cat_output))


def transfer_item(from_inv, to_inv, item_name, quantity):
    item = from_inv.get(item_name)
    if item is None or item["quantity"] < quantity:
        print("Transaction failed!")
        return

    item["quantity"] -= quantity

    if to_inv.get(item_name) is None:
        to_inv[item_name] = {
            "name": item["name"],
            "category": item["category"],
            "rarity": item["rarity"],
            "quantity": quantity,
            "value": item["value"]
        }
    else:
        to_inv[item_name]["quantity"] += quantity

    print("Transaction successful!")


def most_valuable_player(players):
    best_name = ""
    best_value = 0
    for name, inventory in players.items():
        value = inventory_value(inventory)
        if value > best_value:
            best_value = value
            best_name = name
    return best_name, best_value


def most_items_player(players):
    best_name = ""
    best_count = 0
    for name, inventory in players.items():
        count = item_count(inventory)
        if count > best_count:
            best_count = count
            best_name = name
    return best_name, best_count


def rarest_items(players):
    rare_items = {}
    for inventory in players.values():
        for item in inventory.values():
            if item["rarity"] == "rare":
                rare_items[item["name"]] = True
    return ", ".join(rare_items.keys())


# ===== MAIN PROGRAM =====

print("=== Player Inventory System ===\n")

alice_inventory = {
    "sword": create_item("sword", "weapon", "rare", 1, 500),
    "potion": create_item("potion", "consumable", "common", 5, 50),
    "shield": create_item("shield", "armor", "uncommon", 1, 200)
}

bob_inventory = {
    "magic_ring": create_item("magic_ring", "accessory", "rare", 1, 300)
}

players = {
    "Alice": alice_inventory,
    "Bob": bob_inventory
}

print_inventory("Alice", alice_inventory)

print("\n=== Transaction: Alice gives Bob 2 potions ===")
transfer_item(alice_inventory, bob_inventory, "potion", 2)

print("\n=== Updated Inventories ===")
print("Alice potions:", alice_inventory["potion"]["quantity"])
print("Bob potions:", bob_inventory["potion"]["quantity"])

print("\n=== Inventory Analytics ===")
name, value = most_valuable_player(players)
print("Most valuable player:", name, "(" + str(value) + " gold)")

name, count = most_items_player(players)
print("Most items:", name, "(" + str(count) + " items)")

print("Rarest items:", rarest_items(players))
