# inventory.py
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    global inv
    print("Inventory:")
    item_total = 0
    for k, v in inv.items():
        print(str(v) + ' ' + str(k))
        item_total =  sum(inv.values())
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    # your code goes here
    for i in range(len(addedItems)):
        inv.setdefault(addedItems[i], 0) # Adds new items
        inv[addedItems[i]] = inv[addedItems[i]] + 1 # Adding existing items
    return inv

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
