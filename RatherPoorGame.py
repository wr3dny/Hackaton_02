# RPG
# step by step so called 'concept'
from RPG_name_generator import name_generator


def hero_sex(name):
    if name[-1] == 'a':
        he_she = 'lady'
    else:
        he_she = 'sir'
    return he_she


import random

loot = ['axe', 'sword', 'battlehammer', 'sling', 'bow', 'crossbow', 'dagger', 'knife']

def inventory():
    items_list = []
    new_item = random.choice(loot)
    print(f'You fund {new_item}')
    if input("Take y/n ") == 'y':
        items_list.append(f'{new_item}')
    print(items_list)


def crossroads():
    try:
        picked_direction = input('Mountains (M) \n'
                             'Village (V) \n'
                             'Castle (C) \n'
                             'Forrest (F) \n'
                             '>>>> '
                             )
    except ValueError:
        print('Destination not in current version, try again (maybe from list ?)')

    if picked_direction.capitalize() == 'M':
        print(f'You travel up the slope of the mountains')



def mountains():
    import RPG_enemy as enemy
    print(f'On your way you come upon {enemy}')
    print('Fight or run (r/f)')
    choice = input()
    if choice.capitalize() == 'R':
        print('You run off')
        run = 'run'
        return run
    # elif choice.capitalize() == 'F':
    #     # fight()
    # exc




# def village():
#     pass
#
#
# def castle():
#     pass
#
#
# def forrest():
#     pass


def main():
    hero_name = name_generator()
    he_she = hero_sex(hero_name)
    print(f'{he_she.capitalize()} {hero_name} Your journey beggins' )
    try:
        crossroads()
    except (TypeError, ValueError):
        crossroads()
    if mountains() == 'run':
        crossroads()
    pass


if __name__ == '__main__':
    main()
