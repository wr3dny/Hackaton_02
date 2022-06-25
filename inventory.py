import random

loot = ['axe', 'sword', 'battlehammer', 'sling', 'bow', 'crossbow', 'dagger', 'knife']

def inventory():
    items_list = {}
    new_item = random.choice(loot)
    print(f'You fund {new_item}')
    if input("Take y/n ") == 'y':
        items_list[new_item] = random.randint(0,2)
    print(items_list)


inventory()