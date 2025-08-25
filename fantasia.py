##pag 162 - jogo de fantasia

def display_inventory(param):
    print('Inventory:')
    item_total = 0 
    for item, value in param.items():
        print(str(value)+' '+item)
        item_total += value
    print('Total Number of Items: '+str(item_total))

def add_to_inventory(inv, loot):
    for l in loot:
        inv.setdefault (l, 0)
        inv[l] += 1
    return inv


inventario = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'ruby', 'gold coin', 'gold coin']

inv = add_to_inventory(inventario, dragon_loot)
display_inventory(inv)
