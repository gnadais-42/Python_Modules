import sys

def args_to_dict():
    final = dict()
    args = sys.argv[1:]
    for arg in args:
        pair = arg.split(":")
        if len(pair) != 2:
            print(f"Argument {arg} in invalid format (\"Key:Value\")")
            continue
        try:
            final.update({pair[0]: int(pair[1])})
        except ValueError as e:
            print(f"Error: {e}")
    return final


def analysis(inventory):
    total_items = 0
    for value in inventory.values():
        total_items += value
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}\n")


def print_inventory(inventory):
    print("=== Current Inventory ===")
    if not inventory:
        print("Inventory is empty\n")
        return
    total_items = 0
    for value in inventory.values():
        total_items += value
    temp = dict()
    temp.update(inventory)
    while len(temp) > 0:
        max_key = None
        for k in temp:
            max_key = k
            break
        for k in temp:
            if temp.get(k) > temp.get(max_key):
                max_key = k
        value = temp.get(max_key)
        percentage = round(value * 100 / total_items, 1)
        print(f"{max_key}: {value} units ({percentage}%)")
        del temp[max_key]
    print()


def statistics(inventory):
    print("=== Inventory Statistics ===")
    if not inventory:
        print("Inventory is empty\n")
        return
    max_k = None
    for key in inventory.keys():
        max_k = key
        break
    min_k = max_k
    for key in inventory:
        if inventory.get(key) > inventory.get(max_k):
            max_k = key
        elif inventory.get(key) < inventory.get(min_k):
            min_k = key
    print(f"Most abundant: {max_k} ({inventory.get(max_k)} {"units" if inventory.get(max_k) != 1 else "unit"})")
    print(f"Least abundant: {min_k} ({inventory.get(min_k)} {"units" if inventory.get(min_k) != 1 else "unit"})")
    print()
    

def categories(inventory):
    print("=== Item Categories ===")
    if not inventory:
        print("Inventory is empty\n")
        return
    abundant = dict()
    moderate = dict()
    scarce = dict()
    for item in inventory.items():
        if item[1] < 4:
            scarce.update({item[0]: item[1]})
        elif item[1] < 7:
            moderate.update({item[0]: item[1]})
        else:
            abundant.update({item[0]: item[1]})
    if abundant:
        print(f"Abundant: {abundant}")
    if moderate:
        print(f"Moderate: {moderate}")
    if scarce:
        print(f"Scarce: {scarce}")
    print()


def management(inventory):
    print("=== Management Suggestions ===")
    if not inventory:
        print("Inventory is empty\n")
        return
    restock = dict()
    min_value = None
    for value in inventory.values():
        min_value = value
        break
    for value in inventory.values():
        if value < min_value:
            min_value = value
    for key in inventory:
        if inventory.get(key) == min_value:
            restock.update({key: min_value})
    print(f"Restock needed: [", end="")
    first = True
    for key in restock:
        if not first:
            print(", ", end="")
        print(f"\'{key}\'", end="")
        first = False
    print("]")
    print()


def demo(inventory):
    print("=== Dictionary Properties Demo ===")
    if not inventory:
        print("Inventory is empty")
        return
    print("Dictionary keys: [", end="")
    first = True
    for key in inventory:
        if not first:
            print(", ", end="")
        print(f"\'{key}\'", end="")
        first = False
    print("]")
    print("Dictionary values: [", end="")
    first = True
    for value in inventory.values():
        if not first:
            print(", ", end="")
        print(value, end="")
        first = False
    print("]")
    print("Sample lookup - \'sword\' in inventory: "
    f"{True if "sword" in inventory else False}")
    



inventory = args_to_dict()
analysis(inventory)
print_inventory(inventory)
statistics(inventory)
categories(inventory)
management(inventory)
demo(inventory)