inventory = {"apple": 10, "banana": 5, "orange": 8}

def add_items(inventory: dict, item: str, quantity: int) -> dict:

    if item in inventory.keys():
        inventory[item] = quantity + inventory[item]
    else:
        inventory[item] = quantity
    
    return inventory

def remove_items(inventory: dict, item: str, quantity: int) -> dict:
    if item not in inventory.keys():
        print("No Item found to remove")
        return inventory
    inventory[item] = inventory[item] - quantity
    if inventory[item] <= 0:
        inventory.pop(item)
    return inventory

def manage_inventory(inventory) -> None:
    inventory = add_items(inventory=inventory, item="mango", quantity=12)
    print(inventory)
    inventory = remove_items(inventory=inventory, item="hello",quantity=2)
    print(inventory)

    print("Final Inventory:")
    for key, quantity in inventory.items():
        print(f'{key}: {quantity}')

manage_inventory(inventory=inventory)


