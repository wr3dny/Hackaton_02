import random

loot = ['axe', 'sword', 'battlehammer', 'sling', 'bow', 'crossbow', 'dagger', 'knife']
items_list = {}
new_item = random.choice(loot)
print(f'You fund {new_item}')
if input("Take y/n ") == 'y':
    items_list['weapon'] = random.randint(1, 3)
print(items_list)


