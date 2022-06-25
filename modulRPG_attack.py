# attack
from colorama import Fore, Style

from modulRPG_hero_attributes import hero_att
from modulRPG_inventory import current_inventory
from modulRPG_enemy import random_enemy
import random


def attack():
    h = hero_att()
    hh = h.get('health')
    ha = h.get('attack')
    he = h.get('energy')
    hi = current_inventory


    enemy_name = random_enemy()
    enemy_str = random.randint(1, 3)
    enemy_healt = random.randint(5, 10)
    enemy_1 = {'name': enemy_name,
               'attack': enemy_str,
               'health': enemy_healt}
    eh = enemy_1.get('health')

    while hh > 0 and eh > 0:
        i = 0
        hh = hh - enemy_1.get('attack')
        eh = eh - ha

        if eh == 0:
            print(f'Killed {enemy_name.capitalize()}')
            # coin = random.randint(0, 5)
            # print(f'Looted corpse for {coin} gp')
        elif hh == 0:
            print('You died')
    hhh = h.get('health') - hh
    # print(f'{title.capitalize()} {name} health {hh}')
    print(f'Your health is currently {hh}')
    print(Fore.YELLOW + str(hh) + ' ' + Fore.GREEN + (hh * '[X]') + (hhh * '[]'))
    print(Style.RESET_ALL)






