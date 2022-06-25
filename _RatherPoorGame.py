# 02 Hackaton

import sys
from modulRPG_name_generator import name_generator
from modulRPG_menu import what_to_do
from modulRPG_port import port
from modulRPG_mountains import mountains
from modulRPG_forrest import forrest
from modulRPG_castle import castle
from modulRPG_village import village

inventory = {
    'food': 0,
    'weapon': 0,
    'gold': 0}


def hero_attributes(hero_name):

    hero_att = {
        'name': hero_name,
        'health' : 20,
        'energy' : 20,
        'attack' : 1
     }
    return hero_att


def hero_sex(name):
    if name[-1] == 'a':
        he_she = 'lady'
    else:
        he_she = 'sir'
    return he_she

def crossroads():
    answers = ['M', 'V', 'C', 'F', 'P']
    answer = input('Mountains (M) \n'
                   'Village (V) \n'
                   'Castle (C) \n'
                   'Forrest (F) \n'
                   'Port (P)\n'
                   '>>>> '
                   )
    while answer.capitalize() not in answers:
        answer = input('Enter your answer: ')

    # if answer.capitalize() == 'M':
    #     print('You travel up the slope of the mountains.')
    # elif answer.capitalize() == 'V':
    #     print(f'You go straight to peaceful (?) village. ')
    # elif answer.capitalize() == 'C':
    #     print(f'You castle. Maybe there a princess to rescue. ')
    # elif answer.capitalize() == 'F':
    #     print(f'You enter deep gloomy forrest.')

    return answer

def main():
    menu_choice = int(what_to_do())
    if menu_choice == 1:
        hero_name = name_generator()
        hero = hero_attributes(hero_name)

    elif menu_choice == 2:
        with open ('save.txt') as f:
            content = f.readlines()
            hero = content

    elif menu_choice == 3:
        print('No time for fun. Understood')
        sys.exit()

    sir_lady = hero_sex(hero_name)
    print(f'{sir_lady.capitalize()} {hero_name}, Your journey beggins,\n'
          f'please pick up where to go')
    direction = crossroads()
    if direction.capitalize() == 'P':
        print(f'So, {sir_lady.capitalize()} {hero_name} wants to sea the see.')
        story = port()
        coin = story
        inventory['gold'] = coin
    elif direction.capitalize() == 'V':
        print('You go straight to peaceful (?) village.')
        story = village()
    elif direction.capitalize() == 'C':
        print(f'You go straight to peaceful (?) village. ')
        story = castle()
    elif direction.capitalize() == 'F':
        print(f'You enter deep gloomy forrest.')
        story = forrest()
    elif direction.capitalize() == 'M':
        print('You travel up the slope of the mountains.')
        story = mountains()
    fv = inventory.get('food')
    wv = inventory.get('weapon')
    gv = inventory.get('gold')
    hero
    na = hero.get('name')
    ha = hero.get('health')
    ea = hero.get('energy')
    aa = hero.get('attack')

    with open('save.txt', 'w') as f:
        f.write(f'food: {fv} \n')
        f.write(f'weapon: {wv} \n')
        f.write(f'gold: {gv} \n')
        f.write(f'name: {na} \n')
        f.write(f'health: {ha} \n')
        f.write(f'energy: {ea} \n')
        f.write(f'attack: {aa} \n')

    direction = crossroads()
    if direction.capitalize() == 'P':
        print(f'So, {sir_lady.capitalize()} {hero_name} wants to sea the see.')
        story = port()
        coin = story
        inventory['gold'] = coin
    elif direction.capitalize() == 'V':
        print('You go straight to peaceful (?) village.')
        story = village()
    elif direction.capitalize() == 'C':
        print(f'You go straight to peaceful (?) village. ')
        story = castle()
    elif direction.capitalize() == 'F':
        print(f'You enter deep gloomy forrest.')
        story = forrest()
    elif direction.capitalize() == 'M':
        print('You travel up the slope of the mountains.')
        story = mountains()
    fv = inventory.get('food')
    wv = inventory.get('weapon')
    gv = inventory.get('gold')
    hero
    na = hero.get('name')
    ha = hero.get('health')
    ea = hero.get('energy')
    aa = hero.get('attack')

    with open('save.txt', 'w') as f:
        f.write(f'food: {fv} \n')
        f.write(f'weapon: {wv} \n')
        f.write(f'gold: {gv} \n')
        f.write(f'name: {na} \n')
        f.write(f'health: {ha} \n')
        f.write(f'energy: {ea} \n')
        f.write(f'attack: {aa} \n')





if __name__ == '__main__':
    main()
