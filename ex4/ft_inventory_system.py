import sys

def bubble_sort(my_list: list) -> list:
    """Sorts a list of dictionaries in descending order by quantity using bubble sort."""
    n = len(my_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if my_list[j]['qty'] < my_list[j + 1]['qty']:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list

def main() -> None:
    """Run the inventory system demonstration."""
    print("=== Player Inventory System ===")
    print("\n=== Alice's Inventory ===")

    inventory = dict()
    sum_of_qty = 0

    args = sys.argv[1:]
    
    for i, arg in enumerate(args):
        try:
            name, qty_str = arg.split(':')
            added_qty = int(qty_str)

            current_qty = inventory.get(name, {}).get("qty", 0)
            new_qty = current_qty + added_qty
            
            new_item = {
                name: {
                    "qty": new_qty,
                    "index": i
                }
            }
            inventory.update(new_item)
            sum_of_qty += added_qty
        except Exception:
            print(f"Warning: Invalid format for '{arg}'. Expected name:qty.")

    print(f"Total items in inventory: {sum_of_qty}")
    print(f"Unique item types: {len(inventory.keys())}\n")

    print("=== Current Inventory ===")
    
    sorted_inventory = []
    
    for item_name, item_details in inventory.items():
        single_item_dict = {"name": item_name}
        single_item_dict.update(item_details)
        sorted_inventory.append(single_item_dict)
        
    sorted_inventory = bubble_sort(sorted_inventory)

    for item in sorted_inventory:
        qty = item["qty"]
        name = item["name"]
        
        str_output = f"{name}: {qty}"
        str_output += " units" if qty > 1 else " unit"
        if sum_of_qty > 0:
            str_output += f" ({(qty / sum_of_qty * 100):.1f}%)"
        print(str_output)

    print("\n=== Inventory Statistics ===")
    if len(sorted_inventory) > 0:
        most = sorted_inventory[0]
        least = sorted_inventory[-1]
        print(f"Most abundant: {most['name']} ({most['qty']} {'units' if most['qty'] > 1 else 'unit'})")
        print(f"Least abundant: {least['name']} ({least['qty']} {'units' if least['qty'] > 1 else 'unit'})")

    print("\n=== Item Categories ===")
    moderate_items = dict()
    scarce_items = dict()

    for item in sorted_inventory:
        name = item['name']
        qty = item['qty']
        if qty >= 5:
            moderate_items.update({name: qty})
        else:
            scarce_items.update({name: qty})

    print(f"Moderate: {moderate_items}")
    print(f"Scarce: {scarce_items}")

    print("\n=== Management Suggestions ===")
    print("Restock needed: ", end="")
    first = True
    for item in sorted_inventory:
        if item['qty'] <= 1:
            if first:
                print(item['name'], end="")
                first = False
            else:
                print(f", {item['name']}", end="")
    print()

    print("\n=== Dictionary Properties Demo ===")
    
    print("Dictionary keys: ", end="")
    first = True
    for key in inventory.keys():
        if not first:
            print(", ", end="")
        print(key, end="")
        first = False
    print()
    
    print("Dictionary values: ", end="")
    first = True
    for val in inventory.values():
        if not first:
            print(", ", end="")
        print(val.get('qty', 0), end="") 
        first = False
    print()

    is_sword_present = 'sword' in inventory
    print(f"\nSample lookup - 'sword' in inventory: {is_sword_present}")

if __name__ == "__main__":
    main()