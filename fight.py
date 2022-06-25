# fighting part
import random

def fight(enemy, weapon):
    enemy_health = random.randint(1, 5)
    print(f'Fight with {enemy}, hp = {enemy_health}')
    print(f'Attacking {enemy} with {weapon}')
    while enemy_health > 0:
        enemy_health = enemy_health - 2
        print(enemy_health)
    else:
        xp = random.randint(1,5)
        coin = random.randint(0,10)
        print(f'Killed {enemy}, gained {random.randint(1,5)} xp and {coin} coin(s)')

    return coin



fight('goblin', 'sword')

def main():
    fight('wolf', 'bow')
    coin = fight('wolf', 'bow')
    print(coin)