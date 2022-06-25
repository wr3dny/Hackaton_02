import random
from modulRPG_enemy import random_enemy
from modulRPG_attack import attack

enemy = random_enemy()

quest_p1 = ['Help digging down the mine', 'Trade with dwarf']
quest_p2 = [f'Help fight {enemy} from near mines', f'Fight with {enemy}',
            f'Kill spying {enemy}']
quest_p3 = ['Travel back to crossroads']


def mountains():
    while True:
        print(random.choice(quest_p1))
        name_question = input("Want to try ?")
        name_question = name_question.capitalize()
        if name_question == "Y":
            name = True
            break
        else:
            print("\nSo maybe something else.\n")

    fcoin = random.randint(1, 5)


    while True:
        print(random.choice(quest_p2))
        name_question = input("Want to try ?")
        name_question = name_question.capitalize()
        if name_question == "Y":
            name = True
            attack()
            break
        else:
            print("\nSo maybe something else.\n")

    scoin = random.randint(2, 7)


    while True:
        print(random.choice(quest_p3))
        name_question = input("Want to try ?")
        name_question = name_question.capitalize()
        if name_question == "Y":
            name = True
            break
        else:
            print("\nSo maybe something else.\n")


    coin = fcoin + scoin
    print(f'With {coin} gp in pocket its time to go back to crossroads')
    return coin

