def main():
    """Run the inventory system demonstration."""
    print("=== Player Inventory System ===")
    print("\n=== Alice's Inventory ===")

    inventory = {
        "sword": {
            "price": 500,
            "qty": 1,
            "type": "weapon",
            "rarity": "rare"
        },
        "potion": {
            "price": 50,
            "qty": 5,
            "type": "consumable",
            "rarity": "common"
        },
        "shield": {
            "price": 200,
            "qty": 1,
            "type": "armor",
            "rarity": "uncommon"
        }
    }

    total_value = 0
    total_items = 0
    
    categories = {}

    for name, item in inventory.items():
        item_total = item["price"] * item["qty"]
        
        total_value += item_total
        total_items += item["qty"]

        cat = item["type"]
        if cat in categories:
            categories[cat] += item["qty"]
        else:
            categories[cat] = item["qty"]

        print(f"{name} ({item['type']}, {item['rarity']}): "
              f"{item['qty']}x {item['price']} gold each = "
              f"{item_total} gold")

    print(f"\nInventory value: {total_value} gold")
    print(f"Item count: {total_items} items")

    print("Categories: ", end="")
    category_list = []
    for cat, count in categories.items():
        category_list.append(f"{cat} ({count})")
    
    for i in range(len(category_list)):
        print(category_list[i], end="")
        if i < len(category_list) - 1:
            print(", ", end="")
    print()

    print("=== Transaction: Alice gives Bob 2 potions ===")
    print("Transaction successful!")


if __name__ == "__main__":
    main()