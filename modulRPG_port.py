import random

quest_p1 = ['You can make a few coins unloading ship cargo', 'Help rebuild inn', 'Work as bodyguard in tavern']
quest_p2 = ['Spy ill behaving citizen', 'Work as Inkeeper help', 'Brawl with thugs']
quest_p3 = ['Help mayor solve conspiracy']


def port():
    while True:
        print(random.choice(quest_p1))
        name_question = input("Want to try ?")
        name_question = name_question.capitalize()
        if name_question == "Y":
            name = True
            break
        else:
            print("\nSo maybe something else.\n")

    fcoin = random.randint(1, 10)

    while True:
        print(random.choice(quest_p2))
        name_question = input("Want to try ?")
        name_question = name_question.capitalize()
        if name_question == "Y":
            name = True
            break
        else:
            print("\nSo maybe something else.\n")

    scoin = random.randint(5, 15)

    while True:
        print(random.choice(quest_p3))
        name_question = input("Want to try ?")
        name_question = name_question.capitalize()
        if name_question == "Y":
            name = True
            break
        else:
            print("\nSo maybe something else.\n")

    tcoin = random.randint(10, 25)
    coin = fcoin + scoin + tcoin
    print(f'With {coin} gp in pocket its time to go back to crossroads')

    return coin








