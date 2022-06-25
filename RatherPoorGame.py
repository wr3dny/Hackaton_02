# 02

import sys
from RPG_name_generator import name_generator

inventory = {
    'food': 0,
    'weapon': 0,
    'gold' : 0
}

def what_to_do():
    print('|| Welcome||')
    print('What You want to do ?')
    options = int(input('1 - new game, 2 - continue, 3 - quit'))
    return options

def menu():
    try:
        what_to_do()
    except ValueError as e:
        print('Its not what I meant')


def hero_sex(name):
    if name[-1] == 'a':
        he_she = 'lady'
    else:
        he_she = 'sir'
    return he_she

def crossroads():
    while True:
        picked_direction = input('Mountains (M) \n'
                                 'Village (V) \n'
                                 'Castle (C) \n'
                                 'Forrest (F) \n'
                                 'Port (P)\n'
                                 '>>>> '
                                 )
        if picked_direction.capitalize() == 'M':
            picked_direction = True
            break
        elif picked_direction.capitalize() == 'C':
            picked_direction = True
            break
        elif picked_direction.capitalize() == 'V':
            picked_direction = True
            break
        elif picked_direction.capitalize() == 'F':
            picked_direction = True
            break
        elif picked_direction.capitalize() == 'P':
            picked_direction = True
            break
        else:
            print('Direction currently not available')
        return str(picked_direction)


import random



# def inventory():
#     items_list = []
#     new_item = random.choice(loot)
#     print(f'You fund {new_item}')
#     if input("Take y/n ") == 'y':
#         items_list.append(f'{new_item}')
#     print(items_list)





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
    menu()
    hero_name = name_generator()
    he_she = hero_sex(hero_name)
    hero_inventory = inventory
    print(f'{he_she.capitalize()} {hero_name} Your journey beggins,\n'
          f'please pick up where to go')
    direction = crossroads()
    print(direction)

    # if direction.capitalize() == 'M':
    #     print(f'You travel up the slope of the mountains.')
    # elif direction.capitalize() == 'V':
    #     print(f'You go straight to peaceful (?) village. ')
    # elif direction.capitalize() == 'C':
    #     print(f'You castle. Maybe theres a princess to rescue. ')
    # elif direction.capitalize() == 'F':
    #     print(f'You enter deep gloomy forrest. ')





if __name__ == '__main__':
    main()
