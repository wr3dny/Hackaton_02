# attack

from hero_att import hero_attributes
from RPG_inventory import items_list
import random

def attack_strenght():
    hero_str = hero_attributes('attack')
    weapon = items_list('weapon')
    total_att = hero_str + weapon
    return total_att


def enemy_strenght():
    enemy_str = random.randint(1,3)
    return enemy_str

def main():
    hero_attack = attack_strenght()
    enemy_attack = enemy_strenght()


if __name__ == '__main__':
    main()