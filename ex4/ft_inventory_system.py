import sys

def bubble_sort(my_list: list) -> list:
    """Sorts a list of numbers in ascending order using bubble sort."""
    n = len(my_list)

    for i in range(n):
        for j in range(0, n - 1):
            if my_list[j]['qty'] < my_list[j + 1]['qty']:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

    return my_list

def dict_lookup(list_of_dic: list, value: str) -> bool:
    for item_name, item_details in list_of_dic:
        if item_name == value:
            return True
    return False

def main() -> None:
    """Run the inventory system demonstration."""
    print("=== Player Inventory System ===")
    print("\n=== Alice's Inventory ===")

    inventory = dict()
    unique_items = set()
    global sum_of_qty
    sum_of_qty = 0


    args = sys.argv[1:]
    try:
        for i, arg in enumerate(args):

            name, qty_str = arg.split(':')
            current_qty = inventory.get(name, {}).get("qty", 0)

            new_qty = current_qty + int(qty_str)
            new_item = {name: {
                        "qty": new_qty,
                        "index": i
                            }
                        }
            inventory.update(new_item)
            sum_of_qty += int(qty_str)
            unique_items.add(name)
    except Exception as e:
        print(e)

    print(f"Total items in inventory: {sum_of_qty}")
    print(f"Unique item types: {len(unique_items)}\n")

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
        str_output += f" ({(qty / sum_of_qty * 100):.1f}%)"
        print(f"{str_output}")


    print("\n=== Inventory Statistics ===")
    most = None
    least = None
    if sorted_inventory != []:
        most = sorted_inventory[0]
        least = sorted_inventory[-1]
        print(f"Most abundant: {most['name']} ({most['qty']} {'units' if most['qty'] > 1 else 'unit'})")
        print(f"Least abundant: {least['name']} ({least['qty']} {'units' if least['qty'] > 1 else 'unit'})")

    print("\n=== Item Categories ===")
    moderate_items = []
    scarce_items = []

    for item in sorted_inventory:
        if item['qty'] >= 5:
            moderate_items.append(item)
        else:
            scarce_items.append(item)

    print("Moderate: ", end="")
    print("{", end="")
    for item in moderate_items:
        if item != moderate_items[-1]:
            print(f"'{item['name']}': {item['qty']}", end=", ")
        else:
            print(f"'{item['name']}': {item['qty']}", end = "")
    print("}")
    print(f"Scarce: ", end="")
    print("{", end="")
    for item in scarce_items:
        if item != scarce_items[-1]:
            print(f"'{item['name']}': {item['qty']}", end = ", ")
        else:
            print(f"'{item['name']}': {item['qty']}", end="")
    print("}")
    print()
    print("=== Management Suggestions ===")
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
    items = list(inventory.items())
    for item in items:
        item_name, item_details = item
        if item != items[-1]:
            print(item_name, end = ", ")
        else:
            print(item_name, end = "")
    print()
    print("Dictionary values: ", end="")
    for item in items:
        item_name, item_details = item
        if item != items[-1]:
            print(item_details['qty'], end = ", ")
        else:
            print(item_details['qty'], end = "")
    print()
    print(f"Sample lookup - 'sword' in inventory: {dict_lookup(inventory.items(), 'sword')}")
if __name__ == "__main__":
    main()
