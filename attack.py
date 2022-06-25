# attack

from hero_att import hero_attributes
from RPG_inventory import items_list
from RPG_enemy import random_enemy
import random


def hero_combat():
    hero_str = hero_attributes.get('attack')
    weapon = items_list.get('weapon')
    health = hero_attributes.get('health')
    hero = hero_str + weapon
    return total_att


def enemy_unit():
    enemy_name = random_enemy()
    enemy_str = random.randint(1, 3)
    enemy_healt = random.randint(5, 10)
    enemy_1 = {'name': enemy_name,
               'strength' : enemy_str,
               'health' : enemy_healt}
    return enemy_1


def main():
    enemy = enemy_unit()
    enemy_n = enemy.get('name')
    print(f'You fight with {enemy_n.capitalize()} ')
    dd = attack_strength()
    while j > 0 for j in





if __name__ == '__main__':
    main()