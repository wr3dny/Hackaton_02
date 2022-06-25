import random

quest_p1 = ['You can make a few coins unloading ship cargo', 'Help rebuild inn', 'Work as bodyguard in tavern']
quest_p2 = ['Spy ill behaving citizen', 'Work as Inkeeper help', 'Brawl with thugs']
quest_p3 = ['Travel back to crossroads', 'Help mayor solve conspiracy']


def castle():
    while True:
        print(random.choice(quest_p1))
        name_question = input("Want to try ?")
        name_question = name_question.capitalize()
        if name_question == "Y":
            name = True
            break
        else:
            print("\nSo maybe something else.\n")

    coin = random.randint(1, 10)

    while True:
        print(random.choice(quest_p2))
        name_question = input("Want to try ?")
        name_question = name_question.capitalize()
        if name_question == "Y":
            name = True
            break
        else:
            print("\nSo maybe something else.\n")

    coin = random.randint(5, 15)

    while True:
        print(random.choice(quest_p3))
        name_question = input("Want to try ?")
        name_question = name_question.capitalize()
        if name_question == "Y":
            name = True
            break
        else:
            print("\nSo maybe something else.\n")

    coin = random.randint(10,25)


    coin = coin + coin + coin
    return coin