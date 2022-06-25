import random


def random_enemy():
    who_random = ['pixie', 'banshee', 'werewolf', 'skeleton', 'zombie', 'dwarf', 'bestigor', 'goblin', 'skaven']
    occupations_random = [' bodyguard', ' hangman', ' tax collector', ' miner', ' mime', ' innkeeper', ' gardener',
                      ' servant', ' shaman', ' archer', ' cook', ' ring bearer', ' troll slayer']

    picked_enemy = random.choice(who_random)
    picked_class = random.choice(occupations_random)
    rg_enemy = picked_enemy + picked_class
    return rg_enemy






