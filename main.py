##pag 162 - jogo de fantasia

import pprint

def display_inventory(param):
    final = []
    for i in param:
        qtd = 0
        qtd = qtd + param[i]
        final.append(str(qtd)+' '+i)
    pprint.pprint(final)

inventario = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

display_inventory(inventario)
